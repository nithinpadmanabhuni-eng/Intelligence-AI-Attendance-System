import streamlit as st


def subject_card(
    name,
    code,
    section,
    stats=None,
    footer_callback=None
):

    # Construct complete HTML string
    html = f"""
    <div style="
        border-left: 8px solid #EB459E;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #000000;
        margin-bottom: 20px;
        background-color: #ffffff;
        font-family: sans-serif;
    ">
        <h3 style="font-size: 1.5rem; margin: 0 0 10px 0;">{name}</h3>

        <p style="color: #64748b; margin: 10px 0;">
            Code :
            <span style="
                background: #E0E3FF;
                color: #5865F2;
                padding: 2px 8px;
                border-radius: 5px;
            ">{code}</span>
            | Section : {section}
        </p>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px;">'
        for icon, label, value in stats:
            html += f'<div style="background: #EB459E10; padding: 5px 12px; border-radius: 12px; font-size: 0.9rem;">{icon} <b>{value}</b> {label}</div>'
        html += '</div>'

    html += '</div>'

    # Render HTML directly using st.html
    st.html(html)

    if footer_callback:
        footer_callback()