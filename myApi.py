from textblob import TextBlob

class API:

    def sentiment_analysis(self, text):
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity  

            positive = max(0, polarity)
            negative = max(0, -polarity)
            neutral = 1 - (positive + negative)

            result = {
                "POSITIVE": round(positive, 2),
                "NEGATIVE": round(negative, 2),
                "NEUTRAL": round(neutral, 2)
            }

            return result

        except Exception as e:
            return {"Error": str(e)}

    def ner(self,text):
        pass

    def emotion_analysis(self,text):
        pass