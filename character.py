import os


def _load_level_dict(filename: str) -> dict:
    """Load a mapping from the given level file: first column -> second column.

    Lines are expected in the format: "<char><whitespace><pinyin>" (extra whitespace allowed).
    If a line has more than two whitespace-separated tokens, only the first two are used.
    Empty lines are ignored.
    """
    mapping: dict = {}
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            key = parts[0]
            value = parts[1]
            mapping[key] = value
    return mapping


level1 = _load_level_dict("level1.txt")
level2 = _load_level_dict("level2.txt")
level3 = _load_level_dict("level3.txt")
level4 = _load_level_dict("level4.txt")
level5 = _load_level_dict("level5.txt")
level6 = _load_level_dict("level6.txt")
level7 = _load_level_dict("level7.txt")
level8 = _load_level_dict("level8.txt")
level9 = _load_level_dict("level9.txt")
level10 = _load_level_dict("level10.txt")
level11 = _load_level_dict("level11.txt")
level12 = _load_level_dict("level12.txt")
level13 = _load_level_dict("level13.txt")
level14 = _load_level_dict("level14.txt")


__all__ = [
    "level1",
    "level2",
    "level3",
    "level4",
    "level5",
    "level6",
    "level7",
    "level8",
    "level9",
    "level10",
    "level11",
    "level12",
    "level13",
    "level14",
]


