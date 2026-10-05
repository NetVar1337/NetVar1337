# Markus Halvorsen

Independent research toward **game-security analyst** work. I do not work for a studio or an anti-cheat vendor.

The loop I practice: name the cheat class, measure a behavior, cohort it, write the query, and say what the evidence does not prove.

## Work to judge

| Repo | What a reviewer can check |
|:---|:---|
| [apex-anticheat-lab](https://github.com/NetVar1337/apex-anticheat-lab) | Clone and run `detections/run_fixture.py`. Synthetic fixture, per-cohort baselines, explainable scores. The investigation packet includes the case where a high-skill human outranks a recoil script on the composite. |
| [cheat-intel](https://github.com/NetVar1337/cheat-intel) | How to grade a community claim. The landscape note marks its own weak sources. |
| [account-security](https://github.com/NetVar1337/account-security) | Account-takeover and session-abuse signals, as a graph rather than a login rate-limit. |

## How I would work a report

1. **Taxonomy first.** Aimbot, triggerbot, ESP, DMA, macro, spoofing, boosting. Name the class, then the layer that can even see it.
2. **Behaviour over binaries.** A signature dies on the next build. Aim kinematics, input timing, and account behavior survive the rewrite.
3. **Cohort before score.** Mouse versus controller, rank, weapon. A pooled baseline is a false-positive machine.
4. **Explainable review queue.** No auto-ban on one feature. Every flag carries the numbers that produced it.
5. **Measure enforcement.** Match infection rate before and after, not the raw ban count. Replacement accounts fake a win.

## What this profile is not

- Not employment, and not a claim that any of this runs on a live game.
- The lab fixture is synthetic. The investigation packet says so in the title.
- YARA in the lab is a heuristic sketch. It is not an operational ruleset.
- Kernel and hypervisor projects are not the work I want this profile judged on.

I also contribute to [Decepticon](https://github.com/BitterSecurity/Decepticon), an authorized red-team agent. That is a different job. Do not read it as anti-cheat employment.

Open to game-security analyst and detection roles.
