# Coding agent support

This repo has one canonical agent skill: [`../SKILL.md`](../SKILL.md). Install or vendor the full repository, not only this `agents/` directory, so the skill can read its relative references in [`../references/`](../references/), [`../templates/`](../templates/) and [`../examples/`](../examples/).

## Paths and activation

The adapters are stored under `agents/`. Markdown-linked adapters use `../SKILL.md`
and `../references/` relative to that location; Cursor and Windsurf use project-root
paths such as `SKILL.md`. When copying rules into another project, rewrite **all**
skill and reference paths to the full repo's location, for example
`vendor/nikita-bier-consumer-app-virality-playbook/SKILL.md` and
`vendor/nikita-bier-consumer-app-virality-playbook/references/benchmarks.md`.
Do not assume a root-level `SKILL.md` is discovered by every agent.

For example, vendor the whole repo in your app project:

```bash
git clone https://github.com/william-c-stanford/nikita-bier-consumer-app-virality-playbook \
  vendor/nikita-bier-consumer-app-virality-playbook
```

Then copy or load the chosen adapter below, adjusting its paths. Merge with existing
instruction files rather than overwriting them. Ask the agent to use the playbook
explicitly; automatic attachment varies by agent and rule configuration.

## Native skill installs

Use native skill loading where the agent supports it.

### Codex

Codex user skills are installed under `~/.agents/skills`. Install the full repo there so Codex sees the skill and its supporting files:

```bash
git clone https://github.com/william-c-stanford/nikita-bier-consumer-app-virality-playbook \
  ~/.agents/skills/nikita-bier-consumer-app-virality-playbook
```

Then ask:

```text
Run the Nikita Bier playbook audit on my app.
```

Source: OpenAI Codex skills documentation: <https://developers.openai.com/codex/skills/>.

### Claude Code

Claude Code supports skills and project/user memory files. Install the full repo as a Claude skill folder when you want native skill behavior:

```bash
git clone https://github.com/william-c-stanford/nikita-bier-consumer-app-virality-playbook \
  ~/.claude/skills/nikita-bier-consumer-app-virality-playbook
```

If you instead use project instructions, point them at the vendored repo's `SKILL.md` and keep the full repo available.

Source: <https://code.claude.com/docs/en/skills>.

## Rule and instruction adapters

These agents do not all have the same native skill format. Use their rules or instruction mechanisms to point at the canonical `SKILL.md`. All seven thin adapters are linked below.

| Agent | Repo file or instruction target | How to use | Source |
|---|---|---|---|
| Cursor | [`cursor-rules.md`](cursor-rules.md) | Copy into `.cursor/rules/nikita-bier-playbook.mdc` or paste into a project rule. Retain its YAML metadata; select it explicitly with `@nikita-bier-playbook` if it is not attached automatically. If the full repo is vendored elsewhere, change `SKILL.md` in the copied rule to the vendored path. | <https://docs.cursor.com/en/context/rules> |
| GitHub Copilot | [`github-copilot-instructions.md`](github-copilot-instructions.md) | Copy into `.github/copilot-instructions.md`, merge into an existing Copilot instructions file, or use an `AGENTS.md`-style repository instruction. Adjust `../SKILL.md` if the instruction file is not copied to the same relative location. | <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions> |
| Windsurf | [`windsurf-rules.md`](windsurf-rules.md) | Create a workspace rule through Windsurf’s Rules UI and paste this adapter, choosing an activation mode (manual or always-on), or merge into a project-root `AGENTS.md`. Adjust `SKILL.md` if the repo is vendored under another path. | <https://docs.windsurf.com/windsurf/cascade/memories> |
| Cline / Roo Code | [`cline-roo-rules.md`](cline-roo-rules.md) | Paste a thin instruction that tells the agent to read the vendored repo's `SKILL.md`, then follow its references. Copy the adapter into `.roo/rules/nikita-bier-playbook.md` for Roo or `.clinerules/nikita-bier-playbook.md` for Cline and enable the rule. | <https://docs.cline.bot/features/cline-rules> and <https://docs.roocode.com/features/custom-instructions> |
| Gemini CLI | [`gemini.md`](gemini.md) | Add a `GEMINI.md` instruction that points to this repo's `SKILL.md`, or reference the vendored skill from an existing Gemini instruction file. Keep the full repo available for the relative references. | <https://geminicli.com/docs/cli/gemini-md/> |
| OpenCode | [`opencode-instructions.md`](opencode-instructions.md) | Copy the adapter into root `AGENTS.md` with rewritten paths, or add `"instructions": ["vendor/nikita-bier-consumer-app-virality-playbook/agents/opencode-instructions.md"]` to `opencode.json`. OpenCode can also consume external instruction files and some existing rule formats. | <https://opencode.ai/docs/rules/> |
| Aider | [`aider-conventions.md`](aider-conventions.md) | Load with `/read vendor/nikita-bier-consumer-app-virality-playbook/agents/aider-conventions.md` or `aider --read vendor/nikita-bier-consumer-app-virality-playbook/agents/aider-conventions.md`. Also `/read` the canonical `SKILL.md`, benchmarks and relevant chapters/templates: Aider does not automatically load linked files. | <https://aider.chat/docs/usage/conventions.html> |

## Manual fallback

If an agent cannot load files, paste [`../SKILL.md`](../SKILL.md) into the chat and attach:

1. [`../references/benchmarks.md`](../references/benchmarks.md)
2. the reference chapters the skill asks for
3. any relevant template from [`../templates/`](../templates/)

Do not maintain separate copies of the playbook logic in adapter files or agent rules. Update `SKILL.md` first, then keep native skills, rule adapters and manual instructions as thin pointers to it.
