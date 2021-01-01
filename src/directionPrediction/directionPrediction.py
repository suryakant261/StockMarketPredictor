import csv
import pandas as pd
import numpy as np
from sklearn import svm
import numpy as np
from numpy.random import randn
from numpy.random import seed
import properties as prop
import quandl

delta=prop.delta
target_index=prop.target_index
dependency=prop.dependency
authtoken=prop.authtoken
start_date=prop.start_date
end_date=prop.end_date
column=prop.column
train_ratio=prop.train_ratio

def find_all_dates(df):
	return [str(date_index.date()) for date_index in df.index.tolist()]


def return_dictonary(df):
	return { date: df.loc[date] for date in find_all_dates(df)}

def return_alldataInterpolated(dict,all_dates):
	return pd.Series([float(dict[date]) if date in dict else np.NaN for date in all_dates]).interpolate()

def listNormaliser(list1,delta):
	return [(list1[i]-list1[i+delta])/list1[i+delta] for i in range(0,len(list1)-delta)]

df_source =quandl.get(target_index, start_date=start_date, end_date=end_date,authtoken=authtoken)[[column]]
print 'ABCD'
print df_source
print 'ABCD'
all_dates=find_all_dates(df_source)
source_price=listNormaliser(df_source[column].tolist(),delta)
source_label= list(map(lambda x: 1 if x >0 else 0, source_price))
X1=[]

for d in dependency:
	df =quandl.get(d, start_date=start_date, end_date=end_date, authtoken=authtoken)[[column]]
	X1.append(listNormaliser(return_alldataInterpolated(return_dictonary(df),all_dates),delta))

train_cases=int(len(all_dates)*train_ratio)
test_cases=len(all_dates) - train_cases
X= np.array([list(a) for a in list(zip(*X1))][:train_cases])
y= source_label[:train_cases]

# print(X)
# print (y)
clf = svm.SVC( C = 20.0)
clf.fit(X, y)  
predicted_indicator=clf.predict([list(a) for a in list(zip(*X1))][train_cases:])

accuracy_percentage = sum(list(map(lambda x :1 if x[0]==x[1] else 0,zip(predicted_indicator,source_label[train_cases:]))))/test_cases*100
print ('Accuracy of the model is :' +str(accuracy_percentage))
