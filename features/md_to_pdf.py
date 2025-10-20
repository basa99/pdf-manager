import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def md_to_pdf():
    md_file = st.file_uploader("Carica un file Markdown", type=["md", "markdown"], key="md_file")
    
    if md_file:
        # Leggi il contenuto del file
        content = md_file.read().decode('utf-8')
        
        st.success(f"✅ File caricato: {md_file.name}")
        
        # Mostra anteprima del markdown renderizzato
        with st.expander("👁️ Anteprima del contenuto", True):
            st.markdown(content)
        
        # Opzioni di formattazione
        st.write("### Opzioni di formattazione")
        
        col1, col2 = st.columns(2)
        with col1:
            base_font_size = st.slider("Dimensione font base:", 8, 14, 11)
        with col2:
            line_spacing = st.slider("Interlinea:", 12, 20, 14)
        
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
                # Gestisci i vari elementi markdown
                font_name = "Helvetica"
                font_size = base_font_size
                is_bold = False
                
                # Intestazioni
                if line.startswith('# '):
                    line = line[2:]
                    font_size = base_font_size + 8
                    is_bold = True
                    y_position -= line_spacing  # Spazio extra prima
                elif line.startswith('## '):
                    line = line[3:]
                    font_size = base_font_size + 6
                    is_bold = True
                    y_position -= line_spacing * 0.5
                elif line.startswith('### '):
                    line = line[4:]
                    font_size = base_font_size + 4
                    is_bold = True
                elif line.startswith('#### '):
                    line = line[5:]
                    font_size = base_font_size + 2
                    is_bold = True
                
                # Lista puntata
                if line.startswith('- ') or line.startswith('* '):
                    line = "  • " + line[2:]
                
                # Lista numerata (semplificata)
                if len(line) > 2 and line[0].isdigit() and line[1:3] in ['. ', ') ']:
                    pass  # Mantieni il numero
                
                # Imposta il font
                if is_bold:
                    font_name = "Helvetica-Bold"
                
                # Se la riga è vuota, salta una riga
                if not line.strip():
                    y_position -= line_spacing * 0.5
                    continue
                
                # Gestisci il word wrapping
                words = line.split(' ')
                current_line = ""
                
                for word in words:
                    test_line = current_line + word + " "
                    if c.stringWidth(test_line, font_name, font_size) < max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            c.setFont(font_name, font_size)
                            c.drawString(margin_x, y_position, current_line.strip())
                            y_position -= line_spacing
                            
                            if y_position < margin_y:
                                c.showPage()
                                y_position = height - margin_y
                        
                        current_line = word + " "
                
                # Scrivi l'ultima parte della riga
                if current_line:
                    c.setFont(font_name, font_size)
                    c.drawString(margin_x, y_position, current_line.strip())
                    y_position -= line_spacing
                    
                    # Spazio extra dopo le intestazioni
                    if is_bold:
                        y_position -= line_spacing * 0.3
                
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
                file_name=f"{md_file.name.replace('.md', '').replace('.markdown', '')}.pdf",
                mime="application/pdf"
            )