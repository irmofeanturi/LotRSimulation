"""
Data for the Middle-earth simulation: places, group routes and events.

The timeline follows Tolkien's chronology of the War of the Ring (T.A. 3018-3019).
Day 0 = Frodo leaves Bag End (September 23, 3018). Every 'day' value is a running
day number from that point; the 'date' strings are only for display in the HUD.
"""

# ---------------------------------------------------------------------------
# Places on the map. Coordinates are NORMALISED (0..1) relative to the map image
# (x = east, y = south). This way they fit any window size and match the real
# background image (assets/middle_earth_bg.png).
#
# The values were carefully measured against the Wikimedia map. To fine-tune them
# pixel-perfectly:  python3 middle_earth_hud.py --calibrate
# That writes a locations.json which overrides these defaults.
# ---------------------------------------------------------------------------
LOCATIONS = {
    "Grey Havens":      (0.172, 0.267),
    "Hobbiton":         (0.257, 0.275),
    "Bree":             (0.325, 0.281),
    "Weathertop":       (0.376, 0.262),
    "Rivendell":        (0.483, 0.264),
    "Caradhras":        (0.478, 0.362),
    "Moria":            (0.470, 0.386),       # West-gate (Doors of Durin)
    "Lothlorien":       (0.520, 0.415),
    "Argonath":         (0.591, 0.590),
    "Amon Hen":         (0.588, 0.603),       # west shore of Nen Hithoel
    "Emyn Muil":        (0.612, 0.585),
    "Dead Marshes":     (0.640, 0.607),
    "Black Gate":       (0.672, 0.612),
    "Ithilien":         (0.657, 0.672),
    "Minas Morgul":     (0.665, 0.698),
    "Cirith Ungol":     (0.671, 0.689),
    "Mount Doom":       (0.707, 0.666),
    "Barad-dur":        (0.745, 0.662),
    "Fangorn":          (0.505, 0.520),
    "Isengard":         (0.441, 0.541),
    "Edoras":           (0.493, 0.624),
    "Helm's Deep":      (0.452, 0.598),
    "Dunharrow":        (0.493, 0.640),
    "Erech":            (0.493, 0.671),
    "Pelargir":         (0.628, 0.786),
    "Minas Tirith":     (0.639, 0.699),
}

# ---------------------------------------------------------------------------
# Route waypoints along the roads and rivers drawn on the map (normalised x, y).
# The road points were taken from the dotted roads of the map SVG itself.
# Keyframes may use these between two named places so a group follows the
# road / river instead of cutting straight across mountains.
# ---------------------------------------------------------------------------
# East-West Road: Hobbiton -> Brandywine Bridge -> Bree -> Weathertop -> Last Bridge -> Ford of Bruinen
ROAD_SHIRE_BREE = [(0.265, 0.279), (0.270, 0.276), (0.275, 0.272), (0.283, 0.270), (0.289, 0.269),
                   (0.294, 0.268), (0.300, 0.267), (0.307, 0.266), (0.313, 0.267), (0.318, 0.270),
                   (0.321, 0.277)]
ROAD_BREE_WEATHERTOP = [(0.336, 0.277), (0.342, 0.277), (0.350, 0.277), (0.356, 0.278), (0.362, 0.278),
                        (0.369, 0.278), (0.375, 0.277), (0.378, 0.276)]
ROAD_WEATHERTOP_FORD = [(0.384, 0.274), (0.390, 0.271), (0.396, 0.268), (0.401, 0.266), (0.406, 0.263),
                        (0.412, 0.262), (0.418, 0.262), (0.425, 0.262), (0.432, 0.264), (0.440, 0.266),
                        (0.446, 0.267), (0.453, 0.269), (0.460, 0.270), (0.465, 0.271), (0.471, 0.272),
                        (0.475, 0.273)]
# West of the Misty Mountains, south from Rivendell to Hollin (Eregion)
RIVENDELL_HOLLIN = [(0.470, 0.290), (0.460, 0.325), (0.455, 0.350)]
# Through Moria to Dimrill Dale and down the Silverlode (Celebrant) into Lorien
MORIA_LORIEN = [(0.490, 0.386), (0.500, 0.395), (0.510, 0.408)]
# By boat down the Anduin from Lorien to the Argonath
ANDUIN_LORIEN_ARGONATH = [(0.535, 0.427), (0.543, 0.449), (0.560, 0.464), (0.571, 0.476),
                          (0.568, 0.493), (0.586, 0.496), (0.580, 0.515), (0.589, 0.532),
                          (0.589, 0.547), (0.585, 0.579)]
