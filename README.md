# Resetting World Portal (`resettingworld.com`)

> **Rethinking technology. Rebuilding the future.**  
> Official trilingual website (`ca`, `es`, `en`) and free RAG Marketplace frontend for **Resetting World**.

---

## 🌐 Pages & Architecture

- [`index.html`](./index.html): Five-section portal landing page (**Home**, **The 3 Pillars**, **Roadmap**, **Experiments**, **Join Us**) plus Marketplace CTA.
- [`marketplace.html`](./marketplace.html): Standalone searchable & filterable RAG Marketplace covering all 50 knowledge capsules hosted in [`resettingworld/catalogo`](https://github.com/resettingworld/catalogo).
- [`static/i18n.json`](./static/i18n.json): Trilingual dictionary (`ca`, `es`, `en`) with 100% key parity.
- [`static/catalog.json`](./static/catalog.json): Generated marketplace manifest linking local `.zip` packs and GitHub Release downloads.
- [`build_data.py`](./build_data.py) & [`server.py`](./server.py): Local offline catalog generator and static HTTP server (port `8085`).

## 🚀 Run Locally

```bash
python3 build_data.py   # Rebuild static/catalog.json from ../data/packs/*.zip
python3 server.py       # Serves http://localhost:8085
```
