import streamlit as st
from features.page_remover import page_remover
from features.md_to_pdf import md_to_pdf
from features.page_adder import page_adder
from features.txt_to_pdf import txt_to_pdf

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
        "📋 Markdown → PDF",
        "📃 Riassumi PDF",
        "✈️ Traduci PDF",
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
    page_adder()
    
elif option == "📝 TXT → PDF":
    st.header("Converti file TXT in PDF")
    txt_to_pdf()
    
elif option == "📋 Markdown → PDF":
    st.header("Converti file Markdown in PDF")
    md_to_pdf()

elif option == "📃 Riassumi PDF":
    st.header("Riassumi un PDF")
    st.write("Funzionalità in arrivo...")

elif option == "✈️ Traduci PDF":
    st.header("Traduci un PDF")
    st.write("Funzionalità in arrivo...")