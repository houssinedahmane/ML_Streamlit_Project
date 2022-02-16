import streamlit as stl
import numpy as np 
from sklearn import datasets


stl.title("Simple Machine learning Application")

stl.write("""
# Hello Everyone
""")

data_name = stl.sidebar.selectbox("select Dataset", ("diabetes" , "Iris" , "Wine Dasaset"))

Classifier_= stl.sidebar.selectbox("Select Classifier " , ("KNN","Decision Tree","Random Forest"))

def data_get(data_name):
    if data_name == "diabetes":
        data = datasets.load_diabetes()
    elif data_name == "Iris":
        data = datasets.load_iris()
    else:
        data = datasets.load_wine()
    X = data.data
    y = data.target
    return X,y
X,y = data_get(data_name)
stl.write("Data Shape : " , X.shape)
stl.write("Number of Classes : " , len(np.unique(y)))

