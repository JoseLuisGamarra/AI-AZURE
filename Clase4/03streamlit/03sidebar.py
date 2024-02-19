import streamlit as st
from PIL import Image

st.set_page_config(page_title = "Web con sidebar", page_icon = "https://is3-ssl.mzstatic.com/image/thumb/Purple123/v4/43/9a/2b/439a2b08-d8d7-9c89-e142-45f9460f9dcf/source/256x256bb.jpg")

with st.sidebar:

    st.title("Este es un sidebar")

    image = Image.open('machupicchu.jpg')
    st.image(image, caption = 'Machu Picchu')

    st.markdown(
        """
        En un mundo en constante evolución tecnológica, la industria turística busca 
        aprovechar las herramientas digitales para mejorar la experiencia del visitante. 
        Cusco, uno de los destinos turísticos más emblemáticos de Perú y del mundo, 
        requiere soluciones innovadoras para atender a la creciente demanda de información y 
        servicios de calidad por parte de sus visitantes. En este contexto, 
        un chatbot se presenta como una solución tecnológica ideal para satisfacer nuestras necesidades.
        
        ### Propósito

        El propósito principal del chatbot para el sector turismo en Cusco es facilitar la planificación
        y ejecución de la experiencia turística de los visitantes a través de 
        respuestas inmediatas, precisas y personalizadas sobre lugares de interés, 
        desplazamientos y costos asociados.

        ### Objetivos

        - Información actualizada y accesible : Ofrecer a los turistas información actualizada y relevante sobre puntos de interés en Cusco.
        - Orientación de desplazamientos : Proveer recomendaciones sobre cómo desplazarse en la ciudad y sus alrededores, ofreciendo opciones desde transporte público hasta tours organizados.
        - Transparencia en costos : Brindar detalles sobre precios actuales de entradas, pasajes, tours y otros servicios, permitiendo al turista presupuestar y planificar mejor su viaje.
        - Atención 24/7 : Dado que es un servicio digital, el chatbot puede atender consultas en cualquier momento, beneficiando a aquellos turistas que operan en diferentes zonas horarias o que necesitan información fuera de horas laborables.
        - Adaptabilidad lingüística : Posibilidad de interactuar con turistas de diversas nacionalidades, ofreciendo respuestas en varios idiomas.
    """
    )

def clear_chat_history():
    st.session_state.messages = [{"role" : "assistant", "content": msg_chatbot}]

st.sidebar.button('Limpiar historial de chat', on_click = clear_chat_history)

msg_chatbot = """
        Soy un chatbot que te ayudará a conocer Cusco: 
        
        ### Puedo ayudarte con lo relacionado a:

        - 🚶🏻 Como desplazarte por la ciudad.
        - 🥘 Restaurantes típicos imperdibles
        - 💰 Precios del tren de Perú Rail
        - 🎟 Boleto para entrar a Machu Picchu

        ### Preguntas frecuentes

        - ¿qué comida típica puedo comer?
        - ¿qué puedo hacer en esta hermosa ciudad?
        - ¿qué restaurantes me recomiendas visitar? ponlo en una lista
        - ¿cómo puedo comprar los boletos para entrar a Machu Picchu?
        - ¿cómo puedo desplazarme en la ciudad?
"""

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

# Generar una nueva respuesta si el último mensaje no es de un assistant, sino de un user
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Esperando respuesta, dame unos segundos."):
            
            response = "Ingresaste la siguiente pregunta : " + prompt
            placeholder = st.empty()
            full_response = ''
            
            for item in response:
                full_response += item
                placeholder.markdown(full_response)

            placeholder.markdown(full_response)

    message = {"role" : "assistant", "content" : full_response}
    st.session_state.messages.append(message) #Agrega elemento a la caché de mensajes de chat.