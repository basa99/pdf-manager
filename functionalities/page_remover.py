import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

def page_remover():
    uploaded_file = st.file_uploader("Carica un file PDF", type="pdf", key="remove_pages")
    
    if uploaded_file:
        # Leggi il PDF
        pdf_reader = PdfReader(uploaded_file)
        total_pages = len(pdf_reader.pages)
        
        st.success(f"PDF caricato con successo! Numero totale di pagine: {total_pages}")
        
        # Mostra le pagine disponibili
        st.write("### Seleziona l'intervallo di pagine da ELIMINARE")
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_page = st.number_input(
                "Da pagina (compresa):",
                min_value=1,
                max_value=total_pages,
                value=1,
                step=1
            )
        
        with col2:
            end_page = st.number_input(
                "A pagina (compresa):",
                min_value=1,
                max_value=total_pages,
                value=1,
                step=1
            )
        
        # Validazione
        if start_page > end_page:
            st.error("⚠️ La pagina di inizio deve essere minore o uguale alla pagina di fine!")
        else:
            pages_to_remove = list(range(start_page, end_page + 1))
            st.info(f"Verranno eliminate {len(pages_to_remove)} pagina/e: da {start_page} a {end_page}")
        
        if st.button("Rimuovi pagine selezionate", type="primary"):
            if not pages_to_remove:
                st.warning("Seleziona almeno una pagina da eliminare!")
            elif len(pages_to_remove) >= total_pages:
                st.error("Non puoi eliminare tutte le pagine!")
            else:
                # Crea un nuovo PDF senza le pagine selezionate
                pdf_writer = PdfWriter()
                
                for page_num in range(total_pages):
                    if (page_num + 1) not in pages_to_remove:
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                
                # Salva in memoria
                output = io.BytesIO()
                pdf_writer.write(output)
                output.seek(0)
                
                st.success(f"Pagine rimosse con successo! Nuovo PDF con {len(pdf_writer.pages)} pagine")
                
                # Bottone per scaricare
                st.download_button(
                    label="📥 Scarica PDF modificato",
                    data=output,
                    file_name="pdf_senza_pagine.pdf",
                    mime="application/pdf"
                )