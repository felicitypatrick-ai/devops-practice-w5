import unittest

from app.gift_box import box_price, gift_box_total


class GiftBoxTests(unittest.TestCase):
    def test_box_price_is_six_items(self):
        self.assertEqual(box_price(300), 1800)

    def test_one_box_gets_discount(self):
        self.assertEqual(gift_box_total(300, 1), 1750)

    def test_two_boxes_get_two_discounts(self):
        self.assertEqual(gift_box_total(300, 2), 3500)
