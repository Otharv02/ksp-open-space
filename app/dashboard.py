import streamlit as st
import os
import pandas as pd

# --- Streamlit Config ---
st.set_page_config(page_title="KSP OPEN SPACE", layout="wide")
st.sidebar.title("🛰 Kerbal Data Lab")
selection = st.sidebar.radio("Navigation", ["🏠 Home", "📊 Datasets", "👨‍🔬 Community", "🖼 Gallery", "📥 Contact"])

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

# --- Dataset Descriptions ---
dataset_metadata = {
    "kerbnik_1_telemetry.csv": {
        "description": "Telemetry of Kerbin satellite until battery failure at apoapsis.",
        "author": "Atharv Nawale"
    },
    "BACC_thumper_static_test_data.csv": {
        "description": "Static fire data for BACC 'Thumper' solid rocket booster.",
        "author": "Atharv Nawale"
    },
    "RT_05_flea_static_test_data.csv": {
        "description": "Performance test data for RT-05 'Flea' booster on launchpad.",
        "author": "Atharv Nawale"
    },
    "RT_10_hammer_static_test_data.csv": {
        "description": "Static test of the RT-10 'Hammer'.",
        "author": "Atharv Nawale"
    },
    "S1_SRB_KD25k_Kickback__static_test_data.csv": {
        "description": "Static test of the Kickback SRB (KD25k) with telemetry logging.",
        "author": "Atharv Nawale"
    }
}


# --- Helper: List Available Datasets ---
def list_datasets():
    if not os.path.exists("datasets"):
        os.makedirs("datasets")
    files = os.listdir("datasets")
    return [f for f in files if f.endswith(".csv")]

# --- Home Page ---
if selection == "🏠 Home":
    st.title("KSP OPEN SPACE")
    st.markdown("""
        ### Welcome  
        *"Research is what I'm doing when I don't know what I'm doing."*  
        — *Werhner Von Kerman*  
        
        (*[**r/KerbalSpaceProgram**](https://www.reddit.com/r/KerbalSpaceProgram/s/anUFzd9AvS))
        
        ---

        **KSP Open Space** is a community hub for spaceflight experiments, data sharing, and mission documentation within the Kerbal universe.

        #### What you can do here:
        - **View & download mission datasets**: Access telemetry from satellites, rockets, and experiments.
        - **Explore community missions**: Discover Streamlit apps and projects from other Kerbonauts.
        - **Submit ideas or data**: Share your CSV files or links to your own mission dashboards.
        - **Learn from failures and triumphs**: From catastrophic launch explosions to flawless orbital insertions.

        #### 📥 Want to contribute?
        You can email your datasets or apps to be featured in our community:
        **✉️ atharvnawale969@gmail.com**

        Let’s keep exploring — for science, curiosity, and the occasional explosion.
    """)

# --- Datasets Page ---
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

# --- Community Page ---
elif selection == "👨‍🔬 Community":
    st.title("👨‍🔬 Community Streamlit Links")
    st.markdown("Externally hosted datasets and Streamlit apps shared by the community.")

    community_links = [
        {"title": "Kerbnik-1 Mission Telemetry Analysis", "url": "https://kerbnik-1.streamlit.app/", "author": "Soham Kokate"}
        # {"title": "Kerbin Weather Archive", "url": "https://example.com/kerbin", "author": "Alex Kerman"},
        # {"title": "Eve Atmospheric Study", "url": "https://example.com/eve", "author": "Valentina K."}
    ]

    for item in community_links:
        cols = st.columns([3, 1])
        with cols[0]:
            st.markdown(f"[📄 {item['title']}]({item['url']})", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"— by **{item['author']}**")

# --- Gallery Page (View Only) ---
# --- Gallery Page (View Only) ---
elif selection == "🖼 Gallery":
    st.title("🖼 Mission Image Gallery")

    gallery_dir = "gallery"
    os.makedirs(gallery_dir, exist_ok=True)


    image_files = [img for img in os.listdir(gallery_dir) if img.lower().endswith((".png", ".jpg", ".jpeg"))]

    if image_files:
        st.subheader("🔭 Gallery")
        cols = st.columns(3)
        for i, img_file in enumerate(image_files):
            img_path = os.path.join(gallery_dir, img_file)
            with cols[i % 3]:
                st.image(img_path, use_container_width=True)  # Updated
    else:
        st.info("No images in the gallery yet. Check back soon!")


# --- Contact Page ---
elif selection == "📥 Contact":
    st.title("📥 Contact us for Submissions")
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
