import requests as req

def call_text_analytics_api(headers, document, endpoint):
    response = req.post("https://fastapi.cognitiveservices.azure.com/" +
                        endpoint, headers=headers, json=document)
    return response.json()