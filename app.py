import streamlit as st
from extractor import extract_invoice

st.set_page_config(
    page_title="Messy Document Extractor",
    page_icon="📄"
)

st.title("📄 Messy Document Information Extractor")

st.write(
    "Enter messy invoice text below. "
    "The system extracts structured information without guessing missing values."
)

text = st.text_area(
    "Paste invoice text here:",
    height=200,
    placeholder="Example: ABC Electronics Pvt Ltd Invoice No: INV-1025..."
)

if st.button("Extract Information"):

    if not text.strip():
        st.warning("Please enter some invoice text.")

    else:
        result, confidence = extract_invoice(text)

        st.subheader("Extracted Information")

        for field, value in result.items():

            if value is None:
                st.write(f"**{field}:** Not found")
            else:
                st.write(f"**{field}:** {value}")

        st.subheader("Confidence")

        st.progress(confidence)

        st.write(f"Confidence Score: **{confidence * 100:.0f}%**")

        missing = [
            field for field, value in result.items()
            if value is None
        ]

        if missing:
            st.warning(
                "Missing fields: " + ", ".join(missing)
            )
        else:
            st.success("All fields were extracted successfully.")