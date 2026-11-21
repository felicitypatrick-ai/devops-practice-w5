"""Harbor Street Bakery: gift box prices (course sample code)."""

BOX_SIZE = 6  # items in one gift box
BOX_DISCOUNT_CENTS = 50


def box_price(price_cents):
    """Return the price of one full box before any discount, in cents."""
    return price_cents * BOX_SIZE


def gift_box_total(price_cents, boxes):
    """Return the total for a number of gift boxes, in cents."""
    if boxes < 1:
        raise ValueError("boxes must be at least 1")
    return box_price(price_cents) * boxes - BOX_DISCOUNT_CENTS * boxes
