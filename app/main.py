"""Catan Strategizer app. For now, a hello page showing dice odds.

Run with:  .venv\\Scripts\\python -m streamlit run app/main.py
"""

import pandas as pd
import streamlit as st

from catan.board.dice import roll_counts, roll_probability

st.set_page_config(page_title="Catan Strategizer", page_icon="🎲")

st.title("Catan Strategizer")
st.write(
    "Hello! The project is set up and running. The board model comes next (Phase 1). "
    "For now, here's the math everything else builds on."
)

st.header("Dice odds")
st.write(
    "Two dice have 36 equally likely outcomes. Counting how many of them make each "
    "total gives the pips on the number tokens. A 7 has the most ways (6) but no "
    "token: it moves the robber."
)

rows = [
    {
        "Total": total,
        "Ways (out of 36)": ways,
        "Chance": f"{float(roll_probability(total)):.1%}",
        "Pips on token": "none (robber)" if total == 7 else ways,
    }
    for total, ways in roll_counts().items()
]
st.dataframe(pd.DataFrame(rows), hide_index=True)

st.caption("Source: counted in code (src/catan/board/dice.py), checked by tests/test_dice.py.")
