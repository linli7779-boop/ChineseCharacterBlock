import os


def _load_idiom_list(filename: str) -> list:
    """Load all non-empty lines from an idiom file as a list of strings."""
    items: list = []
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            items.append(line)
    return items


idiom_level1 = _load_idiom_list("idiom_level1.txt")
idiom_level2 = _load_idiom_list("idiom_level2.txt")
idiom_level3 = _load_idiom_list("idiom_level3.txt")
idiom_level4 = _load_idiom_list("idiom_level4.txt")
idiom_level5 = _load_idiom_list("idiom_level5.txt")
idiom_level6 = _load_idiom_list("idiom_level6.txt")


__all__ = [
    "idiom_level1",
    "idiom_level2",
    "idiom_level3",
    "idiom_level4",
    "idiom_level5",
    "idiom_level6",
]


