<div align="center">

# NetVar

`Game Security` · `Anti-Cheat` · `Reverse Engineer` · `Developer`

**I work on keeping multiplayer games fair: understanding how cheats actually work, then building the detections that catch them.**

Game security & anti-cheat · Windows internals · IDA / Ghidra · detection engineering · SQL & telemetry

<br/>

<a href="https://github.com/BitterSecurity"><img src="https://img.shields.io/badge/Bitter_Security-Decepticon-8B5CF6?style=flat-square&logo=github&logoColor=white" alt="Bitter Security" /></a>
<a href="https://decepticon.red"><img src="https://img.shields.io/badge/decepticon.red-live-22D3EE?style=flat-square" alt="decepticon.red" /></a>
<a href="https://x.com/NetVar1337"><img src="https://img.shields.io/badge/X-@NetVar1337-0F172A?style=flat-square&logo=x&logoColor=white" alt="X" /></a>
<a href="https://tryhackme.com/p/netvar"><img src="https://img.shields.io/badge/TryHackMe-netvar-212C42?style=flat-square&logo=tryhackme&logoColor=white" alt="TryHackMe" /></a>
<a href="https://discord.com/users/netvar"><img src="https://img.shields.io/badge/Discord-netvar-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord" /></a>
<img src="https://img.shields.io/badge/Available-for_security_work-22C55E?style=flat-square" alt="Available for security work" />

</div>

---

I work where **game security**, **low-level systems** and **detection engineering** meet.

That means taking apart how cheats and anti-cheat actually behave — kernel drivers, DMA
hardware, aim automation, input emulation — and turning that understanding into detections,
telemetry queries and reports a security team can act on. Understanding the attack is the
prerequisite; building the defence is the job.

