# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:45:42 2022

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

load_model=pickle.load(open("https://github.com/naidusaladi/streamletapp/blob/main/diabetes_model_streamlit.sav",'rb'))

def diabetes_prediction(input_data):
    

    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    #standardize the input data
    std_data=input_data_reshaped
    #print(std_data)
    #print(std_data)
    prediction=load_model.predict(std_data)
    #print(prediction)
    if(prediction[0]):
      return "diabatic"
    else:
      return "Non diabatic"

def main():
    st.title('Diabetes Prediction')
    Pregnancie=st.text_input("Number of Pregnancies")
    Glucose=st.text_input("Number of Glucose")
    BloodPressure=st.text_input("Number of BP")
    SkinThickness=st.text_input("Number of SkinThickness")
    Insulin=st.text_input("Number of Insulin")
    BMI=st.text_input("Number of BMI")
    DiabetesPedigreeFunction=st.text_input("Number of DPF")
    Age=st.text_input("Number of Age")
    diagnosis=""
    
    if(st.button("Go for Test")):
        diagnosis=diabetes_prediction([Pregnancie,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)

if __name__=="__main__":
    main()
