# devskills-cli

**An interactive CLI to scaffold AI/ML production projects using the `uv` package manager. No flags — just prompts.**

---

## Why devskills-cli?

Starting an AI/ML API project involves the same repetitive setup every time — folder structure, `.gitignore`, Docker config, Claude Code integration. `devskills-cli` does all of that in under 60 seconds.

```bash
pip install devskills-cli
dev start
```

That's it. Answer four questions, get a production-ready project.

---

## What it does

=== "dev start"

    Scaffolds a complete project structure interactively:

    - Pick a project name (or scaffold in the current directory)
    - Choose a structure: **AI/ML**, **API**, **Minimal**, or **None**
    - Add optional features: **Docker**, **Claude Code**
    - Create a `.venv` immediately

=== "dev skills"

    Manages Claude Code skills from [skills.sh](https://skills.sh):

    - `dev skills find <keyword>` — search and install
    - `dev skills install <owner/repo>` — install directly
    - `dev skills list` — browse top skills

---

## Quick example

```bash
dev start
# > Project name: my-ai-api
# > Structure: AI / ML
# > Features: [x] Claude  [x] Docker
# > Create .venv? Yes

cd my-ai-api
uv sync
```

Your project is ready. Claude Code knows the layout. Docker is configured. Start building.

---

## Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Runtime |
| [uv](https://docs.astral.sh/uv/) | latest | Project init and virtualenv |
| [Node.js / npx](https://nodejs.org) | any | `dev skills` commands only |

---

## Links

- **PyPI:** [pypi.org/project/devskills-cli](https://pypi.org/project/devskills-cli/)
- **GitHub:** [github.com/Iam-Divyesh/devcli](https://github.com/Iam-Divyesh/devcli)
- **Skills marketplace:** [skills.sh](https://skills.sh)
