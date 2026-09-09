# STATUS.md — P5R Save Editor (Change of Heart)

> Human-readable current state. Synced from state.json on every exit.
> Updated: 2026-09-09 UTC

## Current State
- **Phase:** implementation
- **Gate:** ready
- **Mode:** single-agent

## Last Completed
- 2026-09-09: Vercel hosted web mode added — upload/download flow for `DATA.DAT`/`DATA.BIN`, serverless entrypoint (`api/index.py`), `vercel.json`, deploy-mode Origin allowance, and disabled local-only features (Steam auto-discovery, path loads, backups/restores, P5R.exe process check). Targeted hardening + heartbeat tests pass (51/51); lint:context OK.
- 2026-08-24 (later): FIXED bond-points wipe bug (zamasu2020, r/Persona5Royale) — social-stat edits were resetting ALL confidants' accumulated bond points to rank thresholds via the full-confidant re-save loop; same-rank rewrites now preserve exact points, rank-ups preserve carryover (max logic), social stats same treatment. 4 regression tests (174/174). EXE rebuilt.
- 2026-08-24 (later): UI Atlus-fidelity pass R1 — rainbow progress → flat yellow angular, 27 green literals → P5 yellow, hex IDs removed from persona cards, star ladder → horizontal yellow meter, sidebar emoji → flat SVG icons, subtitle weight demoted. 10/10 captures re-baselined, 170/170 tests. R2 candidates in memory/2026-08-24-ui-atlas-pass.md.
- 2026-08-24 (later): UI-liveness watchdog shipped — frontend pings /api/ui-heartbeat; if the native WebView2 window never checks in within 30s (broken runtime = Gruphius's silent-dead-buttons symptom), main.py auto-opens the editor in the system browser and keeps serving. /api/heartbeat-status diagnostics endpoint added. 170/170 tests. EXE rebuilt + live-window smoke test PASSED (heartbeat ever_seen=true).

## Next Action
- Deploy hosted upload/download web mode to Vercel.

## Blockers
- None.

## Recent Session
- 2026-09-09: Vercel hosted web mode (memory/2026-09-09-vercel-web-mode.md)
- 2026-08-24: UI-liveness watchdog + v1.1.1 release
- 2026-08-21: inventory UX pass R1-R9 (memory/2026-08-21-inventory-ux-pass.md)

## Pinned SHAs
- None (no upstream dependencies)

## Build
- Latest desktop: `dist/P5R_Save_Editor.exe` (47.9 MB, rebuilt 2026-08-24 ET — watchdog + UI fidelity pass + bond-points fix D016; sha256 prefix 3d34cc50ddf3ff1b; v1.1.1 release assets refreshed with this build)
- Web: Vercel upload/download mode (`api/index.py`, `vercel.json`)
- PyInstaller 6.22.0 / Python 3.14.6
- GitHub: v1.1.1 Released
