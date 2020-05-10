import textblob

t=textblob.TextBlob('good')
print(t.polarity)

t=textblob.TextBlob('fantastic')
print(t.polarity)

t=textblob.TextBlob('awesome')
print(t.polarity)

t=textblob.TextBlob('excellent')
print(t.polarity)

t=textblob.TextBlob('very good')
print(t.polarity)