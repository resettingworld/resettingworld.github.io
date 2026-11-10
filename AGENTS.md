# AGENTS.md — `resettingworld.com` Web Portal

Instructions for AI coding agents editing the **Resetting World** static website (`web/`).

## Invariants
1. **100% Offline-Capable Core**: No analytics, no tracking, no external backend APIs required to browse the site or marketplace (`static/catalog.json` + `static/i18n.json`).
2. **Trilingual Key Parity**: Every UI string MUST use `data-i18n` and maintain identical keys across `ca`, `es`, and `en` in `static/i18n.json`. Validate JSON syntax and key parity after every edit.
3. **Separate Marketplace Page**: Keep the landing page (`index.html`) focused on the 5 manifesto/architecture sections and keep the full interactive RAG catalog on `marketplace.html`.
4. **Canonical Visual Branding**: Preserve `favicon.ico`, `static/favicon-*.png`, `static/logo.png`, and the Collage Punk / Cyber-Resilience palette (`#090a0f`, `#00f0ff`, `#ff007f`, `#ffea00`).
5. **Never Commit `packs/` Symlink/Binaries**: Keep large `.zip` capsules in `resettingworld/catalogo` Releases, not inside the web git tree.
