import streamlit as st
import pandas as pd

st.title("BMI calculator")

height=st.slider("enter your height(in cm )",100,250,175)
weight=st.slider("enter your weight (in kg)",40,200,70)


bmi=weight/((height/100)**2)

st.write(f" your BMI is {bmi:.2f}💪")

st.write("BMI categories")
st.write("under weight: BMI less than 18.5👍")
st.write("normal weight: BMI between 18.5 and 24.9👌")
st.write("over weight: BMI between 25 and 29.9👏")
st.write("obesity:BMI 30 or greater👍")
