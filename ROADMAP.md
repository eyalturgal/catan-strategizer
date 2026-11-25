# Roadmap and Progress

This file is the source of truth for where the project stands. Update it at the end of every work session.

---

## Current status

- **Current phase:** Phase 1 (Board model and probability), step 1 of 5 done. Plan approved by Eyal: grid, production math, harbors and distance rule, random boards, board view in the app
- **Next action:** Claude: step 2 (what's on the board and what each spot produces). Alongside: the data hunt (Claude drafts the question about the missing dataset, Eyal posts it) and Eyal checks 5 to 10 Colonist boards for harbor positions and touching red numbers
- **Blocked on:** nothing for Phase 1. The dataset download is still offline (see Phase 2)
- **Last updated:** 2026-11-25

### Done so far
- [x] Project idea written up in PROJECT_BRIEF.md and CLAUDE.md
- [x] Brief reviewed. Found: the dataset link is dead, Catanatron should come from GitHub, a similar tool exists (Catan Trainer)
- [x] Decisions made: study mode first, classic Colonist settings, board model before data (see `docs/DECISIONS.md`)
- [x] Project folder, docs, Python environment, first test, first commit
- [x] Project on GitHub: https://github.com/eyalturgal/catan-strategizer (public). Eyal created the repo and signed this computer in to GitHub

---

## Phases

Each phase ends with something working and visible. Don't start the next phase until the current one's "done when" is true. Exception: the data hunt (top of Phase 2) can run during Phase 1, because it's mostly waiting on other people.

### Phase 0: Setup and foundations
- [x] Project folder next to the stock project: `AI Journey\Claude Code\catan-strategizer`
- [x] CLAUDE.md, PROJECT_BRIEF.md, ROADMAP.md, README.md
- [x] Docs: DATA_SCHEMA, FINDINGS, LEARNING_LOG, DECISIONS
- [x] Stack confirmed: Python 3.12, venv + pip, pandas, Parquet, pytest, Streamlit
- [x] Python environment set up, first test passes (dice odds)
- [x] Hello page opens in the browser (command in the README)
- [x] Git set up with a first commit
- [x] GitHub repo created by Eyal, first push done (2026-11-25)
- [x] Check Colonist's rules on outside tools in ranked games (result in `docs/DECISIONS.md`)

**Eyal's steps to create the GitHub repo:**
1. On github.com, click the **+** at the top right, then **New repository**.
2. Name it `catan-strategizer`. Choose **Public**.
3. Leave everything else empty: no README, no .gitignore, no license (the project already has its own files, and GitHub's would clash).
4. Click **Create repository** and tell Claude it's done.

**Done when:** the project is on GitHub, `pytest` passes, and the hello page opens in the browser.

### Phase 1: Board model and probability (no data needed)
- [x] Dice odds by counting all 36 rolls (started in Phase 0 as the first test)
- [x] Hex grid in code: 19 hexes, 54 corners, 72 edges, and which ones touch (`src/catan/board/grid.py`)
- [x] Tests: counts, each corner touches 1 to 3 hexes, adjacency works both ways (15 tests in `tests/test_grid.py`)
- [ ] Distance rule (which corners block which)
- [ ] Ports: the 9 harbors and the corners that use them
- [ ] Production per corner: pips and resources, total 58 pips on a standard board
- [ ] Board scarcity: pips per resource on a given board
- [ ] Random board generator that follows Colonist's setup rules (check the 6 and 8 rule)
- [ ] Research Colonist's board rules: do harbors stay put, do red numbers ever touch? (Eyal looks at 5 to 10 boards; the data confirms later)
- [ ] Board view in the app: draw a board, show production per spot, so Eyal can check a few by hand

**Done when:** tests confirm 54 corners, 72 edges and correct adjacency; Eyal can open a random board in the app and the production numbers match what he counts himself.

### Phase 2: Real game data (find it, understand it)
- [ ] Hunt for the 43,947-game dataset. Claude drafts a question for the copy repo (github.com/OrgadYron/catan_43k_games_dataset), Eyal posts it. Search other places too
- [ ] List other sources of real games: Catan Trainer's stats, Eyal's own Colonist games, anything else that turns up
- [ ] If no real game data: plan simulated data with Catanatron, and write down what bots can't tell us
- [ ] Download and extract into `data/raw/` (never committed)
- [ ] Open several real games and document the format in `docs/DATA_SCHEMA.md`
- [ ] Map the dataset's board coordinates onto our board model, checked on several real games
- [ ] Keep only games with classic settings (read from each game's settings)
- [ ] First Lab question: win rate by seat, with sample size and uncertainty range. Compare with the 24.9% to 25.2% someone else reported

**Done when:** data is on disk (or a fallback is chosen), its format is documented, coordinates are verified, and the seat question is answered in `docs/FINDINGS.md`.

### Phase 3: Data layer
- [ ] Process every game once into Parquet tables: board features, seat, opening spots, what each player built, who won
- [ ] Sanity checks: game counts, one winner per game, 4 players per game, totals that add up

**Done when:** one command builds the tables, and loading them takes seconds, not minutes.

### Phase 4: Strategy Library and Lab
- [ ] Archetypes defined from what players actually did
- [ ] First 5 Lab questions answered, each with sample size and uncertainty
- [ ] Compare our numbers with Catan Trainer's published stats

**Done when:** the Strategy Library has archetypes with evidence, and 5 Lab results are logged in `docs/FINDINGS.md`.

### Phase 5: Board Analyzer and Opening Strategizer (v1)
- [ ] Board entry in the app for study mode: click a hex, pick its resource and number
- [ ] Board Analyzer: what's scarce, what's strong, which ports matter, similar boards in the data
- [ ] Draft simulation (1-2-3-4-4-3-2-1) with opponents modeled on real players
- [ ] Ranked settlement pairs, archetype, win condition, early/mid/end game goals, each with its evidence

**Done when:** Eyal enters a board and seat and gets a ranked settlement pair and a plan, each part explained with evidence and its sample size.

### v1 test: real use
- [ ] Used in at least 3 real games (study mode: before or after the game)
- [ ] Eyal understood why it recommended what it did

**Target:** late December 2026.

---

## Open questions
- **Board entry during a live game:** fast manual entry or reading a screenshot? Decide after v1 study mode works.
- **Exact Colonist settings** (points to win, robber rules): read them from the data in Phase 2.

## Later (not v1)
Live board entry, web version for the personal site, win probability model (machine learning), re-planner, post-game review, live tracker (casual and private games only), 3-player.
