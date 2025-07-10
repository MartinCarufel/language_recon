from PIL import Image
from lingua import Language, LanguageDetectorBuilder

import pytesseract

languages = [Language.ENGLISH,
            Language.FRENCH,
            Language.GERMAN,
            Language.GREEK,
            Language.ITALIAN,
            Language.POLISH,
            Language.PORTUGUESE,
            Language.SPANISH,
            Language.RUSSIAN,
            Language.DANISH,
            ]

langs = ["eng", "fra", "deu", "grc", "ita", "pol", "por", "spa", "rus", "dan"]


for lang in langs:
    print(f"***************** {lang} START ***********************")
    text = pytesseract.image_to_string(Image.open('gr_case_man.png'), lang=lang)
    text_list = text.split(" ")
    text_list = [item for item in text_list if len(item) >= 3]
    print(text_list)

    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    confidence_values = detector.compute_language_confidence_values(text)
    # language = detector.detect_language_of(text)
    for confidence in confidence_values:
        # pass
        print(f"{confidence.language.name}: {confidence.value:.2f}")
    # for result in detector.detect_multiple_languages_of(text):
    #     print(f"{result.language.name}: '{text[result.start_index:result.end_index]}'")
    print(f"\n***************** {lang} END ***********************\n")

# print(language)


# text = "Aoyaptacpoi oSovtiatpwv"
# print(text)



""">>> from lingua import Language, LanguageDetectorBuilder
>>> languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
>>> detector = LanguageDetectorBuilder.from_languages(*languages).build()
>>> confidence_values = detector.compute_language_confidence_values("languages are awesome")
>>> for confidence in confidence_values:
...     print(f"{confidence.language.name}: {confidence.value:.2f}")"""