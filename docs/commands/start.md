# dev start

Scaffold a new AI/ML production project interactively.

```bash
dev start
```

No flags. All configuration is done through interactive prompts.

---

## Prompts

### 1. Project name

```
Project name (or . to scaffold in current folder):
```

- Type a name to create a new subdirectory (e.g. `my-agent`)
- Type `.` to scaffold directly in the current directory

---

### 2. Project structure

Choose the folder layout that matches your project type:

| Option | Directories created |
|--------|-------------------|
| **AI / ML** | `app/` `src/inference/` `src/services/` `src/database/` `models/` `tests/` `docs/` `config/` `.github/workflows/` |
| **API** | `app/` `src/services/` `src/database/` `tests/` `docs/` `config/` |
| **Minimal** | `app/` `tests/` `config/` |
| **None** | Empty project — just `pyproject.toml` + `.gitignore` |

All structures include:

- `pyproject.toml` (via `uv init`)
- `.gitignore` (pre-configured for Python + ML artifacts)
- `.python-version` (set to `3.11`)
- `app/main.py`
- `.env` + `.env.example`

---

### 3. Optional features

Toggle with `space`, confirm with `enter`:

**Docker**

Adds:
```
Dockerfile
.dockerignore
```

**Claude**

Adds:
```
.claude/
├── CLAUDE.md       # Project context for Claude Code
└── AGENTS.md       # Agent instructions
```

---

### 4. Virtual environment

```
❯ Yes — create .venv now (runs uv venv)
  No  — I'll do it manually
```

Choosing **Yes** runs `uv venv` in the project directory immediately.

---

## What gets created (AI/ML example)

```
my-ai-api/
├── app/
│   └── main.py
├── src/
│   ├── inference/
│   ├── services/
│   └── database/
├── models/
├── tests/
├── docs/
├── config/
│   └── settings.py
├── .github/
│   └── workflows/
├── .claude/            # if Claude selected
│   ├── CLAUDE.md
│   └── AGENTS.md
├── Dockerfile          # if Docker selected
├── .dockerignore       # if Docker selected
├── .env
├── .env.example
├── .gitignore
├── .python-version
└── pyproject.toml
```

---

## Idempotent

Running `dev start` on an existing directory is safe — it will not overwrite files that already exist.
