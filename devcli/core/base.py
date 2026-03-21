import subprocess
from pathlib import Path
from devcli.templates.base import make_dir, make_file


def run_uv_init(project_path: Path) -> None:
    subprocess.run(
        ["uv", "init", project_path.name],
        cwd=project_path.parent,
        check=True,
    )


def create_base_structure(project_path: Path) -> None:
    dirs = [
        "app/api",
        "app/dependencies",
        "src/services",
        "src/database",
        "utils",
        "models",
        "config",
        "tests",
        "docs",
        "scripts",
    ]
    for d in dirs:
        make_dir(project_path / d)

    make_file(project_path / "app" / "main.py", 'def main():\n    pass\n')
    make_file(project_path / "config" / "settings.py", '# Application settings\n')
    make_file(project_path / "config" / "logging.py", '# Logging configuration\n')
    make_file(project_path / ".env", '')
    make_file(project_path / ".env.example", '# Copy this to .env and fill in values\n')
    make_file(project_path / ".gitignore", _gitignore_content())
    make_file(project_path / ".dockerignore", _dockerignore_content())
    make_file(project_path / ".gitattributes", '* text=auto\n')
    make_file(project_path / ".python-version", '3.11\n')
    make_file(project_path / "requirements.txt", '')
    make_file(project_path / "ISSUES.md", '# Issues\n\nTrack known issues and bugs here.\n')


def _gitignore_content() -> str:
    return """\
__pycache__/
*.py[cod]
*.egg-info/
dist/
.venv/
.env
.mypy_cache/
.ruff_cache/
.pytest_cache/
"""


def _dockerignore_content() -> str:
    return """\
__pycache__/
*.py[cod]
.venv/
.env
.git/
"""
