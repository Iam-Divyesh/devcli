import subprocess
from pathlib import Path
from devskills.templates.helpers import make_dir, make_file


def run_uv_init(project_path: Path, location: str) -> None:
    if location == ".":
        subprocess.run(["uv", "init", "."], cwd=project_path, check=True)
    else:
        subprocess.run(["uv", "init", project_path.name], cwd=project_path.parent, check=True)


def run_uv_venv(project_path: Path) -> None:
    subprocess.run(["uv", "venv"], cwd=project_path, check=True)


_STRUCTURE_DIRS = {
    "none": [],
    "aiml": [
        "app",
        "src/inference",
        "src/services",
        "src/database",
        "models",
        "tests",
        "docs",
        "config",
        ".github/workflows",
    ],
    "api": [
        "app",
        "src/services",
        "src/database",
        "tests",
        "docs",
        "config",
    ],
    "minimal": [
        "app",
        "tests",
        "config",
    ],
}


def create_base(project_path: Path, structure: str = "aiml") -> None:
    dirs = _STRUCTURE_DIRS.get(structure, _STRUCTURE_DIRS["aiml"])
    for d in dirs:
        make_dir(project_path / d)

    make_file(project_path / ".gitignore", _gitignore_content())
    make_file(project_path / ".python-version", "3.11\n")

    if structure == "none":
        return

    make_file(project_path / "app" / "main.py", "def main():\n    pass\n")
    make_file(project_path / "config" / "settings.py", "# Application settings\n")
    make_file(project_path / ".env", "")
    make_file(project_path / ".env.example", "# Copy this to .env and fill in values\n")


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
