from PIL import Image
from lingua import Language, LanguageDetectorBuilder
import pytesseract
import re

languages = [
    Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.GREEK,
    Language.ITALIAN, Language.POLISH, Language.PORTUGUESE, Language.SPANISH,
    Language.RUSSIAN, Language.DANISH,
]

langs = ["eng", "fra", "deu", "ell", "ita", "pol", "por", "spa", "rus", "dan"]

# Build Lingua detector once
detector = LanguageDetectorBuilder.from_languages(*languages).build()

# Load the image once
image = Image.open('2025-07-08_11-05-09.png')

for lingua_lang, tesseract_lang in zip(languages, langs):
    print(f"***************** {lingua_lang} START ***********************")

    # OCR with this language
    text = pytesseract.image_to_string(image, lang=tesseract_lang)
    # print(f"OCR text:\n{text}\n")

    # Clean and join the text
    text_list = re.split(r'[ \n]', text)
    text_list = [item for item in text_list if len(item) >= 3]
    clean_text = ' '.join(text_list)
    print(clean_text)

    # Now detect language confidence on the whole clean text
    confidence = detector.compute_language_confidence(clean_text, lingua_lang)

    print(f"Language: {lingua_lang}, Confidence: {confidence:.3f}")
    print(f"***************** {lingua_lang} END ***********************\n")
