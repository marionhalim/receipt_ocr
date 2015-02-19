import unittest
import sys
sys.path.append("../app/")
sys.path.append("../images/")
#import app
from ocr import *

"""Tests for ocr.py."""

FILE_PATH = "/Users/jchen/Documents/workspace/receipt_ocr/images"

class OCRTestCase(unittest.TestCase):

	"""Tests the collect names and prices method. Uses restaurant.png"""
	def test_collect_names_prices_1(self):
		print("Testing collecting names and prices from restaurant.png")
		print("-----------------------")
		receipt_file = file_to_string(FILE_PATH + "/restaurant.png")
		receipt = (collect_names_prices(receipt_file))
		self.assertEqual('2.00', receipt['Brown R1ce'])
		self.assertEqual('9.50', receipt['44 G1nger Lover'])

	"""Tests and name and prices method"""
	def test_Name_and_Price(self):
   		test1 = "50 Marion 12.00 SALE"
		test2 = "2 books .00"
		test3 = "44 G1nger Lover $9.50"
		test4 = "Brown R1ce $2.00"
		test5 = "Iota] 2 item(s) $11.50"
		test6 = "Brown Rice 12.00"
		test7 = "Pad Thai 13"
		test8 = "Super awesome Indonesian mie tek tek $12.99"

		print("Testing Name and Price")
		print("-----------------------")
		self.assertEqual("('50 Marion', '12.00')", str(get_name_and_price(test1)))		
		self.assertEqual("None", str(get_name_and_price(test2)))
		self.assertEqual("('44 G1nger Lover', '9.50')", str(get_name_and_price(test3)))
		self.assertEqual("('Brown R1ce', '2.00')", str(get_name_and_price(test4)))
		self.assertEqual("('Iota] 2 item(s)', '11.50')", str(get_name_and_price(test5)))
		self.assertEqual("('Brown Rice', '12.00')", str(get_name_and_price(test6)))
		self.assertEqual("None", str(get_name_and_price(test7)))
		self.assertEqual("('Super awesome Indonesian mie tek tek', '12.99')", str(get_name_and_price(test8)))

if __name__ == '__main__':
    unittest.main()
