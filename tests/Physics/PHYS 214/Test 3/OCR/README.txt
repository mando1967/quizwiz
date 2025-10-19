OCR Pipeline (Local Use)

This folder contains two ways to OCR the exported key page images (from key_pages_export.zip):

Option A — Python + pytesseract
--------------------------------
Requirements:
- Python 3.9+
- Tesseract OCR engine installed on your system and in PATH
  * macOS (brew):   brew install tesseract
  * Ubuntu/Debian:  sudo apt-get update && sudo apt-get install -y tesseract-ocr
  * Windows:        Install from https://github.com/UB-Mannheim/tesseract/wiki  (then add to PATH)

Python packages:
- pip install pillow pytesseract

Run:
1) Unzip key_pages_export.zip to a folder, e.g. key_pages_export/
2) python ocr_images_to_md.py --images-dir key_pages_export --out-dir ocr_text --lang eng
   (Add -l eng+equ if you installed the 'equ' model for math.)

What it does:
- OCRs each PNG into text
- Groups pages by original PDF stem (e.g., Quiz 3 (S19) KEY_p1.png -> Quiz 3 (S19) KEY)
- Produces one Markdown file per key with page-separated sections
- Normalizes simple math notation to TeX where safe (10^-5 -> 10^{ -5 } etc. kept minimal)

Option B — Tesseract CLI only
------------------------------
1) Unzip key_pages_export.zip to key_pages_export/
2) Run for each image:
   tesseract "key_pages_export/Quiz 3 (S19) KEY_p1.png" "out/Quiz_3_S19_KEY_p1" -l eng --psm 6
3) Concatenate the outputs for each key into a Markdown:
   cat out/Quiz_3_S19_KEY_*.txt > "Quiz 3 (S19) KEY (OCR).md"

Tip:
- For math-heavy pages, try page segmentation --psm 6 or 4, and consider installing models like 'equ' or 'math' if available.
- After OCR, you can send me the .txt/.md files and I’ll merge the official answers into the Markdown keys.

