# Installation

## Prerequisites

Before installing `devskills-cli`, make sure you have:

- **Python 3.10+** — check with `python --version`
- **uv** — the fast Python package manager

Install `uv` if you don't have it:

=== "macOS / Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

---

## Install devskills-cli

```bash
pip install devskills-cli
```

Verify the installation:

```bash
dev --help
```

---

## Optional: Node.js

The `dev skills` commands use `npx` under the hood. If you plan to use them, install [Node.js](https://nodejs.org).

---

## Upgrading

```bash
pip install --upgrade devskills-cli
```
