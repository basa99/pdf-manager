import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

def page_adder():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 PDF Principale")
        main_pdf = st.file_uploader("Carica il PDF principale", type="pdf", key="main_pdf")
        
    with col2:
        st.subheader("📎 PDF da Aggiungere")
        add_pdf = st.file_uploader("Carica il PDF da aggiungere", type="pdf", key="add_pdf")
    
    if main_pdf and add_pdf:
        # Leggi entrambi i PDF
        main_reader = PdfReader(main_pdf)
        add_reader = PdfReader(add_pdf)
        
        main_pages = len(main_reader.pages)
        add_pages = len(add_reader.pages)
        
        st.success(f"✅ PDF principale: {main_pages} pagine | PDF da aggiungere: {add_pages} pagine")
        
        st.write("### Dove vuoi inserire le nuove pagine?")
        
        position = st.radio(
            "Posizione:",
            ["All'inizio", "Alla fine", "In una posizione specifica"],
            horizontal=True
        )
        
        insert_at = 0
        if position == "All'inizio":
            insert_at = 0
        elif position == "Alla fine":
            insert_at = main_pages
        else:
            insert_at = st.number_input(
                "Inserisci dopo la pagina:",
                min_value=0,
                max_value=main_pages,
                value=0,
                help=f"0 = all'inizio, {main_pages} = alla fine"
            )
        
        if st.button("Unisci i PDF", type="primary"):
            pdf_writer = PdfWriter()
            
            # Aggiungi le pagine del PDF principale fino al punto di inserimento
            for i in range(insert_at):
                pdf_writer.add_page(main_reader.pages[i])
            
            # Aggiungi tutte le pagine del PDF da inserire
            for page in add_reader.pages:
                pdf_writer.add_page(page)
            
            # Aggiungi le pagine rimanenti del PDF principale
            for i in range(insert_at, main_pages):
                pdf_writer.add_page(main_reader.pages[i])
            
            # Salva in memoria
            output = io.BytesIO()
            pdf_writer.write(output)
            output.seek(0)
            
            total_final_pages = len(pdf_writer.pages)
            st.success(f"PDF uniti con successo! Totale pagine: {total_final_pages}")
            
            # Bottone per scaricare
            st.download_button(
                label="📥 Scarica PDF unificato",
                data=output,
                file_name="pdf_unificato.pdf",
                mime="application/pdf"
            )