import streamlit as st
import PyPDF2

def main():
    st.title("PDF Reader App")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        st.write("**Uploaded File:**", uploaded_file.name)
        text = read_pdf(uploaded_file)
        st.text_area("PDF Content:", text, height=300)


def read_pdf(uploaded_file):
    pdfReader = PyPDF2.PdfFileReader(uploaded_file)
    text = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        text += pageObj.extractText()
    return text

if __name__ == "__main__":
    main()
