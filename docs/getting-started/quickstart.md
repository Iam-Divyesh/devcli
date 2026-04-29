# Quick Start

## 1. Scaffold a new project

```bash
dev start
```

You'll be asked four questions:

**Project name**
```
Project name (or . to scaffold in current folder): my-ai-api
```

**Project structure**
```
❯ AI / ML    app/  src/inference  src/services  src/database  models/  tests/  docs/  .github/
  API        app/  src/services  src/database  tests/  docs/  config/
  Minimal    app/  tests/  config/
  None       empty project (just pyproject.toml + .gitignore)
```

**Optional features**
```
◉ [Docker]    Dockerfile + .dockerignore
◉ [Claude]    .claude/ folder for Claude Code integration
```

**Virtual environment**
```
❯ Yes — create .venv now (runs uv venv)
  No  — I'll do it manually
```

---

## 2. Enter your project and sync dependencies

```bash
cd my-ai-api
uv sync
```

---

## 3. Copy environment variables

```bash
cp .env.example .env
# fill in your API keys
```

---

## 4. Start building

Your project structure is ready. If you selected **Claude**, open Claude Code in the project directory — it will read `.claude/CLAUDE.md` and understand your project layout immediately.

```bash
claude  # opens Claude Code
```

---

## Next steps

- Browse available Claude Code skills: `dev skills list`
- Find a skill for your use case: `dev skills find <keyword>`
- Read the full [dev start reference](../commands/start.md)
