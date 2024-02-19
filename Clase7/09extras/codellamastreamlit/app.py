import streamlit as st
import openai
import os
import getpass
#import replicate
from langchain.llms import Replicate
from PIL import Image

st.set_page_config(page_title = "Chatbot usando Code Llama", page_icon = "👨🏻‍💻")

with st.sidebar:

    st.title("Chatbot usando Code Llama")

    image = Image.open('codellama.jpg')
    st.image(image, caption = 'Code Llama')

    st.markdown(
        """
        Usando el modelo de Code Llama.
    """
    )

def clear_chat_history():
    st.session_state.messages = [{"role" : "assistant", "content": msg_chatbot}]

st.sidebar.button('Limpiar historial de chat', on_click = clear_chat_history)

msg_chatbot = """
        Soy un chatbot que está usa el modelo Code Llama: 

        ### Preguntas frecuentes
        
        - ¿Puedes brindarme el código en python para leer un csv?
        - Y muchas otras mas.
"""

def get_response_codellama(prompt):

    llm = Replicate(
        model = "meta/codellama-34b:efbd2ef6feefb242f359030fa6fe08ce32bfced18f3868b2915db41d41251b46",
        model_kwargs = {"temperature" : 0.01, "max_length" : 500}
    )

    return(llm(prompt))

#Si no existe la variable messages, se crea la variable y se muestra por defecto el mensaje de bienvenida al chatbot.
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content" : msg_chatbot}]

# Muestra todos los mensajes de la conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ingresa tu pregunta")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Genera una nueva respuesta si el último mensaje no es de un assistant, sino un user
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Esperando respuesta, dame unos segundos."):
            
            response = get_response_codellama(prompt)
            placeholder = st.empty()
            full_response = ''
            
            for item in response:
                full_response += item
                placeholder.markdown(full_response)

            placeholder.markdown(full_response)

    message = {"role" : "assistant", "content" : full_response}
    st.session_state.messages.append(message) #Agrega elemento a la caché de mensajes de chat.