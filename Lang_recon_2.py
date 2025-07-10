from PIL import Image
import pytesseract
from langdetect import detect

def detect_image_language(image_path):
    image = Image.open("2025-07-08_11-05-09.png")
    # Try OCR with Greek and English models
    text = pytesseract.image_to_string(image, lang='bul+zho+dan+nld+eng+fra+ell+ita+nob+pol+por+rus+spa')
    print("Extracted Text:\n", text)
    try:
        lang = detect(text)
    except:
        lang = "unknown"
    return lang

lang_code = detect_image_language("your_image.png")
print(f"Detected language: {lang_code}")