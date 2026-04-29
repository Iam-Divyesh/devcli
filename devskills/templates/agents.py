from pathlib import Path
from devskills.templates.base import make_dir, make_file


def create(project_path: Path) -> None:
    for folder in ["agents", "prompts", "tools", "memory"]:
        dir_path = project_path / folder
        make_dir(dir_path)
        make_file(dir_path / ".gitkeep")
