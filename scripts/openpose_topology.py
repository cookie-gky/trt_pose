PARTS = [
    "NOSE",
    "NECK",
    "RSHOULDER",
    "RELBOW",
    "RWRIST",
    "LSHOULDER",
    "LELBOW",
    "LWRIST",
    "RHIP",
    "RKNEE",
    "RANKLE",
    "LHIP",
    "LKNEE",
    "LANKLE",
    "REYE",
    "LEYE",
    "REAR",
    "LEAR",
]

NUM_PARTS = len(PARTS)

TOPOLOGY = [
    [1, 0, PARTS.index('NECK'), PARTS.index('RHIP')],
    [3, 2, PARTS.index('RHIP'), PARTS.index('RKNEE')],
    [5, 4, PARTS.index('RKNEE'), PARTS.index('RANKLE')],
    [7, 6, PARTS.index('NECK'), PARTS.index('LHIP')],
    [9, 8, PARTS.index('LHIP'), PARTS.index('LKNEE')],
    [11, 10, PARTS.index('LKNEE'), PARTS.index('LANKLE')],
    [13, 12, PARTS.index('NECK'), PARTS.index('RSHOULDER')],
    [15, 14, PARTS.index('RSHOULDER'), PARTS.index('RELBOW')],
    [17, 16, PARTS.index('RELBOW'), PARTS.index('RWRIST')],
    [19, 18, PARTS.index('RSHOULDER'), PARTS.index('REAR')],
    [21, 20, PARTS.index('NECK'), PARTS.index('LSHOULDER')],
    [23, 22, PARTS.index('LSHOULDER'), PARTS.index('LELBOW')],
    [25, 24, PARTS.index('LELBOW'), PARTS.index('LWRIST')],
    [27, 26, PARTS.index('LSHOULDER'), PARTS.index('RHIP')],
    [29, 28, PARTS.index('NECK'), PARTS.index('NOSE')],
    [31, 30, PARTS.index('NOSE'), PARTS.index('REYE')],
    [33, 32, PARTS.index('NOSE'), PARTS.index('LEYE')],
    [35, 34, PARTS.index('REYE'), PARTS.index('REAR')],
    [37, 36, PARTS.index('LEYE'), PARTS.index('LEAR')],
]