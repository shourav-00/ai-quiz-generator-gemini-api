from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

load_dotenv()
api_key=os.environ.get("gemini_api_key")
print(api_key)
client = genai.Client(api_key=api_key)
def note_gen(img):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img,"here make summarize or need from the images and maintain professional and bold or note professional way within 100 words" ],
    )
    return response.text

def audio_gen(text):
    speech=gTTS(text,lang="en",slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_gen(img,difficulty):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img,f"Analyze the provided image(s) carefully and generate a professional quiz based on the content.Create exactly 3 questions for each image.Only one option should be correct.question create based on its {difficulty}.Each question must have exactly 4 multiple-choice options (A, B, C, D).After all questions, provide:Correct answers (clearly labeled).Brief explanations for each answer" ],
    )
    return response.text