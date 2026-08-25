<div align="center">

# ⚡ NetVar1337

### `Security Researcher` · `Reverse Engineer` · `Low-Level Systems` · `Offensive AI`

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=800&color=A78BFA&center=true&vCenter=true&width=800&height=48&lines=Windows+Internals+%7C+Kernel+Drivers+%7C+VT-x+Hypervisors;Autonomous+Red-Team+Swarms+%7C+Exploit+AI;Game+Security+%7C+Anti-Cheat+Research+%7C+DMA%2FFPGA;Reverse+Engineering+%7C+IDA+Pro+%7C+Ghidra+MCP)](https://git.io/typing-svg)

<p align="center">
  <a href="https://github.com/PurpleAILAB"><img src="https://img.shields.io/badge/PurpleAILAB-Co--Founder-7C3AED?style=for-the-badge&logo=github&logoColor=white" alt="PurpleAILAB" /></a>
  <a href="https://decepticon.red"><img src="https://img.shields.io/badge/Decepticon-Autonomous_Red_Team-0D1117?style=for-the-badge&logo=target&logoColor=A78BFA" alt="Decepticon" /></a>
  <a href="https://x.com/NetVar1337"><img src="https://img.shields.io/badge/X-@NetVar1337-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" /></a>
  <a href="https://discord.com/users/netvar"><img src="https://img.shields.io/badge/Discord-netvar-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://tryhackme.com/p/netvar"><img src="https://img.shields.io/badge/TryHackMe-netvar-212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" /></a>
</p>

</div>

---

## ⚡ Overview

I build, analyze, and break systems across the entire execution stack — from userland memory spaces and kernel/hypervisor internals (Ring 0 / Ring -1) down to PCIe/FPGA hardware interfaces, and upward into autonomous, agentic offensive intelligence.

Co-founder of **[PurpleAILAB](https://github.com/PurpleAILAB)** and architect behind **[Decepticon](https://github.com/PurpleAILAB/Decepticon)** — an autonomous multi-agent red team system executing full-spectrum cyber kill chains.

> *"If you understand how the machine thinks, you control the machine."*

---

## 🔬 Core Specializations

| Layer / Domain | Focus & Techniques | Weaponry & Tooling |
|:---|:---|:---|
| **Ring -1 / Hypervisors** | VT-x virtualization, EPT/NPT hook stealth, VMCS manipulation, VMEXIT interception | C, x86_64 ASM, [Ophion](https://github.com/NetVar1337/Ophion), HyperDbg |
| **Ring 0 / Windows Kernel** | Driver architecture, manual mapping, BYOVD exploitation, DKOM, callback removal, Unicorn emulation | C++, [Kevlar](https://github.com/NetVar1337/Kevlar), WinDbg, KD |
| **Hardware & DMA** | Direct Memory Access, custom FPGA gateware, PCIe TLP generation, physical memory introspection | Verilog, C, Python, [PCILeechGen](https://github.com/NetVar1337/PCILeechGen), [dma-ai-toolkit](https://github.com/NetVar1337/dma-ai-toolkit) |
| **Reverse Engineering** | Static & dynamic binary triage, protocol deconstruction, packing/VM deobfuscation, agentic RE | IDA Pro, Ghidra, x64dbg, Frida, [AiDA-Fork](https://github.com/NetVar1337/AiDA-Fork), [decepticon-ghidra-mcp](https://github.com/NetVar1337/decepticon-ghidra-mcp) |
| **Game Security & Internals** | Memory manipulation, VMT/IAT hooks, SDK dumpers, anti-cheat analysis (EAC / BE / Vanguard) | C++, Rust, [unknowncheats-mcp](https://github.com/NetVar1337/unknowncheats-mcp), MinHook, Dumper-7 |
| **Autonomous Offensive AI** | Multi-agent swarms, MCP servers, A2A coordination, 0-day hunting pipelines, context compression | Python, TypeScript, Go, [Decepticon](https://github.com/PurpleAILAB/Decepticon), [Vigilo](https://github.com/PurpleAILAB/Vigilo), [omniwire](https://github.com/NetVar1337/omniwire) |
| **Systems & Developer Tooling** | Bun SEA bytecode patching, zero-intervention MCP lifecycles, native TUIs, Dynamic HUD overlays | Go, Zig, Rust, [unleash](https://github.com/NetVar1337/unleash), [vibe-island](https://github.com/NetVar1337/vibe-island), [mcp-ctl](https://github.com/NetVar1337/mcp-ctl) |

---

## 🛠️ Featured Arsenal

### 🤖 Autonomous Offense & Agentic Intelligence
| Repository | Description | Tech |
|:---|:---|:---|
| **[PurpleAILAB / Decepticon](https://github.com/PurpleAILAB/Decepticon)** | Autonomous Red Team Agent — end-to-end kill chains, RoE/OPPLAN execution, 98% XBOW validation | `Python` `AI Agents` `Red Team` |
| **[PurpleAILAB / Vigilo](https://github.com/PurpleAILAB/Vigilo)** | AI security agent for Web3 & smart contracts — bug bounties, audit contests, and exploit research | `TypeScript` `Web3` `Audit` |
| **[NetVar1337 / decepticon-ghidra-mcp](https://github.com/NetVar1337/decepticon-ghidra-mcp)** | Full-featured Ghidra MCP server (P-code, BSim, Version Tracking, emulation) for agentic 0-day workflows | `Java` `Ghidra` `MCP` |
| **[NetVar1337 / omniwire](https://github.com/NetVar1337/omniwire)** | Agent swarm mesh infrastructure — 88+ MCP tools, A2A protocol, mesh VPN, CDP browser automation | `TypeScript` `MCP` `VPN` |

### ⚙️ Low-Level, Kernel & Reverse Engineering
| Repository | Description | Tech |
|:---|:---|:---|
| **[NetVar1337 / Kevlar](https://github.com/NetVar1337/Kevlar)** | x64 Windows kernel-driver emulation and behavioral analysis harness powered by Unicorn Engine | `C++` `Unicorn` `Kernel` |
| **[NetVar1337 / Ophion](https://github.com/NetVar1337/Ophion)** | Stealth-focused Intel VT-x Hypervisor implementation (EPT hooking, VMCS shadow pages) | `C` `Assembly` `VT-x` |
| **[NetVar1337 / unleash](https://github.com/NetVar1337/unleash)** | Bun SEA bytecode patcher & zero-refusal runtime harness — 113 binary patches, interactive TUI | `Go` `Bytecode` `TUI` |
| **[NetVar1337 / AiDA-Fork](https://github.com/NetVar1337/AiDA-Fork)** | AI assistant plugin for IDA Pro 9.0+ accelerating complex C++ game & engine reverse engineering | `C++` `IDA Pro` `AI` |
| **[NetVar1337 / codex-patcher-cc](https://github.com/NetVar1337/codex-patcher-cc)** | Codex CLI Mach-O & Rust binary patcher and automated configuration orchestrator | `Python` `Mach-O` `Patching` |

### 🎮 Game Security, Anti-Cheat & Hardware / DMA
| Repository | Description | Tech |
|:---|:---|:---|
| **[NetVar1337 / unknowncheats-mcp](https://github.com/NetVar1337/unknowncheats-mcp)** | Fast UnknownCheats & Elitepvpers MCP server with automated Cloudflare bypass | `Rust` `MCP` `Cloudflare` |
| **[NetVar1337 / dma-ai-toolkit](https://github.com/NetVar1337/dma-ai-toolkit)** | AI-assisted PCILeech & Direct Memory Access (DMA) hardware attack research toolkit | `Python` `DMA` `PCILeech` |
| **[NetVar1337 / PCILeechGen](https://github.com/NetVar1337/PCILeechGen)** / **[pcileech-fpga](https://github.com/NetVar1337/pcileech-fpga)** | DMA firmware generator & custom FPGA modules for physical memory exploitation | `Go` `Verilog` `FPGA` |

### 🚀 Developer Systems & Desktop HUDs
| Repository | Description | Tech |
|:---|:---|:---|
| **[NetVar1337 / vibe-island](https://github.com/NetVar1337/vibe-island)** | Native Dynamic Island HUD for AI coding agents (macOS, Windows, Hyprland/Sway/GNOME/KDE) | `Rust` `Desktop` `HUD` |
| **[NetVar1337 / mcp-ctl](https://github.com/NetVar1337/mcp-ctl)** | Zero-intervention MCP server lifecycle manager and process supervisor | `Zig` `CLI` `MCP` |
| **[NetVar1337 / claude-for-firefox](https://github.com/NetVar1337/claude-for-firefox)** | Claude browser extension for Firefox with sidebar chat and workflow automation | `JavaScript` `WebExtension` |
| **[NetVar1337 / flipctld](https://github.com/NetVar1337/flipctld)** / **[flipper-profile](https://github.com/NetVar1337/flipper-profile)** | C menu-UI engine and Btrfs/OverlayFS snapshot profile manager for embedded Linux / Flipper One | `C` `Python` `Embedded` |

---

## 🧰 Tech Arsenal & Weaponry

<div align="center">

### Languages & Hardware
<p align="center">
  <img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C" />
  <img src="https://img.shields.io/badge/C++23-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Zig-F7A41D?style=flat-square&logo=zig&logoColor=black" alt="Zig" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/x86__64_ASM-3776AB?style=flat-square&logo=assemblyscript&logoColor=white" alt="ASM" />
  <img src="https://img.shields.io/badge/Verilog-2C2D72?style=flat-square&logo=fpga&logoColor=white" alt="Verilog" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
</p>

### Disassembly, Dynamic Analysis & Emulation
<p align="center">
  <img src="https://img.shields.io/badge/IDA_Pro_9.x-6B21A8?style=flat-square&logo=hexo&logoColor=white" alt="IDA Pro" />
  <img src="https://img.shields.io/badge/Ghidra-000000?style=flat-square&logo=nsa&logoColor=white" alt="Ghidra" />
  <img src="https://img.shields.io/badge/x64dbg-2B5797?style=flat-square&logo=windows&logoColor=white" alt="x64dbg" />
  <img src="https://img.shields.io/badge/WinDbg-0078D4?style=flat-square&logo=windows&logoColor=white" alt="WinDbg" />
  <img src="https://img.shields.io/badge/HyperDbg-107C41?style=flat-square&logo=hyper&logoColor=white" alt="HyperDbg" />
  <img src="https://img.shields.io/badge/Unicorn_Engine-D22630?style=flat-square&logo=cpu&logoColor=white" alt="Unicorn" />
  <img src="https://img.shields.io/badge/Frida-E4405F?style=flat-square&logo=frida&logoColor=white" alt="Frida" />
  <img src="https://img.shields.io/badge/PCILeech_DMA-232F3E?style=flat-square&logo=pci&logoColor=white" alt="PCILeech" />
</p>

### Offensive Security & Agent Ecosystems
<p align="center">
  <img src="https://img.shields.io/badge/Autonomous_Swarms-7C3AED?style=flat-square&logo=openai&logoColor=white" alt="Swarms" />
  <img src="https://img.shields.io/badge/Model_Context_Protocol-000000?style=flat-square&logo=anthropic&logoColor=white" alt="MCP" />
  <img src="https://img.shields.io/badge/Kernel_Exploitation-E11D48?style=flat-square&logo=gnubash&logoColor=white" alt="Kernel" />
  <img src="https://img.shields.io/badge/BYOVD_%2F_DKOM-B91C1C?style=flat-square&logo=hackthebox&logoColor=white" alt="BYOVD" />
  <img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white" alt="Burp" />
  <img src="https://img.shields.io/badge/Metasploit-18539E?style=flat-square&logo=metasploit&logoColor=white" alt="Metasploit" />
</p>

</div>

---

## 📊 Telemetry & Activity

<div align="center">

<table border="0">
  <tr>
    <td align="center" width="50%">
      <img src="https://github-readme-stats.vercel.app/api?username=NetVar1337&show_icons=true&theme=radical&hide_border=true&count_private=true&include_all_commits=true&title_color=A78BFA&text_color=E2E8F0&icon_color=7C3AED&bg_color=0D1117" alt="GitHub Stats" />
    </td>
    <td align="center" width="50%">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=NetVar1337&layout=compact&theme=radical&hide_border=true&title_color=A78BFA&text_color=E2E8F0&bg_color=0D1117" alt="Top Languages" />
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="https://git.io/streak-stats">
        <img src="https://streak-stats.demolab.com/?user=NetVar1337&theme=radical&hide_border=true&stroke=7C3AED&background=0D1117&ring=A78BFA&fire=7C3AED&currStreakLabel=A78BFA" alt="GitHub Streak" />
      </a>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NetVar1337/NetVar1337/output/github-contribution-grid-snake-dark.svg" />
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NetVar1337/NetVar1337/output/github-contribution-grid-snake.svg" />
        <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/NetVar1337/NetVar1337/output/github-contribution-grid-snake.svg" />
      </picture>
    </td>
  </tr>
</table>

</div>

---

## 🎯 Current Operational Focus

- 🛡️ **Kernel & Hypervisor Research:** Stealth Intel VT-x virtualization, EPT hook masking, and Unicorn-based Windows driver execution harnesses.
- 🎯 **Autonomous Offensive Swarms:** Multi-agent coordination, subagent reasoning topologies, and 0-day vulnerability research automation @ [PurpleAILAB](https://github.com/PurpleAILAB).
- ⚡ **Game Security & Anti-Cheat:** Kernel stack-walk evasion, memory integrity research, and DMA hardware-level attack mitigation analysis.
- 📦 **Token & Context Optimization:** High-efficiency CLI shims, MCP tooling ecosystems, and low-latency system-level developer utilities.

---

<div align="center">

```c
/* Stay sharp. Stay low-level. */
while (true) {
    if (understand_the_machine()) {
        control_the_machine();
    }
}
```

</div>