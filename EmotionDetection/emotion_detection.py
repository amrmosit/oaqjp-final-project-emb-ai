import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse):  # Define a function named emotional_detector that takes a string input (text_to_analyse)
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emosion detector service
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    
    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    # Sending a POST request to the emotion detector API
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting the emotions from the response
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    domain_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], 
        key=formatted_response['emotionPredictions'][0]['emotion'].get)

    return {'anger': anger,
     'disgust': disgust, 
     'fear' : fear,
     'joy' : joy,
     'sadness' : sadness,
     'domain_emotion' : domain_emotion 
     }
