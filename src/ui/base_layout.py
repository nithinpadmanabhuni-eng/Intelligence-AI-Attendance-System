import streamlit as st

def style_background_home():

    st.markdown("""
        <style>

            /* ---------- Animated aurora background ---------- */
            .stApp {
                background: linear-gradient(160deg, #2A31A6 0%, #5865F2 55%, #7983F5 100%) !important;
            }

            /* drifting colour blobs */
            .stApp::before {
                content: "";
                position: fixed;
                inset: 0;
                z-index: 0;
                pointer-events: none;
                background:
                    radial-gradient(circle at 20% 25%, rgba(235,69,158,0.55) 0, transparent 38%),
                    radial-gradient(circle at 80% 20%, rgba(254,231,92,0.35) 0, transparent 32%),
                    radial-gradient(circle at 70% 85%, rgba(87,242,135,0.30) 0, transparent 34%),
                    radial-gradient(circle at 15% 85%, rgba(224,227,255,0.40) 0, transparent 36%);
                background-size: 140% 140%;
                filter: blur(40px);
                animation: aurora 18s ease-in-out infinite alternate;
            }

            /* subtle dot grid on top of the aurora */
            .stApp::after {
                content: "";
                position: fixed;
                inset: 0;
                z-index: 0;
                pointer-events: none;
                background-image: radial-gradient(rgba(255,255,255,0.22) 1.2px, transparent 1.2px);
                background-size: 28px 28px;
                -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 80%);
                mask-image: radial-gradient(ellipse at center, black 30%, transparent 80%);
            }

            @keyframes aurora {
                0%   { background-position: 0% 0%;     transform: scale(1); }
                50%  { background-position: 100% 40%;  transform: scale(1.08); }
                100% { background-position: 40% 100%;  transform: scale(1); }
            }

            /* keep real content above the background layers */
            [data-testid="stAppViewContainer"] {
                position: relative;
                z-index: 1;
            }

            /* ---------- Glass cards ---------- */
            .stApp div[data-testid="stColumn"] {
                background: rgba(255,255,255,0.14) !important;
                backdrop-filter: blur(18px) saturate(160%);
                -webkit-backdrop-filter: blur(18px) saturate(160%);
                border: 1px solid rgba(255,255,255,0.40);
                box-shadow: 0 20px 60px rgba(20,24,90,0.35),
                            inset 0 1px 0 rgba(255,255,255,0.45);
                padding: 2.5rem !important;
                border-radius: 5rem !important;
                transition: transform 0.35s ease, box-shadow 0.35s ease, background 0.35s ease;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-10px);
                background: rgba(255,255,255,0.22) !important;
                box-shadow: 0 30px 80px rgba(20,24,90,0.45),
                            0 0 0 2px rgba(255,255,255,0.35),
                            inset 0 1px 0 rgba(255,255,255,0.55);
            }

            .stApp div[data-testid="stColumn"] h2 {
                color: #ffffff !important;
                text-shadow: 0 4px 18px rgba(20,24,90,0.35);
            }

            /* mascots float gently */
            .stApp div[data-testid="stColumn"] [data-testid="stImage"] img {
                filter: drop-shadow(0 14px 18px rgba(20,24,90,0.35));
                animation: floaty 4.5s ease-in-out infinite;
            }
            @keyframes floaty {
                0%, 100% { transform: translateY(0); }
                50%      { transform: translateY(-8px); }
            }

            /* glowing white pill buttons inside the cards */
            .stApp div[data-testid="stColumn"] button {
                background: #ffffff !important;
                color: #5865F2 !important;
                font-weight: 600 !important;
                box-shadow: 0 8px 24px rgba(20,24,90,0.30);
                transition: transform 0.25s ease, box-shadow 0.25s ease !important;
            }
            .stApp div[data-testid="stColumn"] button p {
                color: #5865F2 !important;
            }
            .stApp div[data-testid="stColumn"] button:hover {
                transform: scale(1.08);
                box-shadow: 0 0 0 4px rgba(255,255,255,0.35),
                            0 12px 32px rgba(235,69,158,0.55);
            }

            @media (prefers-reduced-motion: reduce) {
                .stApp::before,
                .stApp div[data-testid="stColumn"] [data-testid="stImage"] img {
                    animation: none !important;
                }
            }

        </style>
        """,
        unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background: #E0E3FF !important;
            }

        </style>
    """, unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }

        </style>
    """, unsafe_allow_html=True)
