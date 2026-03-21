import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from devcli.core import prompts, generator, skills as skills_mod

app = typer.Typer(help="Scaffold AI production projects interactively.")
skills_app = typer.Typer(help="Search and install Claude Code skills from skills.sh.")
app.add_typer(skills_app, name="skills")

console = Console()

BANNER = """
██████╗ ███████╗██╗   ██╗.
██╔══██╗██╔════╝██║   ██║
██║  ██║█████╗  ██║   ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝
██████╔╝███████╗ ╚████╔╝
╚═════╝ ╚══════╝  ╚═══╝

THE OPEN DEV KITS ECOSYSTEM
"""


def show_banner() -> None:
    console.print(f"[bold red]{BANNER}[/bold red]")


@app.callback()
def main():
    pass


# ── dev start ────────────────────────────────────────────────────────────────

@app.command("start")
def start():
    """Scaffold a new AI/ML production project interactively."""
    show_banner()

    try:
        location = prompts.ask_location()
        features = prompts.ask_features()
        run_venv = prompts.ask_venv()

        if prompts.ask_confirm(location, features):
            generator.generate(location, features, run_venv)
    except KeyboardInterrupt:
        console.print("\n  [dim]Cancelled.[/dim]\n")
        raise typer.Exit()


# ── dev skills ────────────────────────────────────────────────────────────────

@skills_app.command("find")
def skills_find(query: str = typer.Argument(..., help="Keyword to search on skills.sh")):
    """Search skills.sh by keyword and optionally install."""
    refs = skills_mod.search_skills_sh(query)
    if not refs:
        return

    selected = prompts.ask_skills_select(refs)
    if not selected:
        return

    cwd = Path.cwd()
    skills_mod.assert_claude_dir(cwd)

    for ref in selected:
        console.print(f"  Installing [cyan]{ref}[/cyan] via npx skills add...")
        skills_mod.install_skill(ref, cwd)

    if len(selected) > 1:
        console.print(f"\n  [bold red]✓[/bold red] {len(selected)} skills installed into .claude/skills/\n")


@skills_app.command("install")
def skills_install(
    refs: list[str] = typer.Argument(..., help="One or more owner/repo refs to install"),
):
    """Install one or more skills from skills.sh into .claude/skills/."""
    cwd = Path.cwd()
    skills_mod.assert_claude_dir(cwd)

    for ref in refs:
        console.print(f"  Installing [cyan]{ref}[/cyan] via npx skills add...")
        skills_mod.install_skill(ref, cwd)

    if len(refs) > 1:
        console.print(f"\n  [bold red]✓[/bold red] {len(refs)} skills installed into .claude/skills/\n")


@skills_app.command("list")
def skills_list():
    """Browse the top skills from the skills.sh leaderboard."""
    console.print("\n  [bold]Top skills on skills.sh[/bold]  [dim](live from https://skills.sh)[/dim]\n")

    top = skills_mod.list_top_skills()

    if not top:
        console.print("  [dim]Could not reach skills.sh. Check your connection.[/dim]\n")
        return

    table = Table(border_style="dim", show_header=True, header_style="bold red")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Skill", style="cyan")
    table.add_column("Installs", justify="right", style="dim")

    for i, s in enumerate(top, 1):
        table.add_row(str(i), s.ref, s.installs or "—")

    console.print(table)
    console.print("\n  Browse all: [cyan]https://skills.sh[/cyan]")
    console.print("  Search:     [dim]dev skills find <query>[/dim]\n")
