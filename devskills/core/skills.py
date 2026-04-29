import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import httpx
from rich.console import Console

console = Console()

_SKILLS_SH_API = "https://skills.sh/api"


@dataclass
class Skill:
    ref: str          # owner/repo format e.g. "anthropics/skills/pdf"
    name: str         # short name e.g. "pdf"
    description: str
    installs: str     # display string e.g. "44.9K"


def search_skills_sh(query: str) -> list[str]:
    try:
        # Tee approach: pipe stdout+stderr through Python so we can both
        # display and capture in one run, without letting npx touch the
        # Windows console mode (which would break questionary afterwards)
        proc = subprocess.Popen(
            ["npx", "skills", "find", query],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )
        lines = []
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            lines.append(line)
        proc.wait()

        combined = "".join(lines)
        # strip ANSI codes, normalise line endings
        clean = re.sub(r"\x1b(?:[@-Z\\-_]|\[[0-9;?]*[ -/]*[@-~])", "", combined)
        clean = clean.replace("\r\n", "\n").replace("\r", "\n")

        refs = re.findall(
            r"^\s*(\S+)\s+[\d.,]+[KMBkmb]?\s+installs",
            clean,
            re.MULTILINE,
        )
        return refs
    except FileNotFoundError:
        console.print("npx is required. Install Node.js from https://nodejs.org")
        return []


def list_top_skills() -> list[Skill]:
    try:
        r = httpx.get(f"{_SKILLS_SH_API}/top", timeout=8)
        r.raise_for_status()
        return [_parse_skill(s) for s in r.json()]
    except Exception:
        return []


def install_skill(ref: str, target: Path) -> None:
    # ref is "owner/repo@skill-name" — split into repo + skill
    if "@" in ref:
        repo, skill_name = ref.split("@", 1)
        cmd = ["npx", "skills", "add", repo, "--skill", skill_name, "-a", "claude-code", "-y"]
    else:
        repo = ref
        skill_name = ref.rstrip("/").split("/")[-1]
        cmd = ["npx", "skills", "add", repo, "-a", "claude-code", "-y"]

    result = subprocess.run(cmd, shell=True, cwd=target)
    if result.returncode != 0:
        console.print(f"  [red]✗[/red] Failed to install {ref} (exit {result.returncode})")


def assert_claude_dir(cwd: Path) -> Path:
    claude_dir = cwd / ".claude"
    if not claude_dir.exists():
        console.print("\n  [red]No .claude/ folder found in current directory.[/red]")
        console.print("  Run [bold]dev start[/bold] and select Claude to initialise it,")
        console.print("  or create .claude/ manually.\n")
        sys.exit(1)
    return claude_dir


def _parse_skill(data: dict) -> Skill:
    ref = data.get("ref") or data.get("name", "")
    name = ref.rstrip("/").split("/")[-1] if ref else ""
    return Skill(
        ref=ref,
        name=name,
        description=data.get("description", ""),
        installs=data.get("installs", ""),
    )
