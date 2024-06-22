from googletrans import Translator, LANGUAGES

def translate_text(text, dest_lang='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def print_supported_languages():
    print("Supported Languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

if __name__ == "__main__":
    print_supported_languages()
    while 1>0:
        text_to_translate = input("Enter text to translate and Enter 0 to Stop Execution: ")
        if text_to_translate=='0':
            break
        dest_language = input("Enter destination language code (e.g., en for English): ")
        
        translated_text = translate_text(text_to_translate, dest_language)
        print(f"\nOriginal Text: {text_to_translate}")
        print(f"Translated Text: {translated_text}")