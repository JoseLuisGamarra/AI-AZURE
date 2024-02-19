
Codespaces es un entorno de desarrollo instantáneo basado en la nube que usa un contenedor para proporcionar lenguajes comunes, herramientas y utilidades para el desarrollo.

![image](https://user-images.githubusercontent.com/2066453/278680037-24cbb036-f0e0-4410-974d-eb04b36426c7.png)

Creamos un Codespaces, clic en Code -> Codespace -> Create codespace on master.

(![image](https://github.com/TonyTecPeru/IA-GENERATIVA/assets/17399925/93e72cb2-af5c-4a22-8979-11ccb4efdb16)

En el terminal de Codespaces ejecuta este comando para instalar las librerías necesarias para el curso:

	pip install openai langchain streamlit Pillow replicate pinecone-client pypdf tiktoken datasets apache_beam pinecone-datasets faiss-cpu chromadb sentence-transformers boto3
 	python -m pip install --upgrade pip

Instalar las siguientes librerías en python

	pip install qdrant-client unstructured[pdf] pysqlite3-binary yt_dlp pydub ffmpeg

 Instalamos ffmpeg:
 
	sudo apt-get update
	sudo apt-get install -y ffmpeg

Instalar las siguientes librerías en python

	pip install gradio google-search-results langchainhub numexpr langchain_experimental
 	pip install boto3 --upgrade

En el repositorio no se podrán subir cambios, para descargar los cambios ejecutar estos dos comandos en el terminal de Codespaces:

	git checkout -f
 	git pull
	
