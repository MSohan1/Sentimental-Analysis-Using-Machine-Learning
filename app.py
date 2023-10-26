import streamlit as st
import joblib
st.title("SENTIMENTAL ANALYSIS")
reloaded_model = joblib.load('positive-negative')
input1 = st.text_input("Enter the Review")
output1=reloaded_model.predict([input1])
if st.button("PRIDTICTE"):
  op=['Neutral','Positive','Negative']
  st.title(op[output1[0]])
