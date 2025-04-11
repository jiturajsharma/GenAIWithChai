from google import genai
from google.genai import types



client = genai.Client(api_key='Insert the api key here')

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Hey how are you doing today?'
)
print(response.text)