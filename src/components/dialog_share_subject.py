import streamlit as st

import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):

    # Retrieve host dynamically (e.g., "your-app-name.streamlit.app" or "localhost:8501")
    host = st.context.headers.get("Host", "localhost:8501")
    
    # Construct full URL with protocol
    join_url = f"https://{host}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy this link to share on Whatsapp or Email")

    with col2:
        st.markdown("### Scan to Join")
        st.image(
            out.getvalue(),
            caption="QRCODE for class joining"
        )
