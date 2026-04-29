# dev skills

Manage Claude Code skills from [skills.sh](https://skills.sh).

!!! note "Requirement"
    These commands require a `.claude/` folder in your current directory.
    Create one by running `dev start` and selecting the **Claude** feature.

---

## dev skills find

Search for a skill by keyword and install it interactively.

```bash
dev skills find <keyword>
```

**Example:**

```bash
dev skills find debugging
```

This searches skills.sh, presents a list of matches, and installs your selection into `.claude/skills/`.

---

## dev skills install

Install one or more skills directly by their `owner/repo` reference.

```bash
dev skills install <owner/repo> [<owner/repo> ...]
```

**Examples:**

```bash
# Install a single skill
dev skills install anthropics/skills

# Install multiple skills at once
dev skills install anthropics/skills some-other/skill
```

---

## dev skills list

Browse the top skills from the skills.sh leaderboard.

```bash
dev skills list
```

Displays a table of top-ranked skills with their names and descriptions. Use this to discover what's available before running `dev skills find` or `dev skills install`.

---

## How skills work

Skills are installed into `.claude/skills/` in your project. Claude Code automatically reads them and uses them as reusable instructions for tasks like testing, deploying, or debugging.

Learn more at [skills.sh](https://skills.sh).
