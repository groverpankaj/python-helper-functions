# Finds the last Thursday of a given month and year
# This function can be modified to calculate any day of the last week 
# by changing the value of weekday in condition of the while loop.


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def lastThursday(inputDate):
  
  # convert to datetime with format 2019-12-01
  inputDt = datetime.strptime(inputDate, '%B %Y').date()

  # Last day of month - Add one month, then subract one day
  nextMonthDate = inputDt + relativedelta(months = +1)
  lastDayOfMonth = nextMonthDate - timedelta(days=1)

  # initial
  lastThursday = lastDayOfMonth 

  # Value of Monday is 0, Sunday is 6 so Thursday will be 3 
  # subract one day till Thursday
  while (lastThursday.weekday() != 3):
      lastThursday = lastThursday - timedelta(days=1)

  return(lastThursday)



givenDate = 'December 2019'

# 2019-12-26
print('Last Thursday of' , givenDate, 'is on' , lastThursday(givenDate))

input('\nAll is Well :)')