I co-build **[Decepticon](https://github.com/BitterSecurity/Decepticon)** — an autonomous
red-team agent with 5.6k+ stars — and **[Vigilo](https://github.com/BitterSecurity/Vigilo)**,
an AI researcher for Web3 bounties and audit contests.

> Know how the cheat works, and you know exactly what behaviour to measure.

## Focus

<table>
<tr>
<td width="33%" valign="top">

### Game Security & Anti-Cheat
Cheat taxonomy for FPS titles, behavioral aim detection, match-integrity analytics, HWID and account-economy abuse, cheat-community intelligence.

`anti-cheat` `detection engineering` `telemetry` `SQL` `Apex / FPS`

</td>
<td width="33%" valign="top">

### Reverse Engineering
Static + dynamic analysis of native code, drivers and anti-tamper. Kernel emulation, VT-x research, protocol recovery — the ground truth behind every detection.

`IDA Pro` `Ghidra` `x64dbg` `WinDbg` `Frida` `Unicorn`

</td>
<td width="33%" valign="top">

### Development
C/C++, Rust, Go, Zig, Python, TypeScript, SQL. Detection pipelines, MCP servers, desktop tooling, embedded Linux.

`systems` `CLI` `MCP` `data` `desktop`

</td>
</tr>
</table>

## Game security work

The defence-in-depth stack I build and study — host signals → static signals → behavioral
signals → economic/account signals → intelligence.

| Project | What it is |
|:---|:---|
| **[apex-anticheat-lab](https://github.com/NetVar1337/apex-anticheat-lab)** | FPS anti-cheat lab: cheat taxonomy, aim-kinematics detections, match-integrity SQL, YARA, host survey |
| **[cheat-intel](https://github.com/NetVar1337/cheat-intel)** | Cheat-community intelligence: monitoring methodology, trend reports, the intel → detection feedback loop |
| **[account-security](https://github.com/NetVar1337/account-security)** | ATO, credential stuffing, session and identity abuse detection — signal catalogue + SQL + scoring |
| **[Kevlar](https://github.com/NetVar1337/Kevlar-Ultimate)** | Windows kernel-driver emulation & behavioral analysis (Unicorn) |
| **[unknowncheats-mcp](https://github.com/NetVar1337/unknowncheats-mcp)** | Structured access to public cheat-community research threads |

**How I work on a cheat problem:**

1. **Taxonomy first** — name the class (aimbot / triggerbot / ESP / DMA / macro / spoofing /
   boosting) and which detection layer it can possibly show up in.
2. **Behaviour over binaries** — signatures expire in days; aim kinematics, input timing and
   economic behaviour survive cheat rewrites and hardware changes.
3. **Cohort before score** — mouse vs. controller, rank tier, weapon class. A pooled baseline
   produces false positives, not detections.
4. **Explainable, ranked review** — never auto-ban on one feature. Every flag carries the
   numbers that produced it.
5. **Measure the enforcement** — infection rate before/after a wave, and how fast the adversary
   adapts. Tempo is the real KPI.

## Featured work

| Project | What it is | |
|:---|:---|---:|
| **[Decepticon](https://github.com/BitterSecurity/Decepticon)** | Autonomous red-team agent — authorized assessments, RoE-aware execution | [![stars](https://img.shields.io/github/stars/BitterSecurity/Decepticon?style=flat-square&logo=github&color=8B5CF6)](https://github.com/BitterSecurity/Decepticon) |
| **[Vigilo](https://github.com/BitterSecurity/Vigilo)** | AI researcher for Web3 / smart-contract bounties and audit contests | [![stars](https://img.shields.io/github/stars/BitterSecurity/Vigilo?style=flat-square&logo=github&color=8B5CF6)](https://github.com/BitterSecurity/Vigilo) |
| **[Kevlar](https://github.com/NetVar1337/Kevlar-Ultimate)** | Windows kernel-driver emulation & behavioral analysis (Unicorn) | [![stars](https://img.shields.io/github/stars/NetVar1337/Kevlar-Ultimate?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/Kevlar-Ultimate) |
| **[Ophion](https://github.com/NetVar1337/Ophion)** | Intel VT-x research — EPT, VMCS and VM-exit interception, used for integrity and hypervisor-residency analysis | [![stars](https://img.shields.io/github/stars/NetVar1337/Ophion?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/Ophion) |
| **[Ghidra MCP](https://github.com/NetVar1337/decepticon-ghidra-mcp)** | Full Ghidra MCP (P-code, BSim, version tracking, emulation) | [![stars](https://img.shields.io/github/stars/NetVar1337/decepticon-ghidra-mcp?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/decepticon-ghidra-mcp) |
| **[omniwire](https://github.com/NetVar1337/omniwire)** | Agent-swarm infrastructure — MCP, A2A, mesh VPN, browser automation | [![stars](https://img.shields.io/github/stars/NetVar1337/omniwire?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/omniwire) |
| **[vibe-island](https://github.com/NetVar1337/vibe-island)** | Native Dynamic Island HUD for AI coding agents | [![stars](https://img.shields.io/github/stars/NetVar1337/vibe-island?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/vibe-island) |
| **[AiDA](https://github.com/NetVar1337/AiDA-Fork)** | IDA Pro 9.x plugin — AI-assisted reverse engineering | [![stars](https://img.shields.io/github/stars/NetVar1337/AiDA-Fork?style=flat-square&logo=github&color=8B5CF6)](https://github.com/NetVar1337/AiDA-Fork) |

## Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=c,cpp,rust,go,py,ts,linux,windows" alt="Languages" />
  <br/><br/>
  <img src="https://img.shields.io/badge/IDA_Pro-6B21A8?style=flat-square" alt="IDA Pro" />
  <img src="https://img.shields.io/badge/Ghidra-1F2937?style=flat-square" alt="Ghidra" />
  <img src="https://img.shields.io/badge/x64dbg-2563EB?style=flat-square" alt="x64dbg" />
  <img src="https://img.shields.io/badge/WinDbg-0078D4?style=flat-square&logo=windows&logoColor=white" alt="WinDbg" />
  <img src="https://img.shields.io/badge/Frida-FF3E00?style=flat-square" alt="Frida" />
  <img src="https://img.shields.io/badge/Unicorn-BE123C?style=flat-square" alt="Unicorn" />
  <img src="https://img.shields.io/badge/HyperDbg-15803D?style=flat-square" alt="HyperDbg" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/YARA-2C2D72?style=flat-square" alt="YARA" />
  <img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white" alt="Burp" />
  <img src="https://img.shields.io/badge/Zig-F7A41D?style=flat-square&logo=zig&logoColor=black" alt="Zig" />
</div>

## Now

- Game security & anti-cheat — cheat taxonomy, behavioral aim detection, match-integrity analytics
- Anti-cheat internals — kernel drivers, DMA hardware surface, hypervisor-level integrity research
- Cheat-community intelligence — trend monitoring and the intel → detection feedback loop
- Detection engineering — telemetry, SQL, explainable scoring, enforcement measurement

## Activity

<div align="center">
  <img src="https://raw.githubusercontent.com/NetVar1337/NetVar1337/master/assets/stats.png" alt="GitHub stats" height="180" />
  <img src="https://raw.githubusercontent.com/NetVar1337/NetVar1337/master/assets/langs.png" alt="Top languages" height="180" />
  <br/>
  <img src="https://streak-stats.demolab.com/?user=NetVar1337&hide_border=true&background=0B0F14&ring=A78BFA&fire=22D3EE&currStreakLabel=A78BFA&sideLabels=94A3B8&dates=64748B&stroke=1E293B" alt="GitHub streak" />
  <br/>
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/NetVar1337/NetVar1337/output/github-contribution-grid-snake-dark.svg" />
</div>

---

<div align="center">

Open to **game security / anti-cheat roles**, **detection engineering**, **RE / Windows internals work**, and **security-product engineering**.

[apex-anticheat-lab](https://github.com/NetVar1337/apex-anticheat-lab) · [Decepticon](https://decepticon.red) · [GitHub](https://github.com/NetVar1337) · [X](https://x.com/NetVar1337) · [TryHackMe](https://tryhackme.com/p/netvar)

```c
while (true) { if (understand_the_cheat()) build_the_detection(); }
```

</div>
