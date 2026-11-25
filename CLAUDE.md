# CLAUDE.md

Read `docs/PROJECT_BRIEF.md` first. It explains what this project is and why. Then read `ROADMAP.md`: it says where the project stands and what to do next. This file explains how to work on it.

## Who you're working with

Eyal is not a programmer and is not trying to become one. He's building this with you to (1) get better at Catan and (2) learn the concepts the project requires: probability, simulation, data analysis, and eventually machine learning. He directs; you build.

That means:
- **Explain as you go.** After each task, summarize in plain language what you built, why, and which concept it used. Short, no jargon without a one-line definition.
- **Teach the concept, not the syntax.** He doesn't need to understand every line of code. He does need to understand what each piece does and whether its output is right.
- **Ask before big decisions** (architecture, libraries, data formats, anything hard to undo). Give 2-3 options with a recommendation. Small decisions: make them and mention them.
- **Use plan mode** for any task touching more than a couple of files. Show the plan before building.
- **Keep it simple.** The simplest thing that works, then improve. No premature abstractions.
- No em dashes in anything you write for him.

## The non-negotiable rule: evidence

Every recommendation the tool gives must show its basis: the math, the dataset query, or the simulation, plus the sample size. If evidence is thin (small sample, wide uncertainty), the output must say so. Never present a guess as a finding.

When analyzing data, actively watch for and flag:
- Small samples after slicing (seat x archetype x board condition shrinks fast)
- Correlation vs causation (e.g. ore/wheat winners may also have had better numbers)
- Reverse causation (e.g. cards played at the very end of a game are mostly the winner's last move, so "late Monopoly wins" says little about when to play it)
- Luck: judge decisions across many games or simulations, never by one outcome
- Unknown player skill in the dataset (results reflect average online players, not pros)
- Bots are not humans: simulated games show what works against bots, not what wins online

## What's in scope

- **Game:** classic base Catan, 4 players, random board setup the way Colonist.io does it. Read the exact settings (points to win, robber rules) from the data and keep only matching games.
- **Use mode:** study first. Eyal enters a board, studies it with the tool, and learns to read boards himself. Live use during a game comes later, and the board entry method is still open (fast manual entry or screenshot).
- **Ranked games:** only if Colonist's rules allow outside tools. See `docs/DECISIONS.md`.

## Stack (confirmed with Eyal, 2026-11-25)

- **Python 3.12** for everything core: board model, data processing, analysis, simulation, ML later
- **venv + pip** for the environment (Python's built-in tools; `.venv/` is never committed)
- **pandas / numpy** for data; **Parquet** (via pyarrow) for processed data
- **pytest** for tests
- **Catanatron** for full-game simulation when needed. Install it from GitHub (github.com/bcollazo/catanatron), not pip: the pip release is from 2022, the GitHub project is still updated
- **Streamlit** for the v1 interface (fast, local, good for interactive analysis). A proper web version for his personal website can come later.
- **scikit-learn or LightGBM** later, for the win probability model

## Setup and everyday commands

Run these from the project folder in PowerShell. The README has the first-time setup. Call the environment's Python directly instead of activating it: Eyal's PowerShell blocks scripts, so `Activate.ps1` fails, and these work without it.

- Run the tests: `.venv\Scripts\python -m pytest`
- Open the app: `.venv\Scripts\python -m streamlit run app/main.py`
- Install a new library: add it to `requirements.txt`, then `.venv\Scripts\python -m pip install -r requirements.txt`

## Data

- **Main source:** a dataset of 43,947 4-player Colonist.io games (JSON, ~6.9GB uncompressed), originally at github.com/Catan-data/dataset. Research and educational use only; cite as the dataset asks (see README).
- **Status (2026-11-25): the download is offline.** The repo, its release page and the file all return "not found". A copy of its README (github.com/OrgadYron/catan_43k_games_dataset) still points to the dead link. Finding the data, or other human game data, is a roadmap task. Never download data from an unofficial mirror without checking with Eyal first.
- **Fallbacks:** simulated games (Catanatron), Catan Trainer's aggregate stats (github.com/dglass211/catan-placement-data, CC BY 4.0, credit "Catan Trainer"), and Eyal's own Colonist games later.
- Raw data goes in `data/raw/`, processed data in `data/processed/`. **Never commit data to git**; `data/` is in `.gitignore`.
- Document the game file format in `docs/DATA_SCHEMA.md` as you learn it.
- Process once into tables; don't re-parse 44k JSON files on every run.

## Structure

```
catan-strategizer/
  CLAUDE.md
  ROADMAP.md             # where we are, what's next (update every session)
  README.md              # what it is, setup, how to run, data citation
  docs/
    PROJECT_BRIEF.md
    DATA_SCHEMA.md       # what's in a game file
    FINDINGS.md          # every Lab result: question, method, answer, sample size
    LEARNING_LOG.md      # concepts Eyal learned, in his words or yours
    DECISIONS.md         # key decisions and why
  src/catan/             # the project's own code, imported as `catan`
    board/               # hex grid, corners, edges, ports, production math
    data/                # loading and processing the dataset (Phase 2)
    analysis/            # Lab queries, archetype classification (Phase 3)
    strategizer/         # draft simulation, recommendations, explanations (Phase 4)
  app/                   # Streamlit interface
  tests/
  data/                  # gitignored
```

Folders for later phases are created when their phase starts, not before.

## Correctness checks

The board model is the foundation; test it hard:
- 19 hexes, 54 corners, 72 edges
- Each corner touches 1 to 3 hexes; adjacency is symmetric
- Distance rule enforced
- Pip math matches the known table (2/12 = 1 ... 6/8 = 5, total 58 pips on a standard board with desert)
- The dataset's coordinate system maps correctly onto our board model (verify with several real games before trusting any analysis)

## Workflow

- Work in small steps; each ends with something runnable or a question answered.
- Commit after each working step with a clear message.
- Log every Lab result in `docs/FINDINGS.md`.
- Log key decisions in `docs/DECISIONS.md`.
- At the end of each session, update `ROADMAP.md` (status, next action) and `docs/LEARNING_LOG.md` (concepts that came up).
- Phases and milestones live in `ROADMAP.md`.

## Out of scope for v1

Live tracking, player profiling, 3-player, expansions, the ML model, post-game review. Don't build ahead.
