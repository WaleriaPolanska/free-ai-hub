# Free AI Hub

**Live demo:** https://waleriapolanska.github.io/free-ai-hub/

A catalog of free and nearly free AI services, open-source patches and AI skills, with data that refreshes itself every 3 days.

## Features
- **Roadmap & legend** - opens first and explains the color legend, statuses and plans.
- **AI** - 30+ AI APIs and agents, split into Free and Paid sub-tabs. Each card shows status, what it gives, what it can do and what signup needs. You can filter by "no card needed".
- **Skills** - 70 skills (52 free from real GitHub repos, 18 paid services) in color-coded folders. Notebook-style bookmarks on the left flip the page with a 3D page-turn.
- **Patches** - 54 free open-source tools in 8 folders: routers and proxies, CLI agents, IDE extensions, local models, chat UIs, MCP servers, usage and hooks, free API lists.
- Every GitHub card shows live ★ stars and last update. Each card also says which AIs make it free and which make it paid.
- **Cloud & tools** - non-AI deals: cloud and VPS credits, proxies, SMS numbers, search APIs for agents.
- **Auto-refresh** - a GitHub Actions workflow runs every 3 days, re-checks every link, refreshes GitHub stars and activity through the GraphQL API, and stamps each card with its check date. Dead links are flagged on the site.

## Tech
- Vanilla HTML, CSS and JS, with no build step and no dependencies.
- Data is kept apart from the UI: `data.json` holds it, `index.html` fetches and renders it.
- `scripts/check_links.py` - concurrent link checker on the Python standard library. It tells bot protection (403/429) apart from pages that are really gone (404/410, DNS errors).
- `.github/workflows/refresh.yml` - scheduled CI job that commits refreshed data back to the repo.
- Search, filters and a responsive grid that works at phone width.
- XSS-safe rendering, because every value is escaped.

## Run locally
```bash
python3 -m http.server 8765
```
Then open http://localhost:8765

Offer data is based on [vldtech.si/offers](https://vldtech.si/offers/).
