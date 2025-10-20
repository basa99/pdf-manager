import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import markdown2
import io
from functionalities.page_remover import page_remover

# Configurazione della pagina
st.set_page_config(
    page_title="PDF Manager",
    page_icon="📄",
    layout="wide"
)

# Titolo principale
st.title("📄 PDF Manager")
st.markdown("---")

# Sidebar con le opzioni
st.sidebar.title("Funzionalità")
option = st.sidebar.radio(
    "Scegli un'operazione:",
    [
        "🗑️ Rimuovi pagine",
        "➕ Aggiungi pagine",
        "📝 TXT → PDF",
        "📋 Markdown → PDF"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Seleziona un'operazione dal menu per iniziare")

# Area principale
if option == "🗑️ Rimuovi pagine":
    st.header("Rimuovi pagine da un PDF")
    page_remover()
    
elif option == "➕ Aggiungi pagine":
    st.header("Aggiungi pagine a un PDF")
    st.write("Funzionalità in arrivo...")
    
elif option == "📝 TXT → PDF":
    st.header("Converti file TXT in PDF")
    st.write("Funzionalità in arrivo...")
    
elif option == "📋 Markdown → PDF":
    st.header("Converti file Markdown in PDF")
    st.write("Funzionalità in arrivo...")