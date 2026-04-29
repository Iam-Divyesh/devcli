import questionary
from questionary import Style
from rich.console import Console

console = Console()

_style = Style([
    ("qmark",        "fg:#ff4444 bold"),
    ("question",     "fg:#ffffff bold"),
    ("instruction",  "fg:#555555 italic"),
    ("pointer",      "fg:#ff4444 bold"),
    ("highlighted",  "fg:#ff4444 bold"),
    ("selected",     "fg:#ff6666 bold"),
    ("separator",    "fg:#444444"),
    ("answer",       "fg:#ff6666 bold"),
])


def ask_location() -> str:
    name = questionary.text(
        "Project name  (or . to scaffold in current folder):",
        style=_style,
    ).ask()
    if name is None:
        raise KeyboardInterrupt
    return name.strip()


def ask_structure() -> str:
    return questionary.select(
        "Project structure:",
        choices=[
            questionary.Choice(
                "  AI / ML    app/  src/inference  src/services  src/database  models/  tests/  docs/  .github/",
                value="aiml",
            ),
            questionary.Choice(
                "  API        app/  src/services  src/database  tests/  docs/  config/",
                value="api",
            ),
            questionary.Choice(
                "  Minimal    app/  tests/  config/",
                value="minimal",
            ),
            questionary.Choice(
                "  None       empty project  (just pyproject.toml + .gitignore)",
                value="none",
            ),
        ],
        style=_style,
    ).ask()


def ask_features() -> list[str]:
    selected = questionary.checkbox(
        "Select features to scaffold  (space = toggle, enter = confirm):",
        choices=[
            questionary.Choice(title="[Docker]    Dockerfile + .dockerignore", value="docker"),
            questionary.Choice(title="[Claude]    .claude/ folder for Claude Code integration", value="claude"),
        ],
        style=_style,
        instruction=" ",
    ).ask()
    return selected if selected is not None else []


def ask_venv() -> bool:
    choice = questionary.select(
        "Create virtual environment (.venv)?",
        choices=[
            questionary.Choice("  Yes — create .venv now  (runs uv venv)", value=True),
            questionary.Choice("  No  — I'll do it manually", value=False),
        ],
        style=_style,
    ).ask()
    return bool(choice)


def ask_skills_select(refs: list[str]) -> list[str]:
    _reset_windows_console()
    print()
    selected = questionary.select(
        "Select a skill to install  (arrow keys + enter):",
        choices=[questionary.Choice(title=ref, value=ref) for ref in refs],
        style=_style,
    ).ask()
    return [selected] if selected is not None else []


def _reset_windows_console() -> None:
    """Re-enable Virtual Terminal Processing so questionary renders correctly
    after subprocess output has potentially changed the console mode."""
    import os
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        kernel32.SetConsoleMode(
            handle,
            0x0001 | 0x0002 | 0x0004,  # PROCESSED | WRAP_AT_EOL | VIRTUAL_TERMINAL_PROCESSING
        )
    except Exception:
        pass


def ask_confirm(location: str, structure: str, features: list[str]) -> bool:
    console.print(f"\n  [dim]Location   :[/dim] {location}")
    console.print(f"  [dim]Structure  :[/dim] {structure}")
    console.print(f"  [dim]Features   :[/dim] {', '.join(features) if features else '(none)'}")
    console.print()
    return questionary.confirm("Looks good?", default=True, style=_style).ask()
