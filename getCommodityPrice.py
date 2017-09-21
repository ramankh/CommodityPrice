import json
import numpy as np
import sys
from datetime import datetime

args = sys.argv
commodity = ""
starting = ""
ending = ""

'''
validate: validates whether if the entered date is in a right format

'''
def validate(date):
    try:
    	datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
    	raise ValueError("The dates should be in the following format: YYYY-MM-DD")

'''
argsValidate: validates if the entered arguments are valid entries
'''

def argsValidate(args):
	if len(args)!=4:
		raise AssertionError("The number of arguments sould be exactly 3.\n\n(Starting Date Ending Date Commodity Name)")
	validate(args[1])
	validate(args[2])
	if args[3] == "gold":
		pass
	elif args[3] == "silver":
		pass
	else:
		raise ValueError("The third argument must be either 'silver' or 'gold'")


argsValidate(sys.argv)






dic = {}
with open('result.json', 'r') as fp:
	dic = json.load(fp)

starting = args[1]
ending = args[2]
commodity = args[3]



'''
Final validation which happens after loading the dataset. Checks if the date range
entered by the user is a valid range base on the min and max dates in our records
'''

allKeys = [key for key in dic[commodity]]
maxDate = max(allKeys)
minDate = min(allKeys)
if maxDate<ending:
	raise ValueError("Sorry! My maximum date is "+maxDate)

if minDate>starting:
	raise ValueError("Sorry! My minimum date is "+minDate)




# find all keys exist in the range
keys = [key for key in dic[commodity] if (key<=ending and key>=starting) ]
# find all the prices for the selected dates
prices = [float(dic[commodity][x]["Price"].replace(',','')) for x in keys]

print(commodity, np.mean(prices), np.var(prices))

