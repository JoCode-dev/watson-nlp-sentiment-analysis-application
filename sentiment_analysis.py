import requests


def sentiment_analyzer(text_to_analyze):
    URL="https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    headers = { "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock" }
    myobj = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url=URL, json=myobj, headers=headers)
    return res.text