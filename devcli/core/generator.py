from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from devcli.core import scaffold
from devcli.templates import docker, claude

console = Console()

_TEMPLATE_MAP = {
    "docker": docker.create,
    "claude": claude.create,
}


def generate(location: str, selected_features: list[str], run_venv: bool = False) -> None:
    if location == ".":
        project_path = Path.cwd()
        project_name = project_path.name
    else:
        project_path = Path.cwd() / location
        project_name = location

    with console.status("[bold red]Initializing project with uv...", spinner="dots"):
        scaffold.run_uv_init(project_path, location)

    with console.status("[bold red]Creating base project structure...", spinner="dots"):
        scaffold.create_base(project_path)

    for feature in selected_features:
        handler = _TEMPLATE_MAP.get(feature)
        if handler:
            with console.status(f"[bold red]Adding {feature}...", spinner="dots"):
                handler(project_path)

    if run_venv:
        with console.status("[bold red]Creating .venv (uv venv)...", spinner="dots"):
            scaffold.run_uv_venv(project_path)

    _print_success(project_name, selected_features, run_venv)


def _print_success(project_name: str, features: list[str], run_venv: bool) -> None:
    lines = [f"[bold red]{project_name}[/bold red] created successfully\n"]

    lines.append("  [dim]Base structure[/dim]    [bold red]✓[/bold red]")
    for f in features:
        lines.append(f"  [dim]{f.capitalize():<16}[/dim] [bold red]✓[/bold red]")
    if run_venv:
        lines.append("  [dim]Virtualenv      [/dim] [bold red]✓[/bold red]  .venv/")

    lines.append(f"\n  [dim]Next steps:[/dim]")
    lines.append(f"  cd {project_name}")
    if not run_venv:
        lines.append("  uv venv")
    lines.append("  uv sync")
    lines.append("  cp .env.example .env")

    if "claude" in features:
        lines.append(
            "\n  [dim]Add skills anytime:[/dim]\n"
            "  dev skills find <keyword>\n"
            "  Browse: [cyan]https://skills.sh[/cyan]"
        )

    console.print(
        Panel(
            "\n".join(lines),
            border_style="red",
            padding=(1, 2),
        )
    )
