import sys
import os

# ensure Day4_OOP is importable when running from workspace root
sys.path.insert(0, os.path.dirname(__file__))

from manager import Manager


def run():
    m = Manager("Alice", "Engineering")
    assert m.to_dict() == {"name": "Alice", "department": "Engineering"}
    out = m.display(print_out=False)
    print(out)
    print("TEST PASSED")


if __name__ == "__main__":
    run()
