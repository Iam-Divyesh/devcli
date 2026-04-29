# devskills-cli

An interactive CLI to scaffold AI/ML production projects using the `uv` package manager. No flags — just prompts.

## Installation

```bash
pip install devskills-cli
```

Requires Python 3.10+ and [`uv`](https://docs.astral.sh/uv/getting-started/installation/).

---

## Commands

### `dev start` — Scaffold a new project

Run this inside any directory:

```bash
dev start
```

It will ask you four questions:

1. **Project name** — type a name to create a new folder, or `.` to scaffold in the current directory
2. **Project structure** — choose one:
   - `AI / ML` — includes `app/`, `src/inference/`, `src/services/`, `src/database/`, `models/`, `tests/`, `docs/`, `config/`, `.github/`
   - `API` — includes `app/`, `src/services/`, `src/database/`, `tests/`, `docs/`, `config/`
   - `Minimal` — includes `app/`, `tests/`, `config/`
   - `None` — empty project (just `pyproject.toml` + `.gitignore`)
3. **Optional features** — space to toggle, enter to confirm:
   - `Docker` — adds `Dockerfile` and `.dockerignore`
   - `Claude` — adds `.claude/` folder for [Claude Code](https://claude.ai/code) integration
4. **Create `.venv` now?** — runs `uv venv` immediately if yes

After confirming, your project is ready with next steps printed on screen.

---

### `dev skills` — Manage Claude Code skills

These commands require a `.claude/` folder in your current directory (created by `dev start` when you select the Claude feature).

#### Search and install a skill

```bash
dev skills find <keyword>
```

Searches [skills.sh](https://skills.sh) for matching skills, lets you pick one, and installs it into `.claude/skills/`.

Example:

```bash
dev skills find debugging
```

#### Install a specific skill directly

```bash
dev skills install <owner/repo>
```

Install one or more skills by their reference without searching:

```bash
dev skills install anthropics/skills
dev skills install anthropics/skills some-other/skill
```

#### Browse top skills

```bash
dev skills list
```

Shows the top skills from the [skills.sh](https://skills.sh) leaderboard in a table.

---

## Example Workflow

```bash
# Install the CLI
pip install devskills-cli

# Scaffold a new AI project
dev start
# > Project name: my-agent
# > Structure: AI / ML
# > Features: [x] Claude  [ ] Docker
# > Create .venv? Yes

cd my-agent
uv sync
cp .env.example .env

# Browse and install Claude Code skills
dev skills list
dev skills find pdf
```

---

## Requirements

| Tool | Purpose |
|---|---|
| Python 3.10+ | Runtime |
| [`uv`](https://docs.astral.sh/uv/getting-started/installation/) | Project init and virtualenv |
| [Node.js / npx](https://nodejs.org) | Only needed for `dev skills` commands |

---

## Links

- PyPI: [pypi.org/project/devskills-cli](https://pypi.org/project/devskills-cli/)
- Skills marketplace: [skills.sh](https://skills.sh)
