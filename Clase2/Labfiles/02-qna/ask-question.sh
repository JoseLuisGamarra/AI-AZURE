
prediction_url="https://qatstd.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=AprenderPreguntasFrecuentes&api-version=2021-10-01&deploymentName=production"
key="6ac2996c02f3487fa37fe1c120f87f5c"

curl -X POST $prediction_url -H "Ocp-Apim-Subscription-Key: $key" -H "Content-Type: application/json" -d "{'question': 'What is a learning Path?' }"

