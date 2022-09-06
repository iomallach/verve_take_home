from typing import List, Optional
import pathlib

def sum_two_and_multiply(entries: List[int], target: int = 2020) -> Optional[int]:
    difference_seen = set()

    for e in entries:
        diff = target - e
        if diff in difference_seen:
            return e * diff
        difference_seen.add(e)
    return None

def sum_three_and_multiply(entries: List[int], target: int = 2020) -> Optional[int]:
    for idx, e in enumerate(entries):
        two_product = sum_two_and_multiply(entries[idx + 1:], target - e)
        if two_product:
            return e * two_product

def read_entries(path: pathlib.Path) -> List[int]:
    return [int(num) for num in path.read_text().split("\n")]


if __name__ == '__main__':
    PATH = pathlib.Path(__file__).parent.joinpath("./entries.txt").resolve()
    entries = read_entries(PATH)
    print(sum_two_and_multiply(entries))
    print(sum_three_and_multiply(entries))
