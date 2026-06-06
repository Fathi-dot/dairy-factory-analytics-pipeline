import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/processed/ai4i_processed.csv")
total_records = len(df)

failures = df["Machine failure"].sum()

failure_rate = (
    failures / total_records
) * 100

st.title("Factory Analytics Dashboard")

st.write("Første 5 rækker")

st.dataframe(df.head())

st.metric(
    "Failure Rate",
    f"{failure_rate:.2f}%"
)
total_records = len(df)

failures = df["Machine failure"].sum()

avg_torque = round(df["Torque"].mean(), 2)

failure_rate = (
    failures / total_records
) * 100
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Records",
    total_records
)

col2.metric(
    "Failures",
    failures
)

col3.metric(
    "Failure Rate",
    f"{failure_rate:.2f}%"
)

col4.metric(
    "Avg Torque",
    avg_torque
)
failure_by_type = (
    df.groupby("Type")["Machine failure"]
      .sum()
      .reset_index()
)

fig = px.bar(
    failure_by_type,
    x="Type",
    y="Machine failure",
    title="Machine Failures by Type"
)

st.plotly_chart(fig)

wear_by_type = (
    df.groupby("Type")["Tool wear"]
      .mean()
      .reset_index()
)

fig = px.bar(
    wear_by_type,
    x="Type",
    y="Tool wear",
    title="Average Tool Wear by Type"
)

st.plotly_chart(fig)
fig = px.histogram(
    df,
    x="Torque",
    title="Torque Distribution"
)

st.plotly_chart(fig)
fig = px.histogram(
    df,
    x="temperature_difference",
    title="Temperature Difference Distribution"
)

st.plotly_chart(fig)
