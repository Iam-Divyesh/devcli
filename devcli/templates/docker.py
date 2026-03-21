from pathlib import Path
from devcli.templates.helpers import make_file


def create(project_path: Path) -> None:
    make_file(project_path / "Dockerfile", _dockerfile_content())
    make_file(project_path / ".dockerignore", _dockerignore_content())


def _dockerfile_content() -> str:
    return """\
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
"""


def _dockerignore_content() -> str:
    return """\
models/
.env
__pycache__/
*.pyc
.venv/
.git/
"""
