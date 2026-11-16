# Free AI Hub

**Live demo:** https://waleriapolanska.github.io/free-ai-hub/

A catalog of free and nearly free AI services, open-source patches and AI skills, with data that refreshes itself every 3 days.

## Features
- **AI tab** - 30+ AI APIs and agents. Each one shows its status, what it gives, what it can do and what signup needs (card, phone, KYC). You can filter by type and by "no card needed".
- **Offers tab** - cloud and VPS credits, proxies, SMS numbers and search APIs for agents.
- **Patches tab** - free open-source tools from GitHub that connect free models to Claude Code, VS Code and the terminal.
- **Skills tabs** - free and paid skills on separate tabs, color-coded by purpose (text, code, images, docs, research, data, media).
- **Roadmap and legend** - what the colors and statuses mean, and plans for the project.
- **Auto-refresh** - a scheduled AI agent re-checks the sources every 3 days and rewrites `data.js`.

## Tech
- Vanilla HTML, CSS and JS, with no build step and no dependencies.
- Data is kept apart from the UI: `data.js` holds it, `index.html` renders it.
- Search, filters and a responsive grid that works at phone width.
- XSS-safe rendering, because every value is escaped.

## Run locally
```bash
python3 -m http.server 8765
```
Then open http://localhost:8765

Offer data is based on [vldtech.si/offers](https://vldtech.si/offers/).
