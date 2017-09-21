from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import json

'''
Using PhantomJs, fetch the page source after load is complete and then save the page source into gold_soup
which is ready for data retrival

Note: The local machines phantomjs directory should be replaced 
with the passing argument in webdriver.PhantomJS()
'''
gold_driver = webdriver.PhantomJS("LOCAL_PATH/phantomjs.exe")
gold_driver.get('https://www.investing.com/commodities/gold-historical-data')
gold_soup = BeautifulSoup(gold_driver.page_source,'html.parser') #page_source fetches page after rendering is complete
gold_driver.quit()


'''
Using PhantomJs, fetch the page source after load is complete and then save the page source into silver_soup
which is ready for data retrival.

Note: The local machines phantomjs directory should be replaced 
with the passing argument in webdriver.PhantomJS()
'''
silver_driver = webdriver.PhantomJS("LOCAL_PATH/phantomjs.exe")
silver_driver.get('https://www.investing.com/commodities/silver-historical-data')
silver_soup = BeautifulSoup(silver_driver.page_source,'html.parser') #page_source fetches page after rendering is complete
silver_driver.quit()


'''
Find the related table from gold page and fetch it's headers and the datas
g_header = contains all the headers of the tabel
g_data = contains all the data in the td elements
'''
g_table = gold_soup.find( "table", {"id":"curr_table"} )
rows = g_table.findAll('tr')
hrs = g_table.findAll('th')
g_headers = [th.findChildren(text=True) for th in hrs]
g_data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
# the first row is empty because it doesnt containg any tds.
del g_data[0]


'''
Find the related table from gold page and fetch it's headers and the datas
s_header = contains all the headers of the tabel
s_data = contains all the data in the td elements
'''
s_table = silver_soup.find( "table", {"id":"curr_table"} )
rows = s_table.findAll('tr')
hrs = s_table.findAll('th')
s_headers = [th.findChildren(text=True) for th in hrs]
s_data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
# the first row is empty because it doesnt containg any tds.
del s_data[0]



'''
Go through all the date values and chnnge them to the requested format namely: 
YYYY-MM-DD like: 2017-09-20
'''
for i in range(len(g_data)):
	g_data[i][0][0] = datetime.strptime(g_data[i][0][0], '%b %d, %Y').strftime('%Y-%m-%d')

'''
Go through all the date values and chnnge them to the requested format namely: 
YYYY-MM-DD like: 2017-09-20
'''
for i in range(len(s_data)):
	s_data[i][0][0] = datetime.strptime(s_data[i][0][0], '%b %d, %Y').strftime('%Y-%m-%d')


dic = {}
dic['gold']= {}
dic['silver'] = {}

'''
Go through all Gold data and add them to the dictionary with the key of gold
the key of each data is the date value. 
'''
for i in range(len(g_data)):
	dic['gold'][g_data[i][0][0]] = {}
	for j in range(len(g_data[i])):
		dic['gold'][g_data[i][0][0]][g_headers[j][0]]=g_data[i][j][0] 



'''
Go through all Silver data and add them to the dictionary with the key of silver
the key of each data is the date value. 
'''
for i in range(len(s_data)):
	dic['silver'][s_data[i][0][0]] = {}
	for j in range(len(s_data[i])):
		dic['silver'][s_data[i][0][0]][s_headers[j][0]]=s_data[i][j][0] 



'''
save the data into a json file under result.json

'''

with open('result.json', 'w') as fp:
	json.dump(dic, fp)


print("Congratulations, the date are fetched from the URLs. You can run now the getCommodityPrice.py")

