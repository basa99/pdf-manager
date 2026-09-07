# 📄 PDF Manager

Applicazione web basata su [Streamlit](https://streamlit.io/) per gestire e generare file PDF direttamente dal browser.

## Funzionalità

- 🗑️ **Rimuovi pagine** — elimina un intervallo di pagine da un PDF
- ➕ **Aggiungi pagine** — unisce due PDF inserendo il secondo in una posizione a scelta del primo
- 📝 **TXT → PDF** — converte un file di testo in PDF con font e interlinea configurabili
- 📋 **Markdown → PDF** — converte un file Markdown in PDF, con supporto base per titoli e liste
- 📃 **Riassumi PDF** — *in arrivo*
- ✈️ **Traduci PDF** — *in arrivo*

## Requisiti

- Python >= 3.14

## Installazione

### Con `uv` (consigliato, usa `pyproject.toml`/`uv.lock`)

```bash
uv sync
```

### Con `pip`

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Avvio dell'applicazione

```bash
streamlit run pdf_manager.py
```

L'app sarà disponibile su [http://localhost:8501](http://localhost:8501).

## Struttura del progetto

```
pdf-manager/
├── pdf_manager.py        # Entry point dell'app Streamlit
├── features/              # Singole funzionalità dell'app
│   ├── page_remover.py
│   ├── page_adder.py
│   ├── txt_to_pdf.py
│   └── md_to_pdf.py
├── src/pdf_manager/        # Package installabile (entry point CLI)
├── requirements.txt
└── pyproject.toml
```
