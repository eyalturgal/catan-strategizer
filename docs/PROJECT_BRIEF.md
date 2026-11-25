# Catan Analyzer & Strategizer: Project Brief

*Working title. Owner: Eyal. Started: November 25, 2026.*

## 1. What this is, in plain words

When you start a chess game, you can study openings: known positions, the lines that follow from them, and why strong players choose one move over another. Catan has no opening book, because every board is different. This project builds one on demand.

I load into a game of classic 4-player Catan (mostly on Colonist.io). I see the board: where the resources are, which numbers sit on them, where the ports are, and what seat I'm in. I give that to the tool, and it tells me:

- what kind of board this is (what's scarce, what's strong, which ports matter)
- where to place my two starting settlements, given my seat and what the other players will likely take
- what strategy this board and seat favor, and what my win condition is
- what I should be trying to do in the early, middle and end game
- **why**, every time, with the evidence behind it

The point is not to play for me. The point is to **teach me to think like a strong player**, so that over time I can read a board myself. It's a teacher, not an autopilot.

## 2. Where the knowledge comes from

The tool's conclusions must come from evidence, not opinions typed in by hand. Three sources:

1. **Probability math.** Dice odds, pips, expected production per settlement, resource scarcity on this specific board. This is exact.
2. **Real games.** A public dataset of 43,947 anonymized 4-player Colonist.io games (github.com/Catan-data/dataset) with the starting board, every placement, every roll, trade, dev card and robber move, and who won. This tells us what actually wins, from which seat, on which kinds of boards. *(Status 2026-11-25: the download is offline. Finding it or other real game data is a roadmap task. If none turns up, simulation carries more of the load.)*
3. **Simulation.** Monte Carlo: play out a situation thousands of times with random dice to see how good a decision is with luck removed. Catanatron (an open-source Catan simulator and bot) can run thousands of full games in seconds.

Known Catan strategy writing (archetypes, principles, common mistakes) is used to **name** patterns. The data decides **how much they matter**.

Other tools already do parts of this (for example Catan Trainer, an opening placement coach). That's useful: they give us a standard to compare against.

## 3. The core idea: decisions vs luck

One game proves almost nothing. A great decision can lose to bad dice, and a bad one can win. The tool judges decisions by what happens across many games or many simulations, never by one result. A decision that loses most of the time is a mistake. A decision that usually wins but lost this time was bad luck. Learning to tell these apart is the main skill this project is meant to build in me.

## 4. Modules

### Strategy Library (the brain)
Strategy archetypes defined by what players actually **did** in real games (city-heavy ore/wheat, road and settlement expansion with wood/brick, development cards, port trading), plus dice odds, phase principles and common mistakes. Each entry carries evidence: win rates, by seat, by board condition, with sample sizes.

### Lab (general analyzer)
Answers general questions with data and simulation, for learning the game beyond any single board. Examples:
- How much does seat order matter? Does seat 1 win more than seat 4?
- When one resource is rare on the board (say ore totals 4 pips), is it better to grab the rare resource or stack the common one, and does the answer change by seat?
- How much is a 2:1 port worth, and when?
- What starting pip totals do winners usually have?

### Board Analyzer
Takes a specific board and describes it: production per spot, scarcity, strong numbers, port value, expansion room. Then finds similar boards in the dataset and reports what won there and how often.

### Opening Strategizer
Takes the board plus my seat. Simulates the snake draft (1-2-3-4-4-3-2-1) many times, with opponents modeled on how real online players draft from each seat. Recommends my best settlement **pair** (not just the best single spot), the archetype to play, the win condition, and early/mid/end game goals. Every recommendation shows its reasoning and its evidence, and says so when the evidence is thin.

### Later modules (not in v1)
- **Win probability model (machine learning):** trained on the dataset to estimate how good a position is, like a chess engine's evaluation. Lets me compare "place here vs there" as a win percentage.
- **Re-planner:** I enter where everyone actually placed, or a mid-game checkpoint, and it adjusts the plan.
- **Post-game review:** load my own downloaded Colonist games (e.g. via the ColonyHistorian extension) and see where I made mistakes vs got unlucky.
- **Live tracker:** reads the game log and tracks public card info. Only for casual and private games, never ranked or tournaments.
- **3-player support:** the dataset is 4-player only, so this needs simulation or other data.

## 5. Out of scope

- Player profiling or reading specific opponents. Trading and reading people is the human side of the game, and that's my job.
- Expansions (Seafarers, Cities & Knights) and 5-6 player.
- Selling it or using it competitively.

## 6. Classic Catan facts the build relies on

- 19 land hexes: 4 wood, 4 wheat, 4 sheep, 3 brick, 3 ore, 1 desert
- 18 number tokens: one 2, one 12, two each of 3, 4, 5, 6, 8, 9, 10, 11
- Pips (out of 36 rolls): 2/12 = 1, 3/11 = 2, 4/10 = 3, 5/9 = 4, 6/8 = 5. A 7 is 6/36.
- 54 settlement spots (corners), 72 road spots (edges)
- 9 harbors: 4 generic 3:1, and 5 specific 2:1 (one per resource)
- Distance rule: no settlement on a corner next to another settlement
- In the variable setup, 6s and 8s may not be on adjacent hexes (Colonist may differ: verify)
- Snake draft: placement order 1-2-3-4-4-3-2-1; the second settlement gives starting resources

## 7. Milestones

The working plan, with checkboxes and current status, lives in `ROADMAP.md`. This table is the original outline.

| Phase | What | Done when |
|---|---|---|
| 0 | Setup and data exploration | Dataset downloaded, game file format documented, win rate by seat answered |
| 1 | Board model and probability | Board represented in code, tests confirm 54 corners / 72 edges / correct adjacency, pip and production math works |
| 2 | Data layer | All games processed into a clean table: board features, seat, opening spots, what each player built, who won |
| 3 | Strategy Library and Lab | Archetypes defined from behavior; first 5 Lab questions answered with sample sizes |
| 4 | Board Analyzer and Opening Strategizer (v1) | I can enter a board and seat, and get a ranked settlement pair, archetype, win con and phase goals, each explained with evidence |
| v1 test | Real use | I've used it in at least 3 real games and understood why it recommended what it did |

*Change on 2026-11-25:* the dataset download is offline, so the board model (no data needed) comes first. Getting the data, documenting its format and the seat question move into the data phase. See `ROADMAP.md` and `docs/DECISIONS.md`.

Target: v1 in about a month (late December 2026). The machine learning model and later modules come after.

## 8. What I want to learn by building it

- How to read a Catan board and pick a strategy myself
- Expected value, variance, and separating decisions from luck
- Monte Carlo simulation
- Working with a real dataset: cleaning, exploring, asking good questions, not fooling myself (correlation vs causation, small samples)
- How a win probability model works and how it can go wrong (overfitting)
- How to direct an AI coding agent through a real multi-week project
