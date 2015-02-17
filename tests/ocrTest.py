import unittest
import sys
sys.path.append("../app/")
#import app
from ocr import *

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

"""#EVERYTHING BELOW IS ONLY FOR TESTING
a = "50 Marion 12.00 SALE"
b = "2 books .00"
c ="44 G1nger Lover $9.50"
d = "Brown R1ce $2.00"
e = "Iota] 2 item(s) $11.50"
x = "Brown Rice 12.00"
y = "Pad Thai 13"
z = "Super awesome Indonesian mie tek tek $12.99"
print get_name_and_price(a)
print get_name_and_price(b)
print get_name_and_price(c)
print get_name_and_price(d)
print get_name_and_price(e)

print get_name_and_price(x)
print get_name_and_price(y)
print get_name_and_price(z)

stuff = file_to_string("images/restaurant.png")
print stuff
x = (collect_names_prices(stuff))
print "Printing all that are collected"
print x
for name in x:
    print (name, x[name])"""

if __name__ == '__main__':
    unittest.main()
