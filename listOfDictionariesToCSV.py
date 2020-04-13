from datetime import datetime
import csv

# list to CSV
def listToCSV(inputList, recordName):
    # Last record for file name
    lastRecord = inputList[0]['rateDate'].strftime("%Y-%m-%d")
    
    fileName = '../Data-Collection/' + recordName + '/' + lastRecord + '-' + recordName + '.csv'

    with open(fileName, 'w', encoding='utf-8', newline='') as myfile:
        fc = csv.DictWriter(myfile, fieldnames=inputList[0].keys())
        fc.writeheader()
        fc.writerows(inputList)


# List of Dictionaries
rateList = [
  {'rateDate': datetime.date(datetime(2020, 3, 1)), 'rateVal': 1.93, 'publishDate': datetime.date(datetime(2020, 3, 26))}, 
  {'rateDate': datetime.date(datetime(2020, 2, 1)), 'rateVal': 21.32, 'publishDate': datetime.date(datetime(2020, 2, 27))}, 
  {'rateDate': datetime.date(datetime(2020, 1, 1)), 'rateVal': 21.34, 'publishDate': datetime.date(datetime(2020, 1, 30))}, 
  {'rateDate': datetime.date(datetime(2019, 12, 1)), 'rateVal': 6.96, 'publishDate': datetime.date(datetime(2019, 12, 26))}, 
  {'rateDate': datetime.date(datetime(2019, 11, 1)), 'rateVal': 6.95, 'publishDate': datetime.date(datetime(2019, 11, 28))}, 
  {'rateDate': datetime.date(datetime(2019, 10, 1)), 'rateVal': 6.99, 'publishDate': datetime.date(datetime(2019, 10, 31))}, 
  {'rateDate': datetime.date(datetime(2019, 9, 1)), 'rateVal': 21.31, 'publishDate': datetime.date(datetime(2019, 9, 26))}, 
  {'rateDate': datetime.date(datetime(2019, 8, 1)), 'rateVal': 21.35, 'publishDate': datetime.date(datetime(2019, 8, 29))}, 
  {'rateDate': datetime.date(datetime(2019, 7, 1)), 'rateVal': 4.0, 'publishDate': datetime.date(datetime(2019, 7, 25))}, 
  {'rateDate': datetime.date(datetime(2019, 6, 1)), 'rateVal': 13.96, 'publishDate': datetime.date(datetime(2019, 6, 27))}]

# Write List of Dictionaries to CSV 
listToCSV(rateList, 'InterestRate')