# Across the open Emnet of Rohan to the eastern eaves of Fangorn
EMNET_TO_FANGORN = [(0.570, 0.585), (0.548, 0.565), (0.515, 0.532)]
# Great West Road: Edoras -> Mering Stream -> Anorien -> Minas Tirith
ROAD_EDORAS_MINAS_TIRITH = [(0.504, 0.632), (0.510, 0.643), (0.516, 0.651), (0.525, 0.656), (0.533, 0.660),
                            (0.541, 0.666), (0.549, 0.671), (0.558, 0.674), (0.567, 0.675), (0.577, 0.677),
                            (0.586, 0.678), (0.596, 0.679), (0.605, 0.683), (0.615, 0.687), (0.623, 0.692),
                            (0.633, 0.696)]
# Minas Tirith -> Osgiliath -> Crossroads -> north through Ithilien -> Morannon
ROAD_MINAS_TIRITH_BLACK_GATE = [(0.651, 0.700), (0.660, 0.699), (0.658, 0.692), (0.658, 0.679), (0.657, 0.665),
                                (0.656, 0.650), (0.656, 0.637), (0.656, 0.624), (0.659, 0.613), (0.668, 0.610)]
# Edoras -> Westfold -> Helm's Deep
ROAD_EDORAS_HELMS_DEEP = [(0.486, 0.615), (0.482, 0.611), (0.463, 0.590), (0.461, 0.594)]
# Erech -> Lamedon -> Linhir -> Lebennin -> Pelargir (Grey Company)
ROAD_ERECH_PELARGIR = [(0.517, 0.694), (0.520, 0.705), (0.528, 0.712), (0.536, 0.718), (0.544, 0.727),
                       (0.550, 0.739), (0.552, 0.751), (0.554, 0.766), (0.554, 0.779), (0.558, 0.789),
                       (0.567, 0.795), (0.577, 0.797), (0.587, 0.796), (0.597, 0.794), (0.606, 0.793),
                       (0.615, 0.793)]
# Up the Anduin with the captured corsair ships
ANDUIN_PELARGIR_MINAS_TIRITH = [(0.636, 0.776), (0.640, 0.752), (0.641, 0.729)]


def _along(d0, d1, points):
    """Spread `points` evenly between story days d0 and d1 as keyframes."""
    n = len(points)
    return [(d0 + (d1 - d0) * (i + 1) / (n + 1), p) for i, p in enumerate(points)]


