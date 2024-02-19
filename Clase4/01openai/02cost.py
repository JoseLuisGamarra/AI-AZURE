import openai
import getpass

# Documentación - https://openai.com/pricing

openai.api_key = getpass.getpass("Ingresa tu API Key de OpenAI : ")
model_openai = "gpt-3.5-turbo"

def openai_api_calculate_cost(usage, model):

    pricing = {
        'gpt-3.5-turbo': {
            'prompt': 0.0015,
            'completion': 0.002
        },
        'gpt-3.5-turbo-16k': {
            'prompt': 0.003,
            'completion': 0.004
        },
        'gpt-4-8k': {
            'prompt': 0.03,
            'completion': 0.06
        },
        'gpt-4-32k': {
            'prompt': 0.06,
            'completion': 0.12
        },
        'text-embedding-ada-002-v2': {
            'prompt': 0.0001,
            'completion': 0.0001
        }
    }

    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Modelo inválido")

    prompt_cost = usage['prompt_tokens'] * model_pricing['prompt'] / 1000
    completion_cost = usage['completion_tokens'] * model_pricing['completion'] / 1000

    total_cost = prompt_cost + completion_cost
    print(f"\nTokens usados:  {usage['prompt_tokens']:,} prompt + {usage['completion_tokens']:,} completion = {usage['total_tokens']:,} tokens")
    print(f"Total costo ({model}): ${total_cost:4f}\n")

    return total_cost

# Define el mensaje de entrada para el chat
prompt = "dame el código para usar la API de OpenAI con Python"
message_input = {
    'messages': [
        {'role': 'system', 'content': 'Eres un asistente virtual'},
        {'role': 'user', 'content': prompt}
    ]
}

# Realiza una solicitud a la API de OpenAI
response = openai.ChatCompletion.create(
    model = model_openai,
    messages = message_input['messages'],
    temperature = 0, #Si está más cercano a 1, es posible que tenga alucinaciones.
    n = 1, #Número de respuestas
    max_tokens = 100
    )

# Imprime la respuesta del modelo
result = response['choices'][0]['message']['content']
print(result)

openai_api_calculate_cost(response["usage"], model_openai)