from pathlib import Path
from devskills.templates.helpers import make_dir, make_file


def create(project_path: Path) -> None:
    claude_dir = project_path / ".claude"
    make_dir(claude_dir)
    make_dir(claude_dir / "skills")

    make_file(
        claude_dir / "CLAUDE.md",
        "# Project Context\n\nDescribe this project for Claude Code here.\n",
    )
    make_file(
        claude_dir / "AGENTS.md",
        "# Agents\n\nDescribe agent roles and responsibilities here.\n",
    )
