## Crear variables de entorno para probar localmente el chatbot

    export OPENAI_API_KEY="sk-XXXXX"
    export PINECONE_API_KEY="TU_API_KEY_PINECONE"
    export ACCESS_KEY="AKIAY6VHQEJTLSP3ABH3"
    export ACCESS_SECRET_KEY="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"

    cd 08huggingface/hf
    streamlit run app.py

## Crear secretos en el Space.

    OPENAI_API_KEY="sk-XXXXX"
    PINECONE_API_KEY="TU_API_KEY_PINECONE"
    ACCESS_KEY="AKIAY6VHQEJTLSP3ABH3"
    ACCESS_SECRET_KEY="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"

## Creación de imagen

    cd 08huggingface

	docker build -t app-ingest-pinecone-website ingestapinecone

## Ejecución de contenedor

	docker run -e OPENAI_API_KEY='sk-XXXX' \
        -e PINECONE_API_KEY='XXX' \
        app-ingest-pinecone-website

# Crear space en Hugging Face