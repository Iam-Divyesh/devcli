# Contributing to devskills-cli

This guide explains how the codebase is structured and how to make changes.

---

## Project Structure

```
devskills/
├── main.py               # CLI entry point — all commands defined here
├── core/
│   ├── prompts.py        # All interactive user prompts (questionary)
│   ├── scaffold.py       # Creates base dirs/files + runs uv init/venv
│   ├── generator.py      # Orchestrates the full project generation flow
│   └── skills.py         # Interfaces with skills.sh API and npx CLI
└── templates/
    ├── helpers.py         # make_dir() and make_file() utilities
    ├── docker.py          # Dockerfile + .dockerignore template
    ├── claude.py          # .claude/ folder template
    ├── agents.py          # agents/, prompts/, tools/, memory/ (unused in prompts)
    └── features.py        # features/example_feature/ (unused in prompts)
```

---

## Local Setup

```bash
git clone <repo>
cd "Project Commands"

# Create virtualenv and install in editable mode
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac/Linux

pip install -e .

# Test it
dev --help
dev start
```

---

## How to Make Changes

### Modify a CLI command

All commands live in `devskills/main.py`.

- `dev start` → `start()` function
- `dev skills find` → `skills_find()` function
- `dev skills install` → `skills_install()` function
- `dev skills list` → `skills_list()` function

Add a new top-level command with `@app.command("name")`, or add to the skills subgroup with `@skills_app.command("name")`.

---

### Change what gets asked during `dev start`

All interactive prompts are in `devskills/core/prompts.py`.

Each function uses `questionary` and returns a value passed to `generator.generate()`:

| Function | Returns | Used for |
|---|---|---|
| `ask_location()` | `str` | Project name or `.` |
| `ask_structure()` | `str` | `aiml`, `api`, `minimal`, `none` |
| `ask_features()` | `list[str]` | Selected feature keys |
| `ask_venv()` | `bool` | Whether to run `uv venv` |
| `ask_confirm()` | `bool` | Final yes/no confirmation |

To add a new prompt, define the function here and call it from `start()` in `main.py`.

---

### Change the base directory structure

`devskills/core/scaffold.py` controls what folders and files are created for each structure type.

Edit `_STRUCTURE_DIRS` to add or remove directories:

```python
_STRUCTURE_DIRS = {
    "aiml": [
        "app",
        "src/inference",
        # add more dirs here
    ],
    ...
}
```

Edit `create_base()` to add or change boilerplate files (e.g. `.gitignore`, `app/main.py`).

---

### Modify an existing template

Templates live in `devskills/templates/`. Each one has a `create(project_path: Path)` function.

- **Docker** → `devskills/templates/docker.py` — edit `Dockerfile` or `.dockerignore` content
- **Claude** → `devskills/templates/claude.py` — edit `.claude/CLAUDE.md` or `.claude/AGENTS.md` content

Use the helper utilities (always idempotent — safe to re-run):

```python
from devskills.templates.helpers import make_dir, make_file

make_dir(project_path / "some/new/folder")
make_file(project_path / "some/file.txt", "file content here")
```

`make_file()` will not overwrite an existing file.

---

### Add a new optional feature template

Three steps:

**1. Create the template module** in `devskills/templates/<feature>.py`:

```python
from pathlib import Path
from devskills.templates.helpers import make_dir, make_file

def create(project_path: Path) -> None:
    make_dir(project_path / "my_new_folder")
    make_file(project_path / "my_new_folder" / "example.py", "# example\n")
```

**2. Register it in `devskills/core/generator.py`**:

```python
from devskills.templates import docker, claude, my_feature  # add import

_TEMPLATE_MAP = {
    "docker": docker.create,
    "claude": claude.create,
    "my_feature": my_feature.create,  # add entry
}
```

**3. Expose it in `devskills/core/prompts.py`** inside `ask_features()`:

```python
choices=[
    questionary.Choice(title="[Docker]    Dockerfile + .dockerignore", value="docker"),
    questionary.Choice(title="[Claude]    .claude/ folder for Claude Code", value="claude"),
    questionary.Choice(title="[MyFeature] Description of your feature", value="my_feature"),  # add
],
```

The `value` string must match the key in `_TEMPLATE_MAP`.

---

### Change the skills.sh integration

`devskills/core/skills.py` handles all communication with skills.sh:

- `search_skills_sh(query)` — runs `npx skills find <query>`, parses output with regex
- `list_top_skills()` — calls `https://skills.sh/api/top` via `httpx`
- `install_skill(ref, target)` — runs `npx skills add <repo> -a claude-code -y`
- `assert_claude_dir(cwd)` — validates `.claude/` folder exists before installing

The API base URL is `_SKILLS_SH_API = "https://skills.sh/api"` — change this if the endpoint changes.

---

## Build & Publish

### Bump the version

Edit `pyproject.toml`:

```toml
[project]
version = "0.1.2"   # increment this
```

Follow [semver](https://semver.org): `MAJOR.MINOR.PATCH`
- Patch: bug fixes
- Minor: new features, backwards compatible
- Major: breaking changes

### Build

```bash
pip install build
python -m build
```

This creates:
```
dist/
  devskills_cli-0.1.2-py3-none-any.whl
  devskills_cli-0.1.2.tar.gz
```

### Test the build locally

```bash
pip install dist/devskills_cli-0.1.2-py3-none-any.whl
dev start
```

### Publish to PyPI

```bash
pip install twine
twine upload dist/*
# username: __token__
# password: your PyPI API token (store it in .env, never commit it)
```

Or with token from env:

```bash
source .env
twine upload dist/* -u __token__ -p "$PYPI_API_TOKEN"
```

---

## Dependencies

Defined in `pyproject.toml`. To add a dependency:

1. Add it under `[project] dependencies`
2. Run `pip install -e .` to update your local environment

| Package | Purpose |
|---|---|
| `typer` | CLI framework (commands, args, help text) |
| `questionary` | Interactive prompts (select, checkbox, text) |
| `rich` | Terminal colors, tables, spinners, panels |
| `httpx` | HTTP client for skills.sh API |