# ---------------------------------------------------------------------------
# Group routes. Each group has keyframes (day, place name) and an "icon"
# (emblem on its seal: star, ring, sword, leaf or hat).
# Positions are interpolated (spline) between two keyframes.
# A group is only visible between its first and last day.
# ---------------------------------------------------------------------------
TRACKS = [
    {
        "name": "The Fellowship",
        "icon": "star",               # emblem on the map seal and in the legend
        "color": (232, 198, 92),
        "members": "Frodo, Sam, Merry, Pippin, Aragorn, Legolas, Gimli, Boromir, Gandalf",
        # A keyframe target is a place name OR a raw (x, y) waypoint that bends the
        # route along the roads and rivers of the map (see the route lists above).
        "keyframes": [
            (0,   "Hobbiton"),
            *_along(0, 6, ROAD_SHIRE_BREE),
            (6,   "Bree"),
            *_along(6, 13, ROAD_BREE_WEATHERTOP),
            (13,  "Weathertop"),
            *_along(13, 27, ROAD_WEATHERTOP_FORD),
            (27,  "Rivendell"),
            (93,  "Rivendell"),
            *_along(93, 104, RIVENDELL_HOLLIN),
            (104, "Caradhras"),
            (108, (0.462, 0.375)),       # turned back from the snow, south to Moria
            (112, "Moria"),
            *_along(112, 116, MORIA_LORIEN),
            (116, "Lothlorien"),
            (146, "Lothlorien"),
            *_along(146, 152, ANDUIN_LORIEN_ARGONATH),
            (152, "Argonath"),
            (156, "Amon Hen"),
        ],
    },
    {
        "name": "Frodo & Sam",
        "icon": "ring",
        "color": (214, 74, 62),
        "members": "Frodo, Sam (and Gollum)",
        "keyframes": [
            (156, "Amon Hen"),
            (157, (0.598, 0.598)),       # across Nen Hithoel to the eastern shore
            (159, "Emyn Muil"),
            (163, "Dead Marshes"),
            (165, "Black Gate"),
            *_along(165, 167, ROAD_MINAS_TIRITH_BLACK_GATE[-1:4:-1]),   # south into Ithilien
            (167, "Ithilien"),
            *_along(167, 171, ROAD_MINAS_TIRITH_BLACK_GATE[3:1:-1]),    # to the Crossroads
            (172, "Minas Morgul"),
            (173, "Cirith Ungol"),
            (181, "Cirith Ungol"),
            (183, (0.690, 0.680)),       # across the plain of Gorgoroth
            (185, "Mount Doom"),
            (190, "Minas Tirith"),       # carried by the Eagles
            (222, "Minas Tirith"),
        ],
    },
    {
        "name": "Aragorn, Legolas & Gimli",
        "icon": "sword",
        "color": (86, 150, 222),
        "members": "Aragorn, Legolas, Gimli",
        "keyframes": [
            (156, "Amon Hen"),
            *_along(156, 159, EMNET_TO_FANGORN),   # pursuit across the Emnet of Rohan
            (159, "Fangorn"),
            (160.5, (0.505, 0.575)),     # riding with Gandalf across the Entwash
            (162, "Edoras"),
            *_along(162, 163, ROAD_EDORAS_HELMS_DEEP),
            (163, "Helm's Deep"),
            (165, "Helm's Deep"),
            *_along(165, 166, ROAD_EDORAS_HELMS_DEEP[::-1]),
            (166, "Edoras"),
            (167, "Dunharrow"),
            (168, "Erech"),              # Paths of the Dead, under the mountains
            *_along(168, 170, ROAD_ERECH_PELARGIR),
            (170, "Pelargir"),
            *_along(170, 175, ANDUIN_PELARGIR_MINAS_TIRITH),  # with the corsair ships
            (175, "Minas Tirith"),
            *_along(175, 185, ROAD_MINAS_TIRITH_BLACK_GATE),
            (185, "Black Gate"),
            *_along(185, 190, ROAD_MINAS_TIRITH_BLACK_GATE[::-1]),
            (190, "Minas Tirith"),
            (222, "Minas Tirith"),
        ],
    },
    {
        "name": "Merry & Pippin",
        "icon": "leaf",
        "color": (108, 190, 110),
        "members": "Merry, Pippin (split from day 165: Pippin -> Minas Tirith, Merry with Rohan)",
        "keyframes": [
            (156, "Amon Hen"),
            *_along(156, 159, EMNET_TO_FANGORN),   # carried off by the Uruk-hai
            (159, "Fangorn"),
            (161, (0.470, 0.522)),       # with Treebeard to the western edge of the forest
            (163, "Isengard"),
            (165, "Isengard"),
            (165.5, (0.470, 0.585)),     # down into the Westfold
            (166, "Edoras"),
            *_along(166, 169, ROAD_EDORAS_MINAS_TIRITH),   # east to Gondor
            (169, "Minas Tirith"),
            (175, "Minas Tirith"),
            (222, "Minas Tirith"),
        ],
    },
    {
        "name": "Gandalf the White",
        "icon": "hat",
        "color": (236, 236, 246),
        "members": "Gandalf (returned after his fall in Moria)",
        "keyframes": [
            (159, "Fangorn"),
            (160.5, (0.505, 0.575)),
            (162, "Edoras"),
            (165, "Edoras"),
            *_along(165, 169, ROAD_EDORAS_MINAS_TIRITH),   # riding east with Pippin
            (169, "Minas Tirith"),
            (175, "Minas Tirith"),
            *_along(175, 185, ROAD_MINAS_TIRITH_BLACK_GATE),
            (185, "Black Gate"),
            *_along(185, 190, ROAD_MINAS_TIRITH_BLACK_GATE[::-1]),
            (190, "Minas Tirith"),
            (222, "Minas Tirith"),
        ],
    },
]

# ---------------------------------------------------------------------------
# Characters who fall during the journey. They have no onward route, so instead
# of a moving dot they get a memorial marker (chosen via "symbol", e.g. a horn)
# at the place where they fall, shown from that day on, plus a legend entry.
# Available symbols: "horn".
# ---------------------------------------------------------------------------
FALLEN = [
    {
        "name": "Boromir",
        "symbol": "horn",                  # the Horn of Gondor
        "color": (238, 240, 247),          # Gondor silver-white (shown on a dark medallion)
        "location": "Amon Hen",
        "day": 156,                        # falls at the breaking of the Fellowship
        "note": "fell defending Merry & Pippin",
    },
]


# ---------------------------------------------------------------------------
# The three films and their EXTENDED EDITION runtimes (in minutes). The master
# clock runs along this total runtime, so at 1x speed a full run lasts as long
# as watching all three extended editions back to back.
# ---------------------------------------------------------------------------
FILMS = [
    ("The Fellowship of the Ring", "FotR", 228),
    ("The Two Towers",             "TTT",  235),
    ("The Return of the King",     "RotK", 263),
]
TOTAL_RUNTIME = sum(rt for _, _, rt in FILMS)   # minutes (= 726)


