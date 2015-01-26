import receipt_ocr.app.ocr
import unittest

class OCRTestCase(unittest.TestCase):
    """Tests for `ocr.py."""

    def test_Name_and_Price(self):
   		a = "50 Marion 12.00 SALE"
		b = "2 books .00"
		c ="44 G1nger Lover $9.50"
		d = "Brown R1ce $2.00"
		e = "Iota] 2 item(s) $11.50"
		x = "Brown Rice 12.00"
		y = "Pad Thai 13"
		z = "Super awesome Indonesian mie tek tek $12.99"

		self.assertEqual("('50 Marion', '12.00')", get_name_and_price(a))
		self.assertEqual("None", get_name_and_price(b))
		self.assertEqual("('44 G1nger Lover', '9.50')", get_name_and_price(c))
		self.assertEqual("('Brown R1ce', '2.00')", get_name_and_price(d))
		self.assertEqual("('Iota] 2 item(s)', '11.50')", get_name_and_price(e))
		self.assertEqual("('Brown Rice', '12.00')", get_name_and_price(x))
		self.assertEqual("None", get_name_and_price(y))
		self.assertEqual("('Super awesome Indonesian mie tek tek', '12.99')", get_name_and_price(z))

if __name__ == '__main__':
    unittest.main()
