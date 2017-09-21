# Commodity Price
In this project, I want to analyze the Gold and Silver prices, and calculate the mean and the variance for a specific period of time. For doing so I have fetched the data from the following links:

https://www.investing.com/commodities/silver-historical-data


https://www.investing.com/commodities/gold-historical-data

# Requirenments:
In order to run the scripts, you would need the following libraries and programming languages. By clicking on each item,
you can find some helpful tips about installing each libraries, especialy if you use Anaconda.

  * Python 3.6.1 or above

  * [Numpy](https://anaconda.org/anaconda/numpy)

  * [Selenium](https://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python)

  * [BeautifulSoup](https://anaconda.org/anaconda/beautifulsoup4)

  * [PhantomJs](https://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python)


# Note:
When you finished installing all the dependencies, you also need to replace 2 lines of codes in the fetchData.py file. We need
to replace the driver path for the phantomJs to our local machines path.

`gold_driver = webdriver.PhantomJS("LOCAL_PATH/phantomjs.exe")`

`silver_driver = webdriver.PhantomJS("LOCAL_PATH/phantomjs.exe")`

# How to run:

1. run the `fetchData.py` in your command line. If it was successfull, it will prompt a congratulation message.

2. run the `getCommodityPrice` in your command line following by three arguments.

   2.1 Startign Date (YYYY-MM-DD)

   2.2 Ending Date (YYYY-MM-DD)

   2.3 Commodity ("gold" or "silver)
   
(e.g. `python getCommodityPrice.py 2017-08-25 2017-09-20 gold`)
