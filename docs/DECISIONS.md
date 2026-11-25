# Decisions

Key decisions and why. Newest at the bottom. If a decision changes, add a new entry instead of editing the old one.

---

### 2026-11-25: Stack
**Decision:** Python 3.12, pandas and numpy, Parquet files, pytest, Streamlit for the interface, Catanatron for simulation when needed.
**Why:** Python is the standard for data analysis, simulation and machine learning, so one language covers every phase. Streamlit turns a Python script into a browser page with no web development. Proposed in CLAUDE.md, confirmed by Eyal.

### 2026-11-25: Environment: venv + pip
**Decision:** Python's built-in `venv` and `pip`, with libraries listed in `requirements.txt`. Commands call `.venv\Scripts\python` directly instead of "activating" the environment.
**Options considered:** venv + pip (built in, nothing new to install), uv (faster, one more tool), conda (heavy, made for scientific setups).
**Why:** simplest option that works. Calling the environment's Python directly avoids a Windows PowerShell setting that blocks the activation script.

### 2026-11-25: Code layout: one `catan` package
**Decision:** the project's code lives in `src/catan/` (board, data, analysis, strategizer) and is installed into the environment in "editable" mode (the `-e .` line in `requirements.txt`).
**Why:** the tests and the Streamlit app can both write `from catan.board import ...` without path tricks, and edits take effect without reinstalling. A small change from CLAUDE.md's suggested `src/board/` layout: plain names like `data` and `analysis` could clash with other libraries.

### 2026-11-25: Where things are stored
**Decision:** code and docs in git, pushed to GitHub. Game data only on Eyal's computer (`data/raw/`, `data/processed/`), never committed. Processed tables are rebuilt by scripts that are in git.
**Why:** GitHub refuses files over 100 MB, the dataset is research and educational use only and isn't ours to republish, and keeping the scripts means the tables can always be rebuilt.

### 2026-11-25: GitHub repo is public
**Decision:** public repo, `catan-strategizer`.
**Why:** a portfolio piece, and it holds no secrets or data. Commits use Eyal's GitHub "noreply" address (same as the stock project), so his email isn't published.

### 2026-11-25: Board model before data
**Decision:** Phase 1 is the board model and probability math. Getting the dataset, documenting it, and the seat question move to Phase 2.
**Why:** the dataset download is offline. The board model needs no data, and everything later depends on it.

### 2026-11-25: Data: find everything real, simulate the rest
**Decision:** hunt for the 43,947-game dataset and any other real game data first. If there isn't enough, use simulated games (Catanatron) and probability math, and say clearly in every result what bots can't tell us about human play. Don't download data from unofficial mirrors without checking with Eyal.
**Why:** Eyal's call: "whatever we can find is good, whatever not, then we'll have to use bots." Unknown mirrors could serve altered or harmful files.

### 2026-11-25: Other tools are a benchmark, not a reason to stop
**Decision:** compare our results with existing tools (Catan Trainer, Catanatron's bots) instead of avoiding the overlap.
**Why:** the project is for learning. Existing tools give a standard to reach and a way to check our numbers.

### 2026-11-25: Game settings
**Decision:** classic base game, 4 players, random board setup the way Colonist.io does it. Exact settings (points to win, robber rules) are read from the data, and only matching games are used.
**Why:** that's what Eyal plays.

### 2026-11-25: Study mode first, live use later
**Decision:** v1 is for studying a board before or after a game. Live use during a game (fast manual entry or reading a screenshot) comes after v1.
**Why:** Eyal's priority is learning to read boards himself. Fast board entry is a separate, harder problem.

### 2026-11-25: Using the tool in ranked games
**What Colonist's rules say** (Community Guidelines, colonist.io/community-guidelines, updated 2026-09-01, read 2026-11-25): under "Don't cheat": *"Don't use extensions or any third-party tool that plays for you or shows hidden information."* The penalty for cheating can be an immediate ban. The rules don't treat ranked, casual and private games differently, and they don't mention a separate app that only uses what's visible on the board.
**Separately, the Terms of Use** (colonist.io/terms, updated 2026-10-06) ban scraping the site, including game replays and statistics, and using its internal data or APIs outside the normal interface.
**Decision:**
- Study mode (before or after games) is clearly fine: the tool doesn't play and only uses the visible board.
- Live opening advice during a game: start with casual and private games. Before using it in ranked, Eyal asks Colonist support. Not breaking rules matters more to him than using it in ranked.
- Later modules that read game data from Colonist itself (live tracker, importing games for post-game review) must be checked against the Terms' scraping and API rules before they're built.
**Why:** the rule as written targets tools that play for you or reveal hidden information, which this isn't. But the rules don't address it directly, so we don't assume.

### 2026-11-25: Board model: our own, built from the shape
**Decision:** we build the board ourselves from its geometry (`src/catan/board/grid.py`) and number everything our way: hexes 0 to 18 row by row, corners 0 to 53 and edges 0 to 71 top to bottom, left to right. The dataset's numbering and Catanatron's get small translators later, checked on real games.
**Options considered:** our own model (chosen), reusing Catanatron's board, copying the dataset's (x, y, z) corner format.
**Why:** easiest to understand and test, and it doesn't depend on a simulator's internals or on a data format we can't see yet. Eyal's choice, 2026-11-25.
