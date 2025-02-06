
# Online Python - IDE, Editor, Compiler, Interpre

import openai
import os

openai.api_type = "azure"
openai.api_base = "https://SEU_ENDPOINT.azure.com/"
openai.api_version = "2024-02-01"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

response = openai.ChatCompletion.create(
    engine="gpt-4",
    messages=[{"role": "user", "content": "Explique o que é o Semantic Kernel."}]
)

print(response["choices"][0]["message"]["content"])

