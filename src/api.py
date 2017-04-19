import unirest
import pprint
text = "i am in love with the shape of you"

emotion = unirest.post("http://apidemo.theysay.io/api/v1/emotion", headers={ "Accept": "application/json" }, params={ "text": text, "level": "sentence" })

#print emotion.body
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(emotion.body)



topic = unirest.post("http://apidemo.theysay.io/api/v1/topic", headers={ "Accept": "application/json" }, params={ "text": text, "level": "sentence" })

#print topic.body
pp.pprint(topic.body)

sentiment = unirest.post("http://apidemo.theysay.io/api/v1/sentiment", headers={ "Accept": "application/json" }, params={ "text": text, "level": "sentence" })

#print sentiment.body
pp.pprint(sentiment.body)

print topic.body[0]['scores'][0]['label']
print topic.body[0]['scores'][1]['label']
print topic.body[0]['scores'][2]['label']
