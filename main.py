import streamlit as st
from modules.processor import process_data

# Set up the page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar for Filters
st.sidebar.header("Filters")

time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)
# Load and process the data
df = process_data()

# Restrict the dataframe based on the selected time range
if time_range == "Last 7 Days":
    df_filtered = df.sort_values('Date', ascending=False).head(7)
elif time_range == "Last 30 Days":
    df_filtered = df.sort_values('Date', ascending=False).head(30)
else:
    df_filtered = df  # Use the full dataframe for 'All Time'

# Create a 3-column layout
col1, col2, col3 = st.columns(3)

# Calculate metrics from the filtered data
average_steps = df_filtered['Steps'].mean()
average_sleep_hours = df_filtered['Sleep_Hours'].mean()
average_recovery_score = df_filtered['Recovery_score'].mean()

# Display metrics in each column
col1.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)
col2.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)
col3.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# Add a clean and modern layout
st.markdown("## Overview")  # Subheading for the overview section

# Show the processed DataFrame in a wide mode
st.dataframe(df, width=1500, height=600)

# Add more sections and visualizations if necessary
# st.markdown("## Additional Metrics")
# st.metric(label="Example Metric", value="123", delta="10%")

st.markdown("---")

# Add footer
st.markdown("### Powered by FitSync - Your health, understood.")