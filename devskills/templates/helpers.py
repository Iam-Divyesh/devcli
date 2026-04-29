from pathlib import Path


def make_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def make_file(path: Path, content: str = "") -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
