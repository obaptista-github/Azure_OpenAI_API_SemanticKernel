
# Online Python - IDE, Editor, Compiler, Interpre

from semantic_kernel import Kernel

kernel = Kernel()
kernel.add_text_completion_service("gpt-4", "https://SEU_ENDPOINT.azure.com/", "AZURE_OPENAI_KEY")

prompt = "Liste três vantagens do Azure OpenAI."
response = kernel.run(prompt)

print(response)
