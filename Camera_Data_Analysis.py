# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:28:34 2022

@author: 91966
"""
#Problem Statements-
# A dataset of about 1000 cameras with 13 properties such as weight, focal 
# length, price, etc. Analyse data, remove null values and find insides.


#Required Libralies
import pandas as pd
import numpy as np


#Import Data sets
Camera_data = pd.read_csv(r"E:\MY TAB\Data Science\Python\PROJECT\Camera.csv")
Camera_data.shape  #(1038, 13)
Camera_data.columns

#Finding percentage of missing Values
Camera_data.isnull().sum()/len(Camera_data)*100

#Outoff 13 columns Storage included,Weight (inc. batteries),Dimensions have
# 12.04%, 2.21%, 1.54% missing values respectively.


#Summary of data in dataframe
summary_data = Camera_data.describe().T

# Replace Blank values by NUll.
Camera_data.replace(" ",np.NaN)

#Treament for Null Values
Camera_data.fillna(Camera_data.median(),inplace=True)

#Createing fuction for Discount:
def Discount(discount=5):
    Camera_data["Discount_Price"]=Camera_data["Price"]*(100-discount)/100
    return Camera_data["Discount_Price"]

Discount(2)
Camera_data.columns

#Droping Unimportant Columns
Camera_data.drop(['Macro focus range','Zoom tele (T)'],axis=1,inplace=True)


Camera_data['Model'].replace('Agfa ePhoto CL50','Agfa ePhoto CL250',inplace=True)


Camera_data.rename(columns={'Release date':'Release Year'},inplace=True)


max_price = Camera_data['Price'].max()
Camera_data[Camera_data['Price']==max_price]['Model']
#Models Canon EOS-1Ds, Canon EOS-1Ds Mark II, Canon EOS-1Ds Mark III has 
# Maximum Price.




min_price = Camera_data['Weight (inc. batteries)'].min()
Camera_data[Camera_data['Weight (inc. batteries)']==min_price]['Model']
#Model Casio Exilim EX-S20 has minimum price

Camera_data['Release Year'].value_counts()
#count of Year wise model release. 


# Extracting Columns 
Extract_Colomn = Camera_data[['Model','Storage included','Price','Discount_Price','Dimensions']]
Extract_Colomn


Model_05_06 = Camera_data[(Camera_data['Release Year']==2006)
                          | (Camera_data['Release Year']==2005)];Model_05_06
#Model Release in 2005 & 2006


Model_05 = Camera_data[Camera_data['Release Year']==2005]
Model_06 = Camera_data[Camera_data['Release Year']==2006]

Model_05_06 = Model_05.append(Model_06);Model_05_06
#Model Release in 2005 & 2006 ( Second Method )


Camera_data_2007 = Camera_data[Camera_data['Release Year']==2007]
max_price  = Camera_data_2007['Price'].max();max_price
min_price  = Camera_data_2007['Price'].min();min_price
# The model which release in 2007 has maximum price 7999 & minimum price 99.


expensive_cheapest_model = Camera_data_2007[(Camera_data_2007['Price']==max_price)
                         | (Camera_data_2007['Price']==min_price)][['Model','Price']]
expensive_cheapest_model

#model  Canon EOS-1Ds Mark III is most expensive model with price 7999
# and models Nikon Coolpix L10,Nikon Coolpix L11,Nikon Coolpix L12,Ricoh Caplio R6,
# Ricoh Caplio R7, Samsung L730,Samsung L830,Samsung S630,Samsung S830,
# Samsung S730,Samsung S830 are cheapest with price 99.
    

Model_Release = Camera_data.groupby(by=['Release Year'])['Model'].count()
Model_Release.max()

# In 2007 maximum number of model are released.






