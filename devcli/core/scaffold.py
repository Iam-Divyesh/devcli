import subprocess
from pathlib import Path
from devcli.templates.helpers import make_dir, make_file


def run_uv_init(project_path: Path, location: str) -> None:
    if location == ".":
        subprocess.run(["uv", "init", "."], cwd=project_path, check=True)
    else:
        subprocess.run(["uv", "init", project_path.name], cwd=project_path.parent, check=True)


def run_uv_venv(project_path: Path) -> None:
    subprocess.run(["uv", "venv"], cwd=project_path, check=True)


def create_base(project_path: Path) -> None:
    dirs = [
        "app",
        "src/inference",
        "src/services",
        "src/database",
        "models",
        "tests",
        "docs",
        "config",
        ".github/workflows",
    ]
    for d in dirs:
        make_dir(project_path / d)

    make_file(project_path / "app" / "main.py", "def main():\n    pass\n")
    make_file(project_path / "config" / "settings.py", "# Application settings\n")
    make_file(project_path / ".env", "")
    make_file(project_path / ".env.example", "# Copy this to .env and fill in values\n")
    make_file(project_path / ".gitignore", _gitignore_content())
    make_file(project_path / ".python-version", "3.11\n")


def _gitignore_content() -> str:
    return """\
models/
.env
.venv/
__pycache__/
*.pyc
dist/
*.egg-info/
"""
