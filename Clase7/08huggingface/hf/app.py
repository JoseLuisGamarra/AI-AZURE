import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.vectorstores import Pinecone
from PIL import Image
import os
import boto3
import pinecone

pinecone_key = os.environ["PINECONE_API_KEY"]
pinecone_env = "gcp-starter" 
index_name = "knowledge-base-eliminatorias" 

region = 'us-east-1'
aws_access_key_id = os.environ["ACCESS_KEY"]
aws_secret_access_key = os.environ["ACCESS_SECRET_KEY"]

st.set_page_config(page_title = "Chatbot usando Bedrock (Anthropic Claude 2)", page_icon = "⚽")

#Create a Side bar
with st.sidebar:
    
    st.title("Chatbot usando Bedrock (Anthropic - Claude 2)")
    
    image = Image.open('conmebol.jpg')
    st.image(image, caption = 'Conmebol')

    st.markdown(
        """
        ### Propósito

        Este chatbot utiliza una base de conocimiento (Pinecone) con información del sitio web de Marca.
        Usa Langchain para usar Bedrock (Anthropic - Claude 2)

        ### Fuentes 

        - Marca - (https://www.marca.com)
    """
    )

msg_chatbot = """
        Soy un chatbot que te ayudará a conocer sobre las eliminatorias sudamericanas: 
        
        ### Puedo ayudarte con las siguiente preguntas:

        - ¿Quién es el líder en la tabla de posiciones?
        - ¿Cuáles son los próximos partidos de Perú?
        - Bríndame la tabla de posiciones
        - Y muchas más ..... 
"""
#Store the LLM Generated Reponese
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content" : msg_chatbot}]
    
# Diplay the chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Clear the Chat Messages
def clear_chat_history():
    st.session_state.messages = [{"role" : "assistant", "content": msg_chatbot}]

# Create a Function to generate
def generate_bedrock_pinecone_response(prompt_input):
    
    model_version_id = "anthropic.claude-v2"
    bedrock_client = boto3.client(
        "bedrock-runtime", 
        region_name = region,
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key
    )
    
    llm = Bedrock(
        model_id = model_version_id, 
        client = bedrock_client,
        model_kwargs = {'temperature': 0}
    )

    template = """Responda a la pregunta basada en el siguiente contexto.
    Si no puedes responder a la pregunta, usa la siguiente respuesta "No lo sé disculpa, puedes buscar en internet."

    Contexto: 
    {context}.
    Pregunta: {question}
    Respuesta utilizando también emoticones: 
    """
    
    prompt = PromptTemplate(
        input_variables = ["context", "question"],
        template = template
    )

    chain_type_kwargs = {"prompt": prompt}

    embeddings = OpenAIEmbeddings()
    
    # Connect with Pinecone
    pinecone.init(
        api_key = pinecone_key,
        environment = pinecone_env
    )
    
    text_field = "text"
    # switch back to normal index for langchain
    index = pinecone.Index(index_name)
    vectorstore = Pinecone(
        index, embeddings.embed_query, text_field
    )

    qa = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = 'stuff',
        retriever = vectorstore.as_retriever(),
        verbose = True,
        chain_type_kwargs = chain_type_kwargs
    )

    output = qa.run(prompt_input)

    return output

st.sidebar.button('Limpiar historial de chat', on_click = clear_chat_history)

prompt = st.chat_input("Ingresa tu pregunta")
if prompt:
    st.session_state.messages.append({"role": "user", "content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generar una nueva respuesta si el último mensaje no es de un assistant, sino un user
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Esperando respuesta, dame unos segundos."):
            
            response = generate_bedrock_pinecone_response(prompt)
            placeholder = st.empty()
            full_response = ''
            
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)

    message = {"role" : "assistant", "content" : full_response}
    st.session_state.messages.append(message) #Agrega elemento a la caché de mensajes de chat.