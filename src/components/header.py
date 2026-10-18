import streamlit as st

def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <style>
            @keyframes logoFloat {{
                0%, 100% {{ transform: translateY(0) rotate(-3deg); }}
                50%      {{ transform: translateY(-10px) rotate(3deg); }}
            }}
            .snap-logo {{
                height: 100px;
                filter: drop-shadow(0 0 28px rgba(254,231,92,0.65));
                animation: logoFloat 5s ease-in-out infinite;
            }}
            .snap-title {{
                text-align: center;
                color: #ffffff;
                text-shadow: 0 6px 28px rgba(20,24,90,0.45);
                letter-spacing: 2px;
            }}
            @media (prefers-reduced-motion: reduce) {{
                .snap-logo {{ animation: none; }}
            }}
        </style>
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img class="snap-logo" src="{logo_url}" />
            <h1 class="snap-title">SNAP<br/>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src="{logo_url}" style="height:85px;" />
            <h2 style="text-align:left; color:#5865F2">SNAP<br/>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)
