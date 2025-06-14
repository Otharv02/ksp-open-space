import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI config
st.set_page_config(page_title="KSP OPEN SPACE", layout="wide")
st.sidebar.title("🛰 Kerbal Mission Control")
selection = st.sidebar.radio("Navigation", ["🏠 Home", "📡 Missions", "👨‍🔬 Community", "📥 Request / Submit"])

# Global styles
st.markdown("""
    <style>
    body { background-color: #1b1b1b; color: #f5f5f5; }
    .block-container { padding-top: 2rem; }
    h1, h2, h3, h4, h5 { color: #39ff14; }
    .card { padding: 1rem; background-color: #2a2a2a; border-radius: 1rem; box-shadow: 0 2px 10px rgba(0,255,0,0.1); margin-bottom: 1rem; }
    a { color: #03dac6; }
    </style>
""", unsafe_allow_html=True)

# Mission-specific content (to simulate from code)
mission_info = {
    "Kerbnik-1 Solar Dive": {
        "status": "Complete",
        "date": "2025-06-14",
        "summary": "Recorded extreme solar proximity telemetry.",
        "details": "Probe reached perihelion of 3 million km before systems failed. Temperature sensors maxed out."
    },
    "GeoSat-2": {
        "status": "Live",
        "date": "2025-06-13",
        "summary": "Monitoring equatorial region with hullcam. Updated hourly.",
        "details": "Geosynchronous imagery archive enabled. Atmospheric haze level tracking in progress."
    }
}

if selection == "🏠 Home":
    st.title("🚀 KSP OPEN SPACE")
    st.markdown("""
        ### Welcome Commander
        This is your gateway to the Kerbal scientific network.
        🌌 Browse missions, access shared data, or propose something wildly ill-advised.
    """)

elif selection == "📡 Missions":
    st.title("📡 Active Missions & Satellites")
    for name, mission in mission_info.items():
        with st.container():
            st.markdown(f"""
            <div class='card'>
                <h3>{name} ({mission['status']})</h3>
                <p><strong>Date:</strong> {mission['date']}</p>
                <p>{mission['summary']}</p>
                <details><summary>🔍 Details</summary>
                <p>{mission['details']}</p>
                </details>
            </div>
            """, unsafe_allow_html=True)

elif selection == "👨‍🔬 Community":
    st.title("👨‍🔬 Community Mission Links")
    st.write("External missions shared by other users. Verified and indexed by KerbalNet Admins.")
    st.markdown("""
    - [Solar Relay Explorer](https://example-solar-relay.streamlit.app) - Orbiting the sun at 0.2 AU
    - [Minmus Crater SensorNet](https://example-minmus-base.streamlit.app) - Ground array deployed near the Greater Flats
    - [Mun ComNet Expansion](https://example-mun-net.streamlit.app) - Polar relay with intermittent signals
    """)

elif selection == "📥 Request / Submit":
    st.title("📥 Submit Link / Request a Mission")
    option = st.radio("Choose an action", ["💡 Request a Mission Idea", "🔗 Submit Your Streamlit URL"])

    if option == "💡 Request a Mission Idea":
        request_text = st.text_area("Describe your mission idea or ask for a specific satellite to be added")
        if st.button("Submit Request"):
            st.success("Mission request submitted! We'll review it soon.")

    if option == "🔗 Submit Your Streamlit URL":
        mission_name = st.text_input("Mission Name")
        mission_url = st.text_input("Streamlit App URL")
        mission_desc = st.text_area("Brief Description")
        if st.button("Submit URL"):
            st.success("URL received! We'll verify and list it on the Community page.")
