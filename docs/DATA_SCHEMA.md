# Data Schema

What's inside a game file, and how to read it. Built up as we learn the data.

> **Status: unverified.** Everything below comes from the dataset's README (copy at github.com/OrgadYron/catan_43k_games_dataset), not from opening real files. The download is offline as of 2026-11-25. When we get the data, check every line against several real games and mark it verified, corrected, or wrong.

## The dataset in one paragraph

43,947 anonymized 4-player Colonist.io games, one JSON file per game, about 6.9 GB uncompressed. Shipped as `games.tar.gz`, which extracts to a `games/` folder. No usernames, user IDs or country codes. Player colors, every game event, and the starting board are kept.

## Top-level layout

```
data
  playerUserStates     player info (anonymized)
  playOrder            turn order, as a list of player colors, e.g. [2, 5, 3, 1]
  gameSettings         game configuration (points to win, robber rules, etc.: to be checked)
  eventHistory
    events             every game event, in order
    endGameState       final state, including the winner
    totalTurnCount     game length in turns
    initialState       the starting board
```

## Codes

**Player colors**

| Code | Color |
|---|---|
| 1 | Blue |
| 2 | Red |
| 3 | Orange |
| 4 | Brown (rare) |
| 5 | White |

**Resources**

| Code | Resource |
|---|---|
| 1 | Brick |
| 2 | Wool (sheep) |
| 3 | Grain (wheat) |
| 4 | Ore |
| 5 | Lumber (wood) |

**Event types** (in `stateChange.gameLogState`, field `text.type`)

| Type | Meaning |
|---|---|
| 4 | Building placed (settlement, road or city) |
| 11 | Resources received from a dice roll |
| 14 | Trade with the bank |
| 15 | Trade with a player |
| 20 | Development card played |
| 22 | Development card bought |
| 45 | Winner declared |
| 49 | Robber moved |
| 55 | Cards discarded (a 7 was rolled) |
| 86 | Monopoly result |

**Development cards** (`cardEnum` in event type 20)

| Code | Card |
|---|---|
| 10, 11 | Knight |
| 12 | Monopoly |
| 13 | Victory Point |
| 14 | Road Building |
| 15 | Year of Plenty |

## Board coordinates

- **Hexes:** `(x, y)`
- **Corners:** `(x, y, z)`, where `z = 0` is the hex's top corner and `z = 1` its bottom corner. Our reading (to check): each hex "owns" its top and bottom corners and shares the other four with neighbors. 19 land hexes own only 38 corners, so the other 16 of the 54 must hang off sea hexes
- **Edges:** IDs in `tileEdgeStates`

Mapping these onto our own board model is a Phase 2 task, checked on several real games before any analysis trusts it.

## Winner and points

In `data.eventHistory.endGameState.players`, keyed by color:

```json
"2": {
  "rank": 1,
  "color": 2,
  "winningPlayer": true,
  "victoryPoints": { "0": 3, "1": 2, "2": 1, "3": 1, "4": 1 }
}
```

`victoryPoints` keys: 0 settlements, 1 cities, 2 Largest Army, 3 Longest Road, 4 VP cards. The values look like counts, not points (a city or Largest Army is worth 2): to verify.

## Questions to answer when we open real files

- Which seat (1 to 4) is each color? Is `playOrder` the placement order?
- Where exactly are the opening placements, and can we tell the first settlement from the second?
- Are ports in `initialState`, and how are they positioned?
- What's in `gameSettings`, and how many games use non-classic settings?
- Are there unfinished, abandoned, or bot-filled games?
