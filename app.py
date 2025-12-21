from numpy.random import default_rng as rng
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Sustainable Waste Management",
    page_icon="🌍",
    layout=None)




df = pd.read_csv('data.csv', parse_dates=['date'])


st.header("Sustainable Waste Management – Overflow Monitoring Dashboard")
st.markdown(
    "A dashboard for tracking **waste overflow problems**"
    "and assisting in waste management decision-making."
)

st.sidebar.header("Filters")

area_selected = st.sidebar.multiselect(
    "Select Area",
    options=df["area"].unique(),
    default=df["area"].unique()
)

date_range = st.sidebar.date_input(
    "Choose a date range",
    value=(df["date"].min().date(), df["date"].max().date())
)

# ---- Normalize date input ----
if isinstance(date_range, (list, tuple)):
    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range[0]
else:
    start_date = end_date = date_range

# Convert to pandas datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

df = df[
    (df["date"] >= start_date) &
    (df["date"] <= end_date)
]


total_overflow_days = df["overflow"].sum()
high_risk_areas = df.groupby("area")["overflow"].sum()
high_risk_areas = (high_risk_areas > 5).sum()

avg_ratio = (df["waste_kg"] / df["collection_capacity_kg"]).mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Overflow Days", int(total_overflow_days))
col2.metric("High Risk Areas", int(high_risk_areas))
col3.metric("Avg Waste / Capacity", f"{avg_ratio:.2f}")

area_df = (
    df[["date", "waste_kg", "collection_capacity_kg"]]
    .sort_values("date")
    .set_index("date")
)

st.subheader("📊 Waste vs Collection Capacity (Area View)")

st.area_chart(
    area_df,
    height=350
)

st.caption("Area chart highlights volume differences between waste and capacity.")

st.divider()

with st.expander("📂 View Raw Data"):
    st.dataframe(df)
#-----------------------------------
scatter_df = df[[
    "collection_capacity_kg",
    "waste_kg",
    "overflow"
]].copy()

# แปลง overflow เป็น label สำหรับสี
scatter_df["Status"] = scatter_df["overflow"].map({
    0: "Normal",
    1: "Overflow"
})

st.subheader("🚨 Overflow Risk Scatter Plot")

st.scatter_chart(
    data=scatter_df,
    x="collection_capacity_kg",
    y="waste_kg",
    color="Status",
    height=350
)




#-----------------------------------
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
pred_df = pd.DataFrame({
    "Actual Collection Capacity (kg)": Y_test,
    "Predicted Collection Capacity (kg)": Y_pred
})

st.subheader("Predicted vs Actual Collection Capacity")

st.scatter_chart(
    data=pred_df,
    x="Actual Collection Capacity (kg)",
    y="Predicted Collection Capacity (kg)"
)

st.caption(
    "This scatter plot compares the model's predicted collection capacity "
    "with actual values. Points closer to the diagonal indicate better prediction accuracy."
)


st.divider()


st.markdown("### Sponsors")

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    st.image("exxonmobil.png", width=100)
with s2:
    st.image("egat.png", width=100)
with s3:
    st.image("roza.png", width=85)
with s4:
    st.image("cute.png", width=100)
with s5:

    st.image("camphub.png", width=100)
