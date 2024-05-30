import json
import os

# Função para ler um arquivo JSON e retornar como string
def ler_json_como_string(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo_json = json.load(arquivo)
        return conteudo_json
    except Exception as e:
        return str(e)

def config():
    config = ler_json_como_string(os.path.join('.','config.json'))
    return config

# Exemplo de uso
if __name__ == "__main__":
    caminho_arquivo = 'caminho/do/arquivo.json'  # Substitua pelo caminho do seu arquivo JSON
    conteudo_string = ler_json_como_string(caminho_arquivo)
    print(conteudo_string)
