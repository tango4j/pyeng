from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Translate this sentence into Korean: 'not having any success in this particular video.'"
)

print(response.output_text)