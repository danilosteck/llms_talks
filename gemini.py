# Ref: https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=pt-br

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from google.colab import userdata

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=userdata.get(cfg['api_keys']['gemini'])

# genai.configure(api_key=GOOGLE_API_KEY)

# ---------------

import requests
import json

# Configure sua chave de API da Gemini
api_key = 'sua-chave-de-api-gemini-aqui'
api_url = 'https://api.gemini.com/v1/completion'

# Função para gerar texto usando o Gemini
def gerar_texto_gemini(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 150  # Ajuste o número de tokens conforme necessário
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    return response_data['choices'][0]['text'].strip()

# Exemplo de uso
if __name__ == "__main__":
    prompt = "Escreva um poema sobre a natureza."
    texto_gerado = gerar_texto_gemini(prompt)
    print(texto_gerado)