# ---------------------------------------------------------------------------
# Events for the HUD. Each event has:
#   (day, film_minute, date, film, title, text)
# - day .......... story day (drives the group routes, see TRACKS)
# - film_minute .. approximate position within the trilogy's extended runtime
#                  (cumulative minutes from the start of film 1). Monotonic.
# The displayed event is the latest one whose film_minute <= current time.
# ---------------------------------------------------------------------------
EVENTS = [
    (0,    40, "Sep 23, 3018", "The Fellowship of the Ring",
     "Departure from Bag End",
     "Frodo leaves the Shire with the One Ring, heading for Bree."),
    (6,    66, "Sep 29, 3018", "The Fellowship of the Ring",
     "At the Prancing Pony",
     "In Bree the hobbits meet Strider (Aragorn)."),
    (13,   85, "Oct 6, 3018", "The Fellowship of the Ring",
     "Weathertop",
     "Frodo is wounded by the Witch-king with a Morgul blade."),
    (27,  104, "Oct 20, 3018", "The Fellowship of the Ring",
     "Arrival in Rivendell",
     "Elrond heals Frodo. The free peoples debate the fate of the Ring."),
    (93,  130, "Dec 25, 3018", "The Fellowship of the Ring",
     "The Fellowship sets out",
     "Nine companions leave Rivendell heading south."),
    (104, 142, "Jan 11, 3019", "The Fellowship of the Ring",
     "Caradhras",
     "Snow forces the Fellowship to take the road through Moria."),
    (112, 152, "Jan 13, 3019", "The Fellowship of the Ring",
     "The Mines of Moria",
     "The Fellowship enters the ancient dwarven halls."),
    (114, 170, "Jan 15, 3019", "The Fellowship of the Ring",
     "Gandalf falls",
     "On the Bridge of Khazad-dum, Gandalf falls into the abyss with the Balrog."),
    (116, 184, "Jan 17, 3019", "The Fellowship of the Ring",
     "Lothlorien",
     "Galadriel welcomes the Fellowship into the Golden Wood."),
    (146, 200, "Feb 16, 3019", "The Fellowship of the Ring",
     "Farewell to Lorien",
     "They travel down the Anduin by boat."),
    (156, 222, "Feb 26, 3019", "The Fellowship of the Ring",
     "The Fellowship breaks",
     "Boromir falls. Frodo & Sam head east, Merry & Pippin are captured, "
     "Aragorn, Legolas & Gimli take up the pursuit."),
    (159, 255, "Feb 29, 3019", "The Two Towers",
     "Fangorn & Gandalf's return",
     "Merry & Pippin meet Treebeard. Gandalf returns as the White."),
    (162, 285, "Mar 2, 3019", "The Two Towers",
     "Edoras",
     "Gandalf frees King Theoden from Saruman's grip."),
    (163, 300, "Mar 3, 3019", "The Two Towers",
     "Frodo & Sam in the Dead Marshes",
     "Gollum leads them through the marshes toward the Black Gate."),
    (164, 425, "Mar 4, 3019", "The Two Towers",
     "Battle of Helm's Deep",
     "Rohan holds the fortress; the Ents overrun Isengard."),
    (165, 440, "Mar 5, 3019", "The Two Towers",
     "At the Black Gate",
     "The gate is shut - Gollum knows another way. Pippin looks into the palantir."),
    (167, 458, "Mar 7, 3019", "The Two Towers",
     "Ithilien & Faramir",
     "Frodo & Sam are caught by Faramir's rangers."),
    (169, 500, "Mar 9, 3019", "The Return of the King",
     "Gandalf & Pippin in Minas Tirith",
     "The white city of Gondor prepares against Mordor."),
    (172, 560, "Mar 12, 3019", "The Return of the King",
     "Cirith Ungol",
     "Shelob lurks in the pass. Aragorn takes the Paths of the Dead."),
    (175, 640, "Mar 15, 3019", "The Return of the King",
     "Battle of the Pelennor Fields",
     "Theoden falls, the Witch-king is slain, Aragorn arrives with the fleet."),
    (185, 690, "Mar 25, 3019", "The Return of the King",
     "The Ring is destroyed",
     "The host at the Black Gate draws Sauron's eye - at Mount Doom the Ring falls. Sauron is defeated."),
    (222, 720, "May 1, 3019", "The Return of the King",
     "The Coronation",
     "Aragorn is crowned King Elessar. A new age begins."),
]

# Last day of the timeline (used for normalisation of the routes).
MAX_DAY = EVENTS[-1][0]
