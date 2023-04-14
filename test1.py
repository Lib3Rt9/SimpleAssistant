import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

import openai
openai.api_key = secrets["api_key"]

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response['choices'][0]['text']

while True:
    prompt = input('User: ')
    response = generate_text(prompt)
    print(f'Assistant: {response}')