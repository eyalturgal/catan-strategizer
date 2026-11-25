"""Facts about the board's shape that must always be true."""

from collections import Counter

from catan.board.grid import (
    COASTAL_CORNERS,
    COASTAL_EDGES,
    CORNER_EDGES,
    CORNER_HEXES,
    CORNER_NEIGHBORS,
    CORNER_POINTS,
    EDGE_HEXES,
    EDGES,
    HEX_COORDS,
    HEX_CORNERS,
    HEX_EDGES,
    HEX_NEIGHBORS,
)


# --- Counts -------------------------------------------------------------

def test_19_hexes_54_corners_72_edges():
    assert len(HEX_COORDS) == 19
    assert len(CORNER_POINTS) == 54
    assert len(EDGES) == 72


def test_rows_of_3_4_5_4_3():
    hexes_per_row = Counter(r for q, r in HEX_COORDS)
    assert [hexes_per_row[r] for r in range(-2, 3)] == [3, 4, 5, 4, 3]


def test_every_hex_has_6_different_corners_and_6_different_sides():
    for corners, sides in zip(HEX_CORNERS, HEX_EDGES):
        assert len(set(corners)) == 6
        assert len(set(sides)) == 6


# --- Corners and the hexes they touch ----------------------------------

def test_each_corner_touches_1_to_3_hexes():
    how_many = Counter(len(hexes) for hexes in CORNER_HEXES)
    # 24 inland corners touch 3 hexes; on the coast, 12 touch 2 and 18 touch 1.
    assert how_many == {3: 24, 2: 12, 1: 18}


def test_corner_and_hex_lookups_agree():
    for hex_id, corners in enumerate(HEX_CORNERS):
        for c in corners:
            assert hex_id in CORNER_HEXES[c]
    for corner, hexes in enumerate(CORNER_HEXES):
        for h in hexes:
            assert corner in HEX_CORNERS[h]


# --- The coast -----------------------------------------------------------

def test_coast_has_30_corners_and_30_edges():
    assert len(COASTAL_CORNERS) == 30
    assert len(COASTAL_EDGES) == 30


def test_coastal_edges_join_coastal_corners():
    for e in COASTAL_EDGES:
        a, b = EDGES[e]
        assert a in COASTAL_CORNERS and b in COASTAL_CORNERS


# --- Corner neighbors (one road apart) --------------------------------

def test_every_corner_has_2_or_3_neighbors():
    how_many = Counter(len(n) for n in CORNER_NEIGHBORS)
    assert how_many == {2: 18, 3: 36}


def test_neighbors_work_both_ways():
    for corner, neighbors in enumerate(CORNER_NEIGHBORS):
        for n in neighbors:
            assert corner in CORNER_NEIGHBORS[n]


def test_neighbors_are_exactly_the_corners_joined_by_an_edge():
    for corner in range(54):
        joined = {a if b == corner else b for a, b in (EDGES[e] for e in CORNER_EDGES[corner])}
        assert joined == set(CORNER_NEIGHBORS[corner])


def test_each_edge_joins_two_different_corners_and_borders_1_or_2_hexes():
    for (a, b), hexes in zip(EDGES, EDGE_HEXES):
        assert a != b
        assert len(hexes) in (1, 2)


# --- Hex neighbors (sharing a side) -------------------------------------

def test_42_pairs_of_hexes_touch():
    pairs = {frozenset((h, n)) for h, ns in enumerate(HEX_NEIGHBORS) for n in ns}
    assert len(pairs) == 42


def test_hex_neighbor_counts():
    how_many = Counter(len(n) for n in HEX_NEIGHBORS)
    # 7 inner hexes have 6 neighbors; on the outer ring, the 6 at the tips
    # have 3 and the 6 between them have 4.
    assert how_many == {6: 7, 3: 6, 4: 6}


def test_middle_hex_touches_6_hexes():
    middle = HEX_COORDS.index((0, 0))
    assert middle == 9
    assert len(HEX_NEIGHBORS[middle]) == 6


# --- Numbering stays put -------------------------------------------------

def test_numbering_starts_at_the_top_left():
    assert HEX_COORDS[0] == (0, -2)  # first hex of the top row
    assert HEX_CORNERS[0][0] == 0  # its top corner is corner 0
    top_row_tops = [HEX_CORNERS[h][0] for h in range(3)]
    assert top_row_tops == [0, 1, 2]
