import math 

class product():
	'''
	
	Author: Joel Conley
	Mod date: May 13, 2019
	'''

	def __init__(self, department, productName, unitPrice, QTY, commissionRate):
		self.department = department
		self.productName = productName
		self.unitPrice = unitPrice
		self.QTY = QTY
		self.commissionRate = commissionRate

	def calculateCommission(self, unitPrice, QTY, commissionRate):
		commission = (self.unitPrice*self.QTY)*self.commissionRate
		return round(commission, 2)


