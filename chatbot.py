from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from config import DEEPL_API_KEY

app = Flask(__name__)

# Idiomas soportados (códigos ISO)
LANGUAGES = {
    'es': 'Español',
    'en': 'Inglés',
    'de': 'Alemán',
    'ja': 'Japonés'
}

# Función de traducción (DeepL)
def translate_deepl(text, target_lang):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, data=params)
    return response.json()["translations"][0]["text"]


# Función DeepL
def translate(text, target_lang):
    return translate_deepl(text, target_lang) 


@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    user_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    
    # --- Mensaje de bienvenida ---
    if user_msg == 'hola' or user_msg == 'hi' or user_msg == 'start':
        welcome_msg = """
        ¡Hola! 👋 Soy *La IA de Miguel*, tu tutor de idiomas. 🌍
        
        Puedo ayudarte a practicar:
        - Español (escribe 'es')
        - Inglés (escribe 'en')
        - Alemán (escribe 'de')
        - Japonés (escribe 'ja')
        
        ¡Envía el código del idioma que quieres practicar!
        """
        resp.message(welcome_msg)
        return str(resp)

    # Comandos básicos
    if user_msg == 'holaa':
        reply = "¡Hola! 🌍 Elige un idioma para practicar:\n" + \
                "\n".join([f"- {name} (escribe '{code}')" for code, name in LANGUAGES.items()])
    
    elif user_msg in LANGUAGES:
        reply = f"✅ Modo {LANGUAGES[user_msg]} activado. ¡Envíame una frase y la traduciré!"
    
    else:
        # Traduce el mensaje a los 4 idiomas (ejemplo interactivo)
        translations = {lang: translate(user_msg, lang) for lang in LANGUAGES.keys()}
        reply = "🔍 Traducciones:\n" + \
                "\n".join([f"{LANGUAGES[lang]}: {text}" for lang, text in translations.items()])

    resp.message(reply)
    return str(resp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
