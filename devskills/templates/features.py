from pathlib import Path
from devskills.templates.base import make_dir, make_file


def create(project_path: Path) -> None:
    feature_dir = project_path / "features" / "example_feature"
    make_dir(feature_dir)
    make_file(feature_dir / "__init__.py", "# Example feature module\n")
