import streamlit as st
from langchain.chat_models import ChatOpenAI
from PIL import Image

st.set_page_config(page_title = "Chatbot usando Langchain, OpenAI y Streamlit", page_icon = "https://python.langchain.com/img/favicon.ico")

with st.sidebar:

    st.title("Usando la API de OpenAI con Streamlit y Langchain")

    model = st.selectbox('Eliga el modelo',
        (
            'gpt-3.5-turbo', 
            'gpt-3.5-turbo-16k', 
            'gpt-4'
        ), 
        key = "model"
    )

    image = Image.open('logos.png')
    st.image(image, caption = 'OpenAI, Langchain y Streamlit')

    st.markdown(
        """
        Integrando OpenAI con Streamlit y Langchain.
    """
    )

def clear_chat_history():
    st.session_state.messages = [{"role" : "assistant", "content": msg_chatbot}]

openai_api_key = st.sidebar.text_input("Ingrese tu API Key de OpenAI y dale Enter para habilitar el chatbot", key = "chatbot_api_key", type = "password")
st.sidebar.button('Limpiar historial de chat', on_click = clear_chat_history)

msg_chatbot = """
        Soy un chatbot que está integrado a la API de OpenAI: 

        ### Preguntas frecuentes
        
        - ¿Quién eres?
        - ¿Cómo funcionas?
        - ¿Cuál es tu capacidad o límite de conocimientos?
        - ¿Puedes ayudarme con mi tarea/trabajo/estudio?
        - ¿Tienes emociones o conciencia?
        - Lo que desees
"""

## Se envía el prompt de usuario al modelo de GPT-3.5-Turbo para que devuelva una respuesta
def get_response_openai(prompt, model):
    
    llm = ChatOpenAI(
        openai_api_key = openai_api_key,
        model_name = model,
        temperature = 0
    )

    return llm.predict(prompt)

#Si no existe la variable messages, se crea la variable y se muestra por defecto el mensaje de bienvenida al chatbot.
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content" : msg_chatbot}]

# Muestra todos los mensajes de la conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if openai_api_key:

  prompt = st.chat_input("Ingresa tu pregunta")
  if prompt:
      st.session_state.messages.append({"role": "user", "content": prompt})
      with st.chat_message("user"):
          st.write(prompt)

  # Generar una nueva respuesta si el último mensaje no es de un assistant, sino de un user, entonces entra al bloque de código
  if st.session_state.messages[-1]["role"] != "assistant":
      with st.chat_message("assistant"):
          with st.spinner("Esperando respuesta, dame unos segundos."):
              
              response = get_response_openai(prompt, model)
              placeholder = st.empty()
              full_response = ''
              
              for item in response:
                  full_response += item
                  placeholder.markdown(full_response)

              placeholder.markdown(full_response)

      message = {"role" : "assistant", "content" : full_response}
      st.session_state.messages.append(message) #Agrega elemento a la caché de mensajes de chat.