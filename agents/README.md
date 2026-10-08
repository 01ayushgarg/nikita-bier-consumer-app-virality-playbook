# Coding agent support

This repo has one canonical agent skill: [`../SKILL.md`](../SKILL.md). Keep the whole repository together so the skill can read its relative references in `references/`, `templates/` and `examples/`.

## Native skill installs

### Codex

Codex discovers user skills from `~/.agents/skills`. Install the full repo:

```bash
git clone https://github.com/01ayushgarg/nikita-bier-consumer-app-virality-playbook \
  ~/.agents/skills/nikita-bier-consumer-app-virality-playbook
```

Then ask:

```text
Run the Nikita Bier playbook audit on my app.
```

### Claude Code

Claude Code can load this repo as a skill folder:

```bash
git clone https://github.com/01ayushgarg/nikita-bier-consumer-app-virality-playbook \
  ~/.claude/skills/nikita-bier-consumer-app-virality-playbook
```

## Rule and instruction adapters

These agents do not all have the same native skill format. Use the adapter file for the agent and keep it pointing at the canonical `SKILL.md`.

| Agent | Adapter in this repo | How to use |
|---|---|---|
| Cursor | [`cursor-rules.md`](cursor-rules.md) | Copy into `.cursor/rules/nikita-bier-playbook.mdc` or paste into a project rule. |
| GitHub Copilot | [`github-copilot-instructions.md`](github-copilot-instructions.md) | Copy into `.github/copilot-instructions.md` or merge into an existing Copilot instructions file. |
| Windsurf | [`windsurf-rules.md`](windsurf-rules.md) | Copy into `.windsurf/rules/nikita-bier-playbook.md` or paste into Windsurf rules. |
| Cline / Roo Code | [`cline-roo-rules.md`](cline-roo-rules.md) | Add to custom instructions or project rules. |
| Gemini CLI | [`gemini.md`](gemini.md) | Copy into `GEMINI.md` in the target project or reference it from your existing Gemini instructions. |
| OpenCode | [`opencode-instructions.md`](opencode-instructions.md) | Add to project instructions or agent rules. |
| Aider | [`aider-conventions.md`](aider-conventions.md) | Add to `.aider.conf.yml` as a read-only conventions file or paste into `/read` context. |

## Manual fallback

If an agent cannot load files, paste [`../SKILL.md`](../SKILL.md) into the chat and attach:

1. [`../references/benchmarks.md`](../references/benchmarks.md)
2. the reference chapters the skill asks for
3. any relevant template from [`../templates/`](../templates/)

Do not maintain separate copies of the playbook logic in these adapter files. Update `SKILL.md` first, then keep adapters as thin pointers to it.
