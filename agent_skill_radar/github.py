from __future__ import annotations

import json
import os
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any


class GitHubAPIError(RuntimeError):
    """Raised when the GitHub API returns an unusable response."""


@dataclass
class GitHubClient:
    token: str | None = None
    sleep_seconds: float = 0.8

    def __post_init__(self) -> None:
        if self.token is None:
            self.token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
        if self.token is None:
            self.token = read_gh_token()

    def request_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        if path.startswith("http"):
            url = path
            if params:
                separator = "&" if "?" in url else "?"
                url = url + separator + urllib.parse.urlencode(params)
        else:
            url = "https://api.github.com" + path
            if params:
                url = url + "?" + urllib.parse.urlencode(params)

        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "agent-skill-radar",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read().decode("utf-8")
                if self.sleep_seconds:
                    time.sleep(self.sleep_seconds)
                return json.loads(payload)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise GitHubAPIError(f"GitHub API {exc.code} for {url}: {body[:500]}") from exc
        except urllib.error.URLError as exc:
            raise GitHubAPIError(f"GitHub API request failed for {url}: {exc}") from exc

    def search_repositories(
        self,
        query: str,
        limit: int = 20,
        sort: str = "stars",
        order: str = "desc",
    ) -> list[dict[str, Any]]:
        data = self.request_json(
            "/search/repositories",
            {
                "q": query,
                "sort": sort,
                "order": order,
                "per_page": max(1, min(limit, 100)),
            },
        )
        return data.get("items", [])[:limit]

    def search_issues(
        self,
        repo: str,
        since: str,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        query = f"repo:{repo} is:issue created:>={since}"
        data = self.request_json(
            "/search/issues",
            {
                "q": query,
                "sort": "comments",
                "order": "desc",
                "per_page": max(1, min(limit * 3, 100)),
            },
        )
        issues = data.get("items", [])
        return [normalize_issue(issue) for issue in issues[:limit]]


def normalize_repo(item: dict[str, Any], query_label: str) -> dict[str, Any]:
    owner = item.get("owner") or {}
    return {
        "full_name": item.get("full_name"),
        "name": item.get("name"),
        "owner": owner.get("login"),
        "description": item.get("description") or "",
        "url": item.get("html_url"),
        "stars": int(item.get("stargazers_count") or 0),
        "forks": int(item.get("forks_count") or 0),
        "open_issues": int(item.get("open_issues_count") or 0),
        "language": item.get("language") or "",
        "topics": item.get("topics") or [],
        "created_at": item.get("created_at") or "",
        "pushed_at": item.get("pushed_at") or "",
        "query_label": query_label,
    }


def normalize_issue(item: dict[str, Any]) -> dict[str, Any]:
    reactions = item.get("reactions") or {}
    labels = item.get("labels") or []
    return {
        "number": item.get("number"),
        "title": item.get("title") or "",
        "url": item.get("html_url") or "",
        "state": item.get("state") or "",
        "comments": int(item.get("comments") or 0),
        "reactions": int(reactions.get("total_count") or 0),
        "created_at": item.get("created_at") or "",
        "updated_at": item.get("updated_at") or "",
        "labels": [label.get("name", "") for label in labels if isinstance(label, dict)],
    }


def read_gh_token() -> str | None:
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    token = result.stdout.strip()
    return token or None
