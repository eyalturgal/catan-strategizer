# Findings

Every Lab result goes here: the question, the method, the answer, and the sample size. If the evidence is thin, say so.

## Template

```
### [Question]
- Date:
- Data: which games or simulations, how many, any filters
- Method: what was counted or simulated, in plain words
- Answer: the number(s), with an uncertainty range
- Sample size:
- Caveats: small slices, correlation vs causation, luck, player skill, bots vs humans
- What it means for play:
```

## Our results

None yet. The first one is planned for Phase 2: win rate by seat.

---

## Claims from others (not verified by us)

These are leads and comparison points, not findings. Each one gets checked with our own data before the tool uses it.

### Seat barely matters for win rate
- **Source:** FINDINGS_SUMMARY.md in github.com/OrgadYron/catan_43k_games_dataset (analysis of 41,310 of the 43,947 games, January 2025)
- **Claim:** win rate by placement position: 1st 24.91%, 2nd 24.95%, 3rd 25.18%, 4th 24.95%
- **Our quick check of the math:** with about 41,000 games per seat, luck alone moves a 25% win rate by about ±0.4 points (95% range). All four numbers sit inside that range, so the seats look equal
- **To verify:** does "pick position" mean seat order, and why were 2,637 games left out?

### Late Monopoly wins (a warning example)
- **Same source.** Claim: Monopoly played in the last 10% of a game wins 57.1% of the time, so save it for late
- **Why we don't trust the conclusion:** reverse causation. The game ends right after the winning move, so a card played at the very end is mostly the winner's final card. Winning causes "late Monopoly," not the other way around. The same file's "1 VP card: 41% win rate vs 0: 20%" has a similar problem: a VP card is literally a point, and players with strong economies buy more dev cards
- **Lesson:** a timing or count measured near the end of a game is often a symptom of winning, not a cause

### Opening quality vs win rate (Catan Trainer)
- **Source:** github.com/dglass211/catan-placement-data (CC BY 4.0, credit "Catan Trainer"), generated 2026-11-05
- **Claims:** first settlement in their engine's top spot: 46.4% win rate (138 games); outside the top five: 32% (103 games). Openings with no wheat: 28.6% (27 games). Their "low production" rule: first settlement under 10 pips
- **Caveats:** 431 games, imported by users of their tool (self-selected). Those players won 42.1% overall, far above the 25% average, so they're not typical. Their own README says the numbers are correlations, not experiments
- **Use:** a benchmark for our Strategizer, and a starting checklist of opening mistakes
