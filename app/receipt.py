"""A class for receipts"""
import json

class receipt(): 

	def __init__(self, file_path):
		self.receipt = file_path
		self.userID = ""
		self.transactionID = ""
		self.vendor = ""
		self.date = ""
		self.totalCost = "" 
		self.items = {}

	""" @param item 
		@param cost 
		@return boolean"""
	def addItem(self, item, cost):
		self.items[item] = cost
		return True

	"""Method to validate file path"""

	"""Method to validate userID"""

	"""Method to validate a transactionID""" 