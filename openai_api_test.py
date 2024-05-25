from openai import OpenAI
from config import OPEN_AI_KEY

client = OpenAI(api_key=OPEN_AI_KEY)

response = client.completions.create(
    model="babbage-002",
    prompt="How to use the OpenAI API",
    max_tokens=50
)

print(response.choices[0].text.strip())

