# Language Learning Chatbot 🧠🌍

A multilingual chatbot built with **Python**, **Flask**, **Twilio API**, and **DeepL API** to help users practice languages through WhatsApp.


## 🔧 Technologies Used
- Python 3
- Flask (Web server)
- Twilio API (WhatsApp integration)
- DeepL API (Translation)
- RESTful requests


## 📌 Features
- Users can interact with the bot via WhatsApp.
- Supports four languages: **Spanish, English, German, Japanese**.
- Translates any user message into all selected languages in real time.
- Simple command system (`es`, `en`, `de`, `ja`) to activate language practice mode.
- Friendly welcome message and dynamic responses.


## 🧠 How It Works
- Flask handles incoming POST requests from Twilio.
- User messages are parsed and sent to the DeepL API for translation.
- The bot returns the translations using Twilio’s messaging response.
  

## 🗂 Example Usage
**User:** `hola`  
**Bot:** *(Welcome message + language options)*

**User:** `en`  
**Bot:** `✅ English mode activated. Send me a phrase and I'll translate it!`

**User:** `¿Cómo estás?`  
**Bot:**  

🔍 Translations:
Español: ¿Cómo estás?
English: How are you?
German: Wie geht es dir?
Japanese: お元気ですか？


## ⚙️ Setup Instructions
1. Clone this repository:
```bash
git clone https://github.com/yourusername/language-learning-chatbot.git
cd language-learning-chatbot

2. Install dependencies:
pip install -r requirements.txt

3. Add your DEEPL_API_KEY in a file called config.py:
# config.py
DEEPL_API_KEY = "your_deepl_api_key_here"

4. Run the Flask app:
python chatbot.py
Make sure you configure Twilio to point to your /whatsapp route.

📫 Contact
Created by Jose Miguel Alba – LinkedIn
Feel free to connect or reach out!



