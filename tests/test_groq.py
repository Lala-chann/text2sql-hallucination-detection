from groq import Groq
from app.config import settings


client = Groq(api_key=settings.GROQ_API_KEY)

try:
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[{"role": "user", "content": "Say 'hello' in one word."}]
        
    )
    print("Success:", response.choices[0].message.content)
except Exception as e:
    print("Error Type:", type(e).__name__)
    print("error Detail:", str(e))

    