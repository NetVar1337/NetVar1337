# Executive Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace NetVar1337’s short profile README with a longer, polished executive security profile centered on the Co-Owner role at Decepticon.red.

**Architecture:** A single static `README.md` uses GitHub-flavored Markdown and minimal HTML only for the centered compact logo and identity block. Semantic headings, horizontal rules, lists, and two-column tables organize the leadership narrative, operating principles, selected public work, and contact details without dynamic widgets or external presentation dependencies.

**Tech Stack:** GitHub-flavored Markdown; GitHub-supported HTML; `https://decepticon.red/logo.png`.

## Global Constraints

- Keep the logo linked to `https://decepticon.red/`, use `https://decepticon.red/logo.png`, retain `alt="Decepticon"`, and set `width="220"`.
- Use exact role text `Co-Owner, Decepticon.red` and expose Discord username `netvar` as plain text.
- Include the four approved Decepticon operating claims: runtime-enforced scope and Rules of Engagement; OPPLAN objectives, blockers, pivots, evidence, and next actions; ATT&CK/Skillogy specialist-agent context; operator-controlled observable execution.
- Include project links to Decepticon.red, PurpleAILAB/Decepticon, NetVar1337/decepticon-ghidra-mcp, NetVar1337/omniwire, and NetVar1337/unleash.
- Use semantic headings, horizontal rules, concise paragraphs, bullets, and GitHub Markdown tables only.
- Do not use animated assets, video, badges, dynamic stats, external stat cards, counters, ASCII-art framing, benchmark figures, pricing, beta dates, unverified customer claims, or unsupported personal credentials.
- Preserve readable plain text and descriptive image fallback when images do not load.

---

### Task 1: Publish the executive profile README

**Files:**
- Modify: `README.md`
- Test: live GitHub profile rendering and external destination availability

**Interfaces:**
- Consumes: GitHub Markdown image, heading, table, list, link, and inline-code syntax.
- Produces: `README.md` rendered by GitHub on `https://github.com/NetVar1337`.

- [ ] **Step 1: Replace the README with the approved content**

Write `README.md` exactly as follows:

```markdown
<p align="center">
  <a href="https://decepticon.red/">
    <img src="https://decepticon.red/logo.png" alt="Decepticon" width="220" />
  </a>
</p>

<h1 align="center">NetVar</h1>

<p align="center">
  <strong>Co-Owner, <a href="https://decepticon.red/">Decepticon.red</a></strong><br />
  Governed autonomous red-team operations · Discord: <code>netvar</code>
</p>

> Building controlled, observable AI red-team capability for serious security work.

---

## Decepticon.red

Decepticon.red is a governed AI red-team control plane for adversary emulation under rules set by the operator. It keeps autonomous execution bounded, observable, and tied to engagement evidence.

| Product | Open source |
| --- | --- |
| [Decepticon.red](https://decepticon.red/) — governed AI red-team operations | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) — autonomous red-team agent |

## Operating model

- **Runtime governance** — scope and Rules of Engagement are enforced before actions fire.
- **Execution discipline** — the OPPLAN follows objectives, blockers, pivots, evidence, and next actions as an engagement evolves.
- **Specialist context** — recon, initial access, and post-exploitation agents operate with ATT&CK and Skillogy knowledge.
- **Operator control** — engagements remain observable and constrained by explicit operator decisions.

## Research & tooling

Reverse engineering · exploit research · security audits

| Project | Focus |
| --- | --- |
| [decepticon-ghidra-mcp](https://github.com/NetVar1337/decepticon-ghidra-mcp) | Ghidra MCP tooling for P-code, BSim, version tracking, emulation, and agentic vulnerability research. |
| [omniwire](https://github.com/NetVar1337/omniwire) | Infrastructure for AI agent swarms: MCP tooling, A2A coordination, networking, browser automation, and operator controls. |
| [unleash](https://github.com/NetVar1337/unleash) | Bun SEA bytecode patch-analysis tooling with interactive workflows and signature scanning. |

## Connect

- Discord: <code>netvar</code>
- [Decepticon.red](https://decepticon.red/) · [Decepticon on GitHub](https://github.com/PurpleAILAB/Decepticon)
```

- [ ] **Step 2: Run focused static checks**

Run these commands from the repository root:

```bash
curl --fail --silent --show-error --output /dev/null https://decepticon.red/logo.png
curl --fail --silent --show-error --output /dev/null https://decepticon.red/
curl --fail --silent --show-error --output /dev/null https://github.com/PurpleAILAB/Decepticon
curl --fail --silent --show-error --output /dev/null https://github.com/NetVar1337/decepticon-ghidra-mcp
curl --fail --silent --show-error --output /dev/null https://github.com/NetVar1337/omniwire
curl --fail --silent --show-error --output /dev/null https://github.com/NetVar1337/unleash
git diff --check
```

Expected: every `curl` command exits `0`, and `git diff --check` prints no whitespace errors.

- [ ] **Step 3: Inspect required profile content**

Use the harness `grep` tool to verify that `README.md` contains exactly one occurrence each of `Co-Owner,`, `## Decepticon.red`, `## Operating model`, `## Research & tooling`, `## Connect`, `Rules of Engagement`, `ATT&CK and Skillogy`, `decepticon-ghidra-mcp`, `omniwire`, `unleash`, and `Discord: <code>netvar</code>`.

Expected: every required marker is present exactly once.

- [ ] **Step 4: Commit the completed README**

```bash
git add README.md
git commit -m "docs: expand executive profile"
```

Expected: Git reports a commit modifying only `README.md`.
