import quandl
import pandas as pd
import numpy as np
import datetime
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import input.correlation_input as prop

source=prop.source
destination=prop.destination
start_date=prop.start_date
end_date=prop.end_date
column=prop.column
delta=prop.delta
authtoken=prop.authtoken

def pearsonCorrelation(data1, data2):
	corr, _ = pearsonr(data1, data2)
	print('Pearsons correlation between datasets is : %.3f' % corr)

def spearmanCorrelation(data1, data2):
	corr, _ = spearmanr(data1, data2)
	print('Spearman correlation between datasets is: %.3f' % corr)

def find_all_dates(df):
	return [str(date_index.date()) for date_index in df.index.tolist()]

def return_dictonary(df):
	return { date: df.loc[date] for date in find_all_dates(df)}

def return_alldataInterpolated(dict,all_dates):
	return pd.Series([float(dict[date]) if date in dict else np.NaN for date in all_dates]).interpolate()

def listNormaliser(list1,delta):
	return [(list1[i]-list1[i+delta])/list1[i+delta] for i in range(0,len(list1)-delta)]
	 
print ('Correlation between '+source + ' and other destinations are listed below:\n')

df_source =quandl.get(source, start_date=start_date, end_date=end_date,authtoken=authtoken)[[column]]
all_dates=find_all_dates(df_source)
source_price=listNormaliser(df_source[column].tolist(),delta)

for d in destination:
	print (d +' and '+ source)
	df =quandl.get(d, start_date=start_date, end_date=end_date, authtoken=authtoken)[[column]]
	destination_price=listNormaliser(return_alldataInterpolated(return_dictonary(df),all_dates),delta)
	pearsonCorrelation(source_price,destination_price)
	spearmanCorrelation(source_price,destination_price)
	print('\n')
