\# Messy Document Extractor



A structured information extraction system that extracts important fields from messy invoice documents.



\## Project Objective



The goal of this project is to extract structured information from invoices even when the document format is inconsistent or messy.



\## Fields Extracted



The system extracts 8 fields:



\- Invoice Number

\- Invoice Date

\- Vendor Name

\- Customer Name

\- Subtotal

\- Tax Amount

\- Total Amount

\- Due Date



\## Features



\- Extracts multiple invoice fields automatically

\- Handles different invoice formats

\- Provides a confidence score

\- Detects missing fields

\- Detects duplicate fields

\- Does not guess missing information

\- Evaluates extraction performance using labelled documents

\- Includes a Streamlit web interface



\## Dataset



A dataset of 50 hand-labelled invoice documents is used for evaluation.



Each document contains ground-truth values for the required invoice fields.



\## Missing and Duplicate Field Handling



If a field is missing, the system returns `None` instead of guessing a value.



If a field appears multiple times, the system reports the duplicate occurrences and uses the first detected value.



\## Evaluation



The project evaluates extraction performance across all 8 fields using 50 labelled documents.



The evaluation report contains:



\- Total documents evaluated

\- Total fields evaluated

\- Overall field accuracy

\- Per-field accuracy



See `evaluation\_report.txt` for the evaluation results.



\## Project Files



| File | Description |

|---|---|

| `extractor.py` | Main information extraction logic |

| `create\_dataset.py` | Creates the labelled invoice dataset |

| `evaluate.py` | Evaluates extraction performance |

| `evaluation\_report.py` | Generates evaluation report |

| `evaluation\_report.txt` | Evaluation results |

| `app.py` | Streamlit web application |

| `requirements.txt` | Required Python package |

| `data/invoices.csv` | Labelled invoice dataset |



\## How to Run



Install the required package:



```bash

pip install -r requirements.txt

