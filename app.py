import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Conveyor Monitor",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Smart Conveyor Predictive Maintenance")
st.write("Monitor conveyor controller health and identify abnormal conditions.")

st.sidebar.header("Sensor Readings")

temperature = st.sidebar.slider(
    "Temperature (°C)", 20, 100, 40
)
current = st.sidebar.slider(
    "Current (A)", 0.0, 10.0, 2.0, 0.1
)
voltage_ripple = st.sidebar.slider(
    "Voltage Ripple (V)", 0.0, 5.0, 0.5, 0.1
)

if temperature >= 75 or current >= 7 or voltage_ripple >= 2.5:
    status = "WARNING"
    st.error("Abnormal readings detected. Inspect the controller.")
elif temperature >= 60 or current >= 5 or voltage_ripple >= 1.5:
    status = "CAUTION"
    st.warning("Readings are rising. Maintenance inspection is recommended.")
else:
    status = "NORMAL"
    st.success("Controller readings are within the demo limits.")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f"{temperature} °C")
col2.metric("Current", f"{current:.1f} A")
col3.metric("Voltage Ripple", f"{voltage_ripple:.1f} V")

st.subheader("Controller Health Status")
st.write(f"### {status}")

data = pd.DataFrame({
    "Parameter": ["Temperature", "Current", "Voltage Ripple"],
    "Reading": [temperature, current, voltage_ripple]
})

st.subheader("Sensor Readings Chart")
st.bar_chart(data.set_index("Parameter"))

st.info(
    "Demo prototype: readings are simulated using sliders. "
    "Thresholds are illustrative and must be calibrated for real equipment."
)
