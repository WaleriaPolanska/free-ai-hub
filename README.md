# Free AI Hub

**Live demo:** https://waleriapolanska.github.io/free-ai-hub/

A catalog of free and nearly free AI services, open-source patches and AI skills, with data that refreshes itself every 3 days.

## Features
- **Roadmap & legend** - opens first and explains the color legend, statuses and plans.
- **AI** - 30+ AI APIs and agents, split into Free and Paid sub-tabs. Each card shows status, what it gives, what it can do and what signup needs. You can filter by "no card needed".
- **Skills** - one tab with Free and Paid sub-tabs, color-coded by purpose (text, code, images, docs, research, data, media).
- **Patches** - free open-source tools from GitHub that connect free models to Claude Code, VS Code and the terminal.
- **Cloud & tools** - non-AI deals: cloud and VPS credits, proxies, SMS numbers, search APIs for agents.
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
