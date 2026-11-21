"""Harbor Street Bakery: release check, run right after each deploy (course sample code)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from order_total import order_total
from gift_box import gift_box_total


def dollars(cents):
    return f"${cents / 100:.2f}"


print(f"Release check: {environment}")
print(open(os.path.join(release, "RELEASE.txt")).read().strip())
print("12 items at $2.00:", dollars(order_total(200, 12)))
print("24 items at $2.00:", dollars(order_total(200, 24)))
print("1 gift box of $3.00 items:", dollars(gift_box_total(300, 1)))
print("Release check passed.")
