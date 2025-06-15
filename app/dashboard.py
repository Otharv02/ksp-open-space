import streamlit as st
import os
import pandas as pd

# --- Streamlit Config ---
st.set_page_config(page_title="KSP OPEN SPACE", layout="wide")
st.sidebar.title("🛰 Kerbal Data Lab")
selection = st.sidebar.radio("Navigation", ["🏠 Home", "📊 Datasets", "👨‍🔬 Community", "📥 Contact"])

# --- Global Styles ---
st.markdown("""
    <style>
    body { background-color: #1b1b1b; color: #f5f5f5; }
    .block-container { padding-top: 2rem; }
    h1, h2, h3, h4, h5 { color: #39ff14; }
    .card { padding: 1rem; background-color: #2a2a2a; border-radius: 1rem; box-shadow: 0 2px 10px rgba(0,255,0,0.1); margin-bottom: 1rem; }
    a { color: #03dac6; }
    </style>
""", unsafe_allow_html=True)

# --- Dataset Descriptions & Metadata (can later be loaded from a JSON or CSV) ---
dataset_metadata = {
    "solid_vs_liquid.csv": {
        "description": "Thrust/temperature comparison between solid and liquid rocket motors on test stand.",
        "author": "Atharv Nawale"
    },
    "kerbin_orbit_telemetry.csv": {
        "description": "Telemetry of Kerbin satellite until battery failure at apoapsis.",
        "author": "Atharv Nawale"
    }
}

# --- Helper: List Available Datasets ---
def list_datasets():
    if not os.path.exists("datasets"):
        os.makedirs("datasets")
    files = os.listdir("datasets")
    return [f for f in files if f.endswith(".csv")]

# --- Pages ---
if selection == "🏠 Home":
    st.title("🚀 KSP OPEN SPACE")
    st.markdown("""
        ### Welcome Commander
        This is your gateway to Kerbal scientific data exchange.
        📊 View shared telemetry datasets, or contribute your own to the community.
    """)

elif selection == "📊 Datasets":
    st.title("📊 Datasets")
    dataset_list = list_datasets()

    if dataset_list:
        for dataset in dataset_list:
            description = dataset_metadata.get(dataset, {}).get("description", "No description available.")
            author = dataset_metadata.get(dataset, {}).get("author", "Unknown")

            cols = st.columns([3, 3, 2])
            with cols[0]:
                with open(f"datasets/{dataset}", "rb") as f:
                    st.download_button(
                        label=f"📥 {dataset}",
                        data=f,
                        file_name=dataset,
                        mime="text/csv"
                    )
            with cols[1]:
                st.markdown(f"*{description}*")
            with cols[2]:
                st.markdown(f"— by **{author}**")
    else:
        st.info("No datasets uploaded yet.")

elif selection == "👨‍🔬 Community":
    st.title("👨‍🔬 Community Dataset Links")
    st.markdown("Externally hosted datasets and Streamlit apps shared by the community.")

    # Example community links
    community_links = [
        {"title": "Minmus Spectral Analyzer", "url": "https://example.com/minmus", "author": "Atharv Nawale"},
        {"title": "Kerbin Weather Archive", "url": "https://example.com/kerbin", "author": "Alex Kerman"},
        {"title": "Eve Atmospheric Study", "url": "https://example.com/eve", "author": "Valentina K."}
    ]

    for item in community_links:
        cols = st.columns([3, 1])
        with cols[0]:
            st.markdown(f"[📄 {item['title']}]({item['url']})", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"— by **{item['author']}**")

elif selection == "📥 Contact":
    st.title("📥 Contact us for Dataset Uploads or Submissions")
    st.markdown("""
    ### 📧 Get in Touch

    If you'd like to:
    - 💡 Request a new dataset  
    - 🔗 Share your Streamlit app  
    - 📤 Submit telemetry or CSV data

    Please send an email to:

    **✉️ [atharvnawale969@gmail.com](mailto:atharvnawale969@gmail.com)**  

    Include:
    - Your name
    - Description of your dataset or app
    - Any links or files you'd like us to review

    ---
    We'll respond as soon as we review your submission.
    """)
