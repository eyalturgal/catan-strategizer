# Learning Log

Concepts that came up while building, in plain words. Newest session first.

## 2026-11-25: Setup

**Git, GitHub and hosting are three different things.**
Git keeps the history of a project's files on your computer. GitHub is a website that stores a copy of that history online (backup, sharing, portfolio). Hosting (like Vercel for the stock project) is what turns code into a website anyone can visit. This project uses the first two. It runs on your own computer, so v1 needs no hosting.

**Keep the recipe, not the cake.**
Big data files (about 7 GB of games) never go on GitHub: it refuses files over 100 MB, and the data isn't ours to republish. Instead, GitHub keeps the scripts that build our tables from the raw data. Lose the tables and you can rebuild them; lose the scripts and you can't.

**A Python environment is like `node_modules`.**
`requirements.txt` lists the libraries the project needs (like `package.json`). The `.venv` folder holds the installed copies (like `node_modules`), private to this project and never committed. So two projects can use different versions of the same library without clashing.

**Luck has a size, and you can measure it.**
Someone found win rates by seat of 24.9%, 25.0%, 25.2% and 25.0% over about 41,000 games each. Even if every seat were exactly equal, luck alone would push each number up or down by about 0.4 points. All four differences are smaller than that, so they tell us nothing. The bigger the sample, the smaller the luck. With only 100 games, luck alone could move a win rate by about 8 points.

**Reverse causation.**
The same analysis says Monopoly played in the last 10% of the game wins 57% of the time. But the game ends right after the winning move, so the last card played is usually the winner's. Winning causes the late Monopoly; the late Monopoly doesn't cause the win. Ask "could the result be causing the thing, instead of the other way around?"

**Dice odds come from counting.**
Two dice have 36 equally likely combinations (6 x 6). A 7 can be made 6 ways, a 6 or 8 in 5 ways, down to a 2 or 12 in 1 way. Those counts are the pips on the number tokens. The project's first test counts all 36 combinations in code and checks they match the pip table.
