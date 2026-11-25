# Catan Strategizer

A personal learning project: a tool that reads a classic 4-player Catan board, explains what kind of board it is, recommends opening settlements and a strategy for a given seat, and shows the evidence behind every recommendation (probability math, real game data, and simulation).

It's a teacher, not an autopilot. See `docs/PROJECT_BRIEF.md` for the full idea and `ROADMAP.md` for where it stands.

## How it runs

Everything runs on your own computer. The interface is a Streamlit app: one command opens it as a page in your browser. There's no hosting for v1.

## First-time setup (Windows, PowerShell)

From the project folder:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

The first line makes a private Python environment for this project in `.venv/` (like `node_modules`, it's never committed). The second installs the libraries listed in `requirements.txt` (like `package.json`), plus the project's own code.

## Everyday commands

Run the tests:

```powershell
.venv\Scripts\python -m pytest
```

Open the app (it opens in your browser; press Ctrl+C in the terminal to stop it):

```powershell
.venv\Scripts\python -m streamlit run app/main.py
```

## Data

Game data is never committed to git. It lives only on your computer:

- `data/raw/`: downloaded files, exactly as they came
- `data/processed/`: tables built from the raw files by this project's scripts

The main planned source is a dataset of 43,947 anonymized 4-player Colonist.io games, for research and educational use only. As of 2026-11-25 its download is offline (see `ROADMAP.md`, Phase 2). If used, cite it as the dataset asks:

```
MR. MUCHO BUCHO Game Data (2025)
43,947 anonymized 4-player Catan games
https://github.com/Catan-data/dataset
```

Other sources this project may use, credited when they are:
- [Catanatron](https://github.com/bcollazo/catanatron), an open-source Catan simulator
- [Catan Trainer](https://catantrainer.com) placement statistics ([data](https://github.com/dglass211/catan-placement-data), CC BY 4.0)

## Disclaimer

Personal, non-commercial learning project. Not affiliated with CATAN GmbH, Catan Studio, or Colonist.io.
