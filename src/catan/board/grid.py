"""The shape of a classic Catan board: 19 hexes, 54 corners, 72 edges.

This file knows only the shape, not what's on it (resources, numbers, harbors).

Hexes are "pointy-top" and sit in rows of 3, 4, 5, 4, 3. Each hex has an
address (q, r): r is the row, from -2 at the top to 2 at the bottom, and q
moves left to right along the row. The middle hex is (0, 0).

Corners are found from the shape: each hex has 6 corner points, and a point
shared by two or three neighboring hexes is one corner. Positions are whole
numbers (x in steps of half a hex width, y in steps of a quarter of a hex
height), so there are no rounding errors.

Numbering, used everywhere in the project:
- hexes 0 to 18: row by row from the top, left to right
- corners 0 to 53: top to bottom, left to right
- edges 0 to 71: by the position of their middle, top to bottom, left to right

Every lookup below is a tuple indexed by those numbers. For example,
CORNER_HEXES[12] is the hexes that corner 12 touches.
"""

RADIUS = 2  # rings of hexes around the middle one: 1 + 6 + 12 = 19 hexes

# Where a hex's 6 corners sit relative to its center, clockwise from the top.
_CORNER_OFFSETS = ((0, -2), (1, -1), (1, 1), (0, 2), (-1, 1), (-1, -1))


def _reading_order(point):
    """Sort key for a point: top to bottom, then left to right."""
    x, y = point
    return (y, x)


def _build():
    # Hexes: every address within 2 steps of the middle, in reading order.
    coords = sorted(
        (
            (q, r)
            for r in range(-RADIUS, RADIUS + 1)
            for q in range(-RADIUS, RADIUS + 1)
            if abs(q + r) <= RADIUS
        ),
        key=lambda qr: (qr[1], qr[0]),
    )
    centers = [(2 * q + r, 3 * r) for q, r in coords]

    # Corners: every hex's 6 corner points; shared points count once.
    hex_points = [[(cx + dx, cy + dy) for dx, dy in _CORNER_OFFSETS] for cx, cy in centers]
    points = sorted({p for pts in hex_points for p in pts}, key=_reading_order)
    corner_id = {p: i for i, p in enumerate(points)}
    hex_corners = [tuple(corner_id[p] for p in pts) for pts in hex_points]

    # Edges: each side of a hex joins two neighboring corners; shared sides count once.
    def side(corners, i):
        a, b = corners[i], corners[(i + 1) % 6]
        return (min(a, b), max(a, b))

    sides = {side(cs, i) for cs in hex_corners for i in range(6)}

    def midpoint_order(edge):
        (xa, ya), (xb, yb) = points[edge[0]], points[edge[1]]
        return _reading_order((xa + xb, ya + yb))

    edges = sorted(sides, key=midpoint_order)
    edge_id = {e: i for i, e in enumerate(edges)}
    hex_edges = [tuple(edge_id[side(cs, i)] for i in range(6)) for cs in hex_corners]

    # Lookups in the other direction.
    corner_hexes = [[] for _ in points]
    for h, cs in enumerate(hex_corners):
        for c in cs:
            corner_hexes[c].append(h)

    edge_hexes = [[] for _ in edges]
    for h, es in enumerate(hex_edges):
        for e in es:
            edge_hexes[e].append(h)

    corner_neighbors = [[] for _ in points]
    corner_edges = [[] for _ in points]
    for e, (a, b) in enumerate(edges):
        corner_neighbors[a].append(b)
        corner_neighbors[b].append(a)
        corner_edges[a].append(e)
        corner_edges[b].append(e)

    # Two hexes are neighbors when they share a side.
    hex_neighbors = [[] for _ in coords]
    for hs in edge_hexes:
        if len(hs) == 2:
            a, b = hs
            hex_neighbors[a].append(b)
            hex_neighbors[b].append(a)

    def frozen(lists):
        return tuple(tuple(sorted(x)) for x in lists)

    return {
        "HEX_COORDS": tuple(coords),
        "HEX_CENTERS": tuple(centers),
        "CORNER_POINTS": tuple(points),
        "EDGES": tuple(edges),
        "HEX_CORNERS": tuple(hex_corners),
        "HEX_EDGES": tuple(hex_edges),
        "HEX_NEIGHBORS": frozen(hex_neighbors),
        "CORNER_HEXES": frozen(corner_hexes),
        "CORNER_NEIGHBORS": frozen(corner_neighbors),
        "CORNER_EDGES": frozen(corner_edges),
        "EDGE_HEXES": frozen(edge_hexes),
    }


_GRID = _build()

HEX_COORDS = _GRID["HEX_COORDS"]  # hex -> its (q, r) address
HEX_CENTERS = _GRID["HEX_CENTERS"]  # hex -> (x, y) of its center, for drawing
CORNER_POINTS = _GRID["CORNER_POINTS"]  # corner -> (x, y), for drawing
EDGES = _GRID["EDGES"]  # edge -> its two corners
HEX_CORNERS = _GRID["HEX_CORNERS"]  # hex -> its 6 corners, clockwise from the top
HEX_EDGES = _GRID["HEX_EDGES"]  # hex -> its 6 sides, clockwise from the upper right
HEX_NEIGHBORS = _GRID["HEX_NEIGHBORS"]  # hex -> hexes that share a side with it
CORNER_HEXES = _GRID["CORNER_HEXES"]  # corner -> the 1 to 3 hexes it touches
CORNER_NEIGHBORS = _GRID["CORNER_NEIGHBORS"]  # corner -> corners one road away
CORNER_EDGES = _GRID["CORNER_EDGES"]  # corner -> the 2 or 3 edges that meet there
EDGE_HEXES = _GRID["EDGE_HEXES"]  # edge -> the 1 or 2 hexes it borders

# The coast: corners touching fewer than 3 land hexes, edges bordering only 1.
COASTAL_CORNERS = tuple(c for c, hs in enumerate(CORNER_HEXES) if len(hs) < 3)
COASTAL_EDGES = tuple(e for e, hs in enumerate(EDGE_HEXES) if len(hs) == 1)
