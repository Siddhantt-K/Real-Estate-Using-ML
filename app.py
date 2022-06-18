# -*- coding: utf-8 -*-

import streamlit as st

import pandas as pd
import numpy as np
import pickle
import streamlit as st

load_model = open("D:/Softwares/DS/Project/RealEstate/Model/Banglore_Home_Prices_Model.pickle", 'rb')
regressor = pickle.load(load_model)


#dataFrameSerialization = "legacy"

#@st.cache(suppress_st_warning=True)
#def main():
#"""Home Price Prediction"""
st.title("Home Price Prediction App")
st.subheader("Please enter below entries to get yourself a suitable house: ")

area = pd.read_json("D:/Softwares/DS/Project/RealEstate/Model/Columns.json")
area1 = area.replace("'","")
loc = area1["data columns"].tolist()
#   area2 = list(area1.value_counts().index)

# Creating a function to predict a price
X = pd.DataFrame(columns= loc)
def predict_price(location, sqft, BHK, bath):
    loc_index = np.where(X.columns==location)[0][0]  
    
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = BHK
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    
    return regressor.predict([x])[0]

with st.form(key='my_form'):  
    location = st.selectbox('Location for the Property', (loc[3:]))
    total_sqft = st.number_input('Total Square Feet', 300, 10000,on_change=None)
    BHK = st.number_input('Total number of Bedrooms', 1, 10,on_change=None)
    bath = st.number_input('Total number of Washrooms', 1, 10,on_change=None)
    st.form_submit_button('Predict')
print(location)
print(total_sqft)
print(BHK)
print(bath)
pred = predict_price(location,total_sqft,BHK,bath)


if bath > BHK+1:
    st.subheader("Please enter valid no. of washrooms")

elif pred < 0:
    st.subheader('Please enter valid values')
else:
    st.subheader('Predicted price for your House is : '+str(round(pred,2))+' Lakhs')


   
    
    


