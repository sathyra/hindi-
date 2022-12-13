# codecs provides access to the internal Python codec registry
import codecs

# This is to translate the text from Hindi to English
from deep_translator import GoogleTranslator

# This is to analyse the sentiment of text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Read the hindi text into 'sentences'
with codecs.open('SampleHindiText.txt', encoding='utf-8') as f:
	sentences = f.readlines()
for sentence in sentences:
	translated_text = GoogleTranslator(source='auto', target='en').translate(sentence)
	#print(translated_text)
	analyzer = SentimentIntensityAnalyzer()
	sentiment_dict = analyzer.polarity_scores(translated_text)
	
	print("\nTranslated Sentence=",translated_text, "\nDictionary=",sentiment_dict)
	if sentiment_dict['compound'] >= 0.05 :
			print("It is a Positive Sentence")
			
	elif sentiment_dict['compound'] <= - 0.05 :
			print("It is a Negative Sentence")	
	else :
		print("It is a Neutral Sentence")
