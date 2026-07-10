# Decepticon GitHub Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create NetVar1337’s GitHub profile README as a concise Decepticon.red owner/operator profile.

**Architecture:** A single static `README.md` uses GitHub-flavored Markdown and one immutable, externally hosted brand asset from the Decepticon landing repository. It contains no executable code, dynamic status widgets, or dependencies; URLs carry readers to the canonical product, public project, research project, and Discord contact.

**Tech Stack:** GitHub-flavored Markdown; GitHub raw-content asset hosting.

## Global Constraints

- Use `https://raw.githubusercontent.com/PurpleAILAB/decepticon-landing/7e06cea49f02f80501c1f0056213563a8b751bd4/public/logo.png` for the Decepticon logo.
- Identify NetVar as an owner of [Decepticon.red](https://decepticon.red/) and expose Discord username `netvar`.
- Claims are limited to the official Decepticon site: runtime-enforced scope and Rules of Engagement, OPPLAN execution tracking, and specialist agents grounded in ATT&CK and Skillogy.
- Include direct links to Decepticon.red, `PurpleAILAB/Decepticon`, and `NetVar1337/decepticon-ghidra-mcp`; display Discord username `netvar` as plain text.
- Exclude videos, animated assets, dynamic counters/stat cards, badges, benchmark figures, pricing, and beta dates.
- README must remain useful as plain text and give the logo descriptive alt text.

---

### Task 1: Create the static profile README

**Files:**
- Create: `README.md`
- Test: GitHub raw asset URL and Markdown link destinations

**Interfaces:**
- Consumes: GitHub Markdown image and link syntax.
- Produces: the repository-root `README.md`, automatically shown by GitHub when this repository is published as `NetVar1337/NetVar1337`.

- [ ] **Step 1: Create the README with the approved content**

Write `README.md` exactly as follows:

```markdown
<p align="center">
  <a href="https://decepticon.red/">
    <img src="https://raw.githubusercontent.com/PurpleAILAB/decepticon-landing/7e06cea49f02f80501c1f0056213563a8b751bd4/public/logo.png" alt="Decepticon" width="360" />
  </a>
</p>

<h1 align="center">NetVar</h1>

<p align="center">
  Owner, <a href="https://decepticon.red/"><strong>Decepticon.red</strong></a><br />
  Governed AI red-team control plane · Discord: <code>netvar</code>
</p>

> Autonomous red-team execution, under operator control.

- **Runtime controls** — scope and Rules of Engagement are enforced before actions fire.
- **Execution clarity** — the OPPLAN tracks objectives, blockers, pivots, evidence, and next actions.
- **Specialist agents** — recon, initial access, and post-exploitation are grounded in ATT&CK and Skillogy context.

<p align="center">
  <a href="https://decepticon.red/">Decepticon.red</a> ·
  <a href="https://github.com/PurpleAILAB/Decepticon">Decepticon</a> ·
  <a href="https://github.com/NetVar1337/decepticon-ghidra-mcp">Ghidra MCP</a> ·
  <span>Discord: netvar</span>
</p>
```

- [ ] **Step 2: Verify the asset and all public URLs resolve**

Run these commands from the repository root:

```bash
curl --fail --silent --show-error --output /dev/null https://raw.githubusercontent.com/PurpleAILAB/decepticon-landing/7e06cea49f02f80501c1f0056213563a8b751bd4/public/logo.png
curl --fail --silent --show-error --output /dev/null https://decepticon.red/
curl --fail --silent --show-error --output /dev/null https://github.com/PurpleAILAB/Decepticon
curl --fail --silent --show-error --output /dev/null https://github.com/NetVar1337/decepticon-ghidra-mcp
git diff --check
```

Expected: every `curl` command exits `0`, and `git diff --check` prints no whitespace errors.

- [ ] **Step 3: Inspect the Markdown for the required profile content**

Run:

```bash
grep -F "Owner," README.md
grep -F "Rules of Engagement" README.md
grep -F "ATT&CK and Skillogy" README.md
grep -F "Discord: netvar" README.md
```

Expected: each command prints exactly one matching README line.

- [ ] **Step 4: Commit the completed README**

```bash
git add README.md
git commit -m "docs: add Decepticon profile README"
```

Expected: Git reports one new `README.md` file in the commit.
