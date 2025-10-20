import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def txt_to_pdf():
    txt_file = st.file_uploader("Carica un file TXT", type="txt", key="txt_file")
    
    if txt_file:
        # Leggi il contenuto del file
        content = txt_file.read().decode('utf-8')
        
        st.success(f"✅ File caricato: {txt_file.name}")
        
        # Mostra anteprima
        with st.expander("👁️ Anteprima del contenuto", True):
            st.markdown(content)
        
        # Opzioni di formattazione
        st.write("### Opzioni di formattazione")
        
        col1, col2 = st.columns(2)
        with col1:
            font_size = st.slider("Dimensione font:", 8, 16, 12)
        with col2:
            line_spacing = st.slider("Interlinea:", 12, 24, 16)
        
        if st.button("Converti in PDF", type="primary"):
            # Crea il PDF
            output = io.BytesIO()
            c = canvas.Canvas(output, pagesize=A4)
            width, height = A4
            
            # Margini
            margin_x = 50
            margin_y = 50
            max_width = width - 2 * margin_x
            
            # Posizione iniziale
            y_position = height - margin_y
            
            # Dividi il testo in righe
            lines = content.split('\n')
            
            for line in lines:
                # Se la riga è troppo lunga, spezzala
                words = line.split(' ')
                current_line = ""
                
                for word in words:
                    test_line = current_line + word + " "
                    # Stima approssimativa della larghezza
                    if c.stringWidth(test_line, "Helvetica", font_size) < max_width:
                        current_line = test_line
                    else:
                        # Scrivi la riga corrente e iniziane una nuova
                        if current_line:
                            c.setFont("Helvetica", font_size)
                            c.drawString(margin_x, y_position, current_line.strip())
                            y_position -= line_spacing
                            
                            # Se siamo alla fine della pagina, creane una nuova
                            if y_position < margin_y:
                                c.showPage()
                                y_position = height - margin_y
                        
                        current_line = word + " "
                
                # Scrivi l'ultima parte della riga
                if current_line:
                    c.setFont("Helvetica", font_size)
                    c.drawString(margin_x, y_position, current_line.strip())
                    y_position -= line_spacing
                else:
                    # Riga vuota
                    y_position -= line_spacing
                
                # Se siamo alla fine della pagina, creane una nuova
                if y_position < margin_y:
                    c.showPage()
                    y_position = height - margin_y
            
            c.save()
            output.seek(0)
            
            st.success("✅ PDF creato con successo!")
            
            # Bottone per scaricare
            st.download_button(
                label="📥 Scarica PDF",
                data=output,
                file_name=f"{txt_file.name.replace('.txt', '')}.pdf",
                mime="application/pdf"
            )