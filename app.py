
import streamlit as st
import psutil
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Cloud Server Monitor",
    page_icon="🖥️",
    layout="wide"
)

st.title("Cloud Server Monitoring Dashboard")
st.caption("Live system monitoring with historical graphs")

# Store recent measurements for this browser session
if "history" not in st.session_state:
    st.session_state.history = []

# Automatically refresh every 5 seconds
@st.fragment(run_every="5s")
def monitor():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    now = datetime.now()

    # Save the latest measurement
    st.session_state.history.append({
        "Time": now,
        "CPU": cpu,
        "RAM": ram,
        "Disk": disk
    })

    # Keep only the most recent 60 measurements
    st.session_state.history = (
        st.session_state.history[-60:]
    )

    # Display current usage
    col1, col2, col3 = st.columns(3)

    col1.metric("CPU Usage", f"{cpu:.1f}%")
    col2.metric("RAM Usage", f"{ram:.1f}%")
    col3.metric("Disk Usage", f"{disk:.1f}%")

    st.subheader("Resource Usage")

    st.write("CPU")
    st.progress(cpu / 100)

    st.write("RAM")
    st.progress(ram / 100)

    st.write("Disk")
    st.progress(disk / 100)

    # Historical graphs
    st.subheader("Historical Resource Monitoring")

    df = pd.DataFrame(st.session_state.history)
    df = df.set_index("Time")

    st.line_chart(
        df[["CPU", "RAM", "Disk"]],
        y_label="Usage (%)"
    )

    st.caption(
        "Showing the latest 60 measurements"
    )

    # Warning alerts
    st.subheader("System Alerts")

    if cpu >= 80:
        st.error("High CPU usage detected!")

    if ram >= 85:
        st.warning("High RAM usage detected!")

    if disk >= 90:
        st.error("Disk storage is almost full!")

    if cpu < 80 and ram < 85 and disk < 90:
        st.success("All resources are within thresholds.")

    st.caption(
        f"Last updated: {now:%H:%M:%S}"
    )

monitor()
