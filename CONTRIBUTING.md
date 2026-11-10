# Contributing to Resetting World

> **Rethinking technology. Rebuilding the future.**  
> Resetting World is **Community Driven** and built through **Open Collaboration**. Developers, systems architects, researchers, librarians, radio amateurs, and makers are all invited to participate.

---

## 🌍 Organization Repositories

| Repository | Focus | Where to Contribute |
|---|---|---|
| **Core Monorepo (`smart-local`)** | Full Python/Rust RAG runtime, scrapers, Mastra UI & `resettingworld.com` portal | Runtime optimizations, portal translations (CA/ES/EN), tests |
| **[`rw-knowledge`](https://github.com/resettingworld/rw-knowledge)** | Knowledge Engine, capsule `.zip`/`.gpk` tooling & public-domain curation | New technical book sources, front-matter parsers, ARM64 optimizations |
| **[`rw-protocol`](https://github.com/resettingworld/rw-protocol)** | Distributed DTN/mesh protocol & pluggable peer-to-peer apps | RFC proposals, LoRa/BLE/Wi-Fi Direct transport drivers, pluggable apps |
| **[`rw-hardware`](https://github.com/resettingworld/rw-hardware)** | Open hardware kits, solar/LiFePO4 schematics & 3D IP65 enclosures | BOM verification, STL/STEP enclosures, power draw telemetry |

---

## 🛠️ Development Workflow

1. **Fork & Branch**: Fork the target repository and create a descriptive branch:
   - `feat/<short-name>`
   - `fix/<short-name>`
   - `docs/<short-name>`
   - `rfc/<number>-<topic>`
2. **Core Non-Negotiable Invariants**:
   - **100% Offline-First**: Runtime paths (`serve`, `query`, `triage`, `mesh`) must NEVER require external internet access or cloud API keys.
   - **No Secrets or Telemetry**: Zero tracking, zero analytics, zero hardcoded credentials.
   - **Knowledge Capsule Standard (`<= 50` books)**: Every RAG capsule must contain at most 50 books, exclude fiction, and include `metadata.json`, `manifest.json`, and Collage Punk `catalog.json`.
   - **Safety First**: No weapons instructions; hardware guides must include over-current fusing and BMS protection.
3. **Run Checks Before Opening a PR**:
   ```bash
   # Python RAG Engine & Pipeline tests
   uv run pytest

   # Rust SmartEngine tests & build
   cd rust-engine && cargo test && cargo build --release
   ```
4. **Pull Request**: Fill out `.github/PULL_REQUEST_TEMPLATE.md` clearly explaining the change, affected platforms (x86_64, ARM64 / Raspberry Pi 5, Termux), and verification steps.

---

## 🗣️ Multilingual Documentation Policy
Human-facing web content and high-level guides support **English (`en`)**, **Català (`ca`)**, and **Español (`es`)**. Code comments, schemas, and agent instructions (`AGENTS.md`) should remain concise and consistent.
