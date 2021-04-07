import gspread

class Sheet:
	def __init__ (self, key = "1VWHYDY7ez4LZBhXageGVdyrCWN4z5C748bMrV8wkvbg"):
		self.gc = gspread.service_account("credentials.json")
		self.sheet = self.gc.open_by_key (key).sheet1
	
	def addLine (self, time, username, price = None, details = 1.0):
		self.nextcol = self.sheet.find ("next").row
		self.sheet.update (f"A{self.nextcol + 1}", "next")
		if price == None: self.previousPrice = self.sheet.get (f"C{self.nextcol - 1}")
		
		#self.sheet.batch_update ([{'range' : f'A{self.nextcol}:C{self.nextcol}', 'values' : [[time, username, self.previousPrice]]}])
		self.sheet.update (f"A{self.nextcol}", time)#When
		self.sheet.update (f"B{self.nextcol}", username)#Who
		self.sheet.update (f"C{self.nextcol}", self.previousPrice)#Ammount
		self.sheet.update (f"D{self.nextcol}", details)#Importance


if __name__ == "__main__":
	Sheet ().addLine ("sss", "user")