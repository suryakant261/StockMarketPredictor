# StockMarketPredictor
Predict movement direction of a share


High level componenets:

1. Data Fetcher: Data can be fetched via API and dumped in tabular structure. Output will be in stock_market/stock_name/daterange_currentdate
2. Data Transformer/ Featurizer : It will do the filtering , interpolation, other data enrichment, calculation of derived fields, reading multiple data and joins and date ranges. Test Train split
3. ML model, BackTesting, and other offline testing : Run the suitable ML algorithm



Low level details :

1. Data Fetcher
Support fetch data from API and write to a systematic folder structure ( at path  stock_market/stock_name/daterange_currentdate , data should be in tabular format CSV)
Download data from internet sources and store at correct location
     2. Data Transformer/ Featurizer
Read multiple data, stock data and other indexes data
Join multiple data on date column
Fill in the missing values
Calculate derived features
Select only required columns
Split the data into train and test
    3. ML model
Read the training and test files
EDA of features, feature importance , feature correlation
Calculate precision /accuracy on test data
Tune the hyperparameters to achieve maximum accuracy
Measure more offline parameters like profit booked, risks associated



