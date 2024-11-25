import streamlit as st
import base64
import requests
import os
from connection import contract


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f"""<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf sandbox="allow-forms allow-pointer-lock allow-same-origin"></iframe>"""
    st.components.v1.html(pdf_display, height=1000)



def view_certificate(certificate_id):
    # Smart Contract Call
    result = contract.functions.getCertificate(certificate_id).call()
    ipfs_hash = result[4]

    pinata_gateway_base_url = 'https://gateway.pinata.cloud/ipfs'
    if not ipfs_hash:
            st.error("No IPFS hash found for this certificate.")
            return

        
    
    content_url = f"{pinata_gateway_base_url}/{ipfs_hash}"
    st.write(f"Fetching PDF from: {content_url}")  # Debugging lin
    response = requests.get(content_url)
    st.download_button(
            label="Download PDF",
            data=response.content,  # Use the PDF content directly for downloading
            file_name="certificate.pdf",  # Specify the filename for the download
            mime="application/pdf"  # Specify the MIME type
        )
    # st.write("Response status code:", response.status_code)
    # st.write("Content-Type:", response.headers.get("Content-Type"))
    # with open("temp.pdf", 'wb') as pdf_file:
    #     pdf_file.write(response.content)
    # displayPDF("temp.pdf")
    
    os.remove("temp.pdf")


def hide_icons():
    hide_st_style = """
				<style>
				#MainMenu {visibility: hidden;}
				footer {visibility: hidden;}
				</style>"""
    st.markdown(hide_st_style, unsafe_allow_html=True)


def hide_sidebar():
    no_sidebar_style = """
    			<style>
        		div[data-testid="stSidebarNav"] {visibility: hidden;}
    			</style>"""
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


def remove_whitespaces():
    st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>""", unsafe_allow_html=True)