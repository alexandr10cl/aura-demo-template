# services/openai_service.py

import os
from openai import OpenAI

# 1. O cliente da OpenAI é inicializado aqui.
# Ele automaticamente busca a chave da API da variável de ambiente OPENAI_API_KEY.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# COMO USAR:
#
# Para criar uma função que usa a IA, importe o 'client' deste arquivo.
# Exemplo de uma função de chat que você pode criar em outro lugar ou aqui mesmo:
#
# def gerar_resposta_chat(mensagem_usuario):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",  # ou o modelo que preferir
#             messages=[
#                 {"role": "system", "content": "Você é um assistente prestativo."},
#                 {"role": "user", "content": mensagem_usuario}
#             ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         print(f"Ocorreu um erro ao chamar a API da OpenAI: {e}")
#         return "Desculpe, não consegui processar sua solicitação no momento."
#