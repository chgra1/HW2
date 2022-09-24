import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import plotly.express as px
iris_data = load_iris()
labels = iris_data.feature_names
targets = iris_data.target
print(labels)
df_form = pd.DataFrame(iris_data.data, columns = labels)
df_form['targets'] = targets
st.write("""
# Iris Dataset
How are petal length and width correlated with speal length and width
""")
fig= px.scatter_3d(df_form, "sepal width (cm)", "sepal length (cm)", "petal length (cm)", "petal width (cm)")
fig.show()

