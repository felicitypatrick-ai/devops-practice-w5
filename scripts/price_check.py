"""Harbor Street Bakery: price check (course sample code).
Checks the order and gift box prices the order page shows against the owner's rules.
It waits 20 seconds on purpose: it stands in for a slow check on a real project."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.gift_box import gift_box_total
from app.order_total import order_total

WAIT_SECONDS = 20


def check_orders():
    """1 to 11 items: full price. 12 to 23 items: 10 percent off."""
    for quantity in range(1, 24):
        full = 200 * quantity
        rule = full - full * 10 // 100 if quantity >= 12 else full
        if order_total(200, quantity) != rule:
            return f"{quantity} items cost {order_total(200, quantity)} cents; the rule gives {rule}"
    return None


def check_gift_boxes():
    """A box holds 6 items; each box is 50 cents off."""
    for boxes in range(1, 11):
        rule = 300 * 6 * boxes - 50 * boxes
        if gift_box_total(300, boxes) != rule:
            return f"{boxes} gift boxes cost {gift_box_total(300, boxes)} cents; the rule gives {rule}"
    return None


PARTS = {"orders": check_orders, "gift-boxes": check_gift_boxes}
part = sys.argv[1] if len(sys.argv) > 1 else ""
if part not in PARTS:
    print(f"Unknown part: {part}. Use orders or gift-boxes.")
    sys.exit(2)
time.sleep(WAIT_SECONDS)
problem = PARTS[part]()
if problem:
    print(f"Price check failed: {problem}")
    sys.exit(1)
print(f"Price check passed: {part}")
