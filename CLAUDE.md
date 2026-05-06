# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal navigation and tools website (煜的工具站) — a collection of mini-games, learning tools, and utility links served by a Node.js/Express backend. All UI text is in Chinese (zh-CN).

## Commands

```bash
npm start          # Start server on port 8000
npm run dev        # Start with nodemon (auto-reload)
npm install        # Install dependencies
```

Access: `http://localhost:8000/frontend/`

## Architecture

**Single-server monolith** — Express serves static files and two JSON API endpoints.

### Backend (`backend/server.js`)
- Express server on port 8000, binds `0.0.0.0`
- Serves `frontend/` as static assets under `/frontend`
- API endpoints:
  - `GET /api/idiom-stories` — reads `中华成语/Idiom stories1.json` (fallback: `Idiom stories.json`)
  - `GET /api/chengyu-data` — reads `中华成语/chengyu_all_simple.json`
- Root `/` redirects to `/frontend/`
- Each `.html` file under `/frontend/` is individually routable via `/frontend/:filename`

### Frontend (`frontend/`)
- No build step. Plain HTML + vanilla JS + Bootstrap 5.3 + Font Awesome 6.
- **PWA enabled**: `sw.js` (service worker) with static/dynamic caching, `manifest.json` for installability.
- **Entry point**: `index.html` — the navigation hub page.
- **Page registry**: `index.data.js` — defines all tool/game/learning links as data arrays (`tools`, `funGames`, `learning`, etc.).
- **JS modules** (`frontend/js/`):
  - `api.service.js` — generic API client class with auth token management (methods exist for auth/file/music/search/stats endpoints, but backend only implements idiom endpoints).
  - `search.js` — multi-engine search (Baidu/Bing/Google/site).
  - `device-adapter.js` — responsive device adaptation.
  - `theme.js` — dark theme management.
- **CSS**: Single `main.css` with dark theme using CSS custom properties (`--bg-color: #050505`, etc.).
- Individual `.html` files are self-contained pages (games, learning tools, etc.) — each is a standalone mini-app.

### Data (`中华成语/`)
- JSON data files for the idiom learning feature.
- `enrich_chengyu_*.py` — Python scripts (batch crawl, 100 idioms each) that populated the data. These are one-time scripts, not part of the running app.
- `requirements.txt` at project root lists Flask dependencies but the server is Node.js; Python is only for the crawler scripts.

### Sub-projects
- `水井棋/` — Well Chess game (separate project with its own `server.js` and `package.json`).
- `frontend/现代汉语词典/` — Chinese dictionary viewer (static HTML + MDict support).
- `frontend/um-web.legacy.v1.10.8/` — Music decoder tool (third-party bundle).

## Key Conventions

- All files and UI text are in Chinese.
- Frontend pages are standalone HTML files — no shared component system, no framework.
- New tools/games are added by: (1) creating a new `.html` file in `frontend/`, (2) adding an entry to the appropriate array in `index.data.js`.
- The `api.service.js` client defines many API methods that don't have corresponding backend routes yet — these are forward-looking stubs.
- CDN dependencies (Bootstrap, Font Awesome) are loaded externally, not bundled.
