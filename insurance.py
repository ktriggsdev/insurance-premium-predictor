import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("Navigation", ["About", "Predict"])
df = pd.read_csv('csv/insurance.csv')

if nav == "About":
    st.title("Health Insurance Premium Predictor")
    st.text(" ")
    st.text(" ")
    st.image('images/health_insurance.jpeg', width=600)


df.replace({'gender':{'male':0, 'female':1, 'non-binary':2}}, inplace=True)


df.replace({'smoker':{'yes':0, 'no':1}}, inplace=True)

df.replace({'region':{'south east':0, 'south west':1, 'north east':2, 'east midlands':3, 'yorkshire':4, 'west midlands':5, 'east':6, 'north west':7, 'london':8, 'scotland':9, 'wales':10 }}, inplace=True)

x = df.drop(columns='charges', axis=1)

y = df['charges']

rfr = RandomForestRegressor()

rfr.fit(x, y)

if nav == 'Predict':
    st.title("Enter Details")
    
    age = st.number_input("Age: ", step=1, min_value=0)
    
    gender = st.radio("gender", ("male", "female", "non-binary"))
    
    if (gender == 'male'):
        g = 0
    if (gender == 'female'):
        g= 1
    if (gender == 'non-binary'):
        g= 2
    
    bmi = st.number_input("BMI: ", min_value=0)
    
    children = st.number_input("Number of children: ", step=1, min_value=0)
    
    smoke = st.radio("Do you smoke?", ("Yes", "No"))
    
    if (smoke == "Yes"):
        sm = 0
    if (smoke == "No"):
        sm = 1
        
    region = st.selectbox('Region', ('south east', 'south west', 'north east', 'east midlands', 'yorkshire', 'west midlands', 'east', 'north west', 'london', 'scotland', 'wales'))
    
    if (region == "south east"):
        reg = 0
    if (region == "south west"):
        reg = 1
    if (region == "north east"):
        reg = 2
    if (region == "east midlands"):
        reg = 3
    if (region == "yorkshire"):
        reg = 4
    if (region == "west midlands"):
        reg = 5
    if (region == "east"):
        reg = 6
    if (region == "north west"):
        reg = 7
    if (region == "london"):
        reg = 8
    if (region == "scotland"):
        reg = 9
    if (region == "wales"):
        reg = 10    
        
    if st.button("Predict"):
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age, g, bmi, children, sm, reg]]))