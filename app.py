from numpy.random import default_rng as rng
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Streamlit with ML",
    page_icon="🕹️",
    layout=None)

df = pd.read_csv('data.csv', parse_dates=['date'])


st.header("Sustainable waste management prediction 2024")
st.write("Raw data")
st.dataframe(df)

selected_features = ['population', 'waste_kg', 'organic_kg', 'recyclable_kg','is_weekend', 'overflow', 'is_holiday', 'is_weekend',  'recycling_campaign', 'temp_c', 'rain_mm']
X = df[selected_features]
y = df['collection_capacity_kg']

df_combined = pd.concat([X, y], axis=1)
df_combined.dropna(inplace=True)

X = df_combined[selected_features]
y = df_combined['collection_capacity_kg']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

st.write("MSE: ", mean_squared_error(Y_test, Y_pred))
st.write("R squared: ", r2_score(Y_test, Y_pred))

# พล็อตกราฟเปรียบเทียบ

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(Y_test, Y_pred, alpha=0.7)
ax.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='red', lw=2, label='Perfect Prediction Line')
ax.set_xlabel('Actual Sustain (Y_test)')
ax.set_ylabel('Predicted Collection capacity kg (Y_pred)')
ax.set_title('Predicted')
ax.legend()
ax.grid(True)

st.pyplot(fig)

df = pd.DataFrame({
    "Actual Dollar Price (Y_test)": Y_test,
    "Predicted Dollar Price (Y_pred)": Y_pred
})

st.header("Predicted vs. Actual Dollar Price")
st.scatter_chart(
    data=df,
    x="Actual Dollar Price (Y_test)",
    y="Predicted Dollar Price (Y_pred)"
)