# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

def calc_sentiment():
    # Instantiates a client
    client = language.LanguageServiceClient()

    #Import Tweets result file.
    with open("Hashtag_Tweets.json", "r+", encoding='utf-8') as f:
        data = json.loads(f.read()) 
    Sentiment_output = open("tweets_sentiment.txt","w", encoding='utf-8')
    #Analyze each tweet text
    generalScore = 0.0
    for tweet in data:
        text = tweet['text']
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        #Call API to analyze text.
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        #Write result to file
        generalScore += sentiment.score
        Sentiment_output.write("Text:" + text +"\n")
        Sentiment_output.write("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude)+"\n\n")

    print("The general sentiment score of Trump over last 20 tweets is: " + str(generalScore))
    return generalScore
