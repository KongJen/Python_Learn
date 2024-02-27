import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from dateutil import rrule
# set a date range of the data from Jan 1, 2019 to today
start_date = datetime(2019,1,1)
end_date   = datetime(2019,6,30)
days_diff = (end_date - start_date).days
NUM_POINTS = 30
random.seed(25)
# create a DataFrame of example data
data = pd.DataFrame()
for i in range(NUM_POINTS):
    this_date = start_date + \
        timedelta(days=random.randint(0,days_diff))    
    data = data.append({'date':this_date,'value': 'test'}, 
                       ignore_index=True)
# add columns for week and year of the date
data['date_week'] = data['date'].apply(lambda x: x.isocalendar()[1])
data['date_year'] = data['date'].apply(lambda x: x.isocalendar()[0])