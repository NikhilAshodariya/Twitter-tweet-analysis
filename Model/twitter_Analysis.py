from tweepy.streaming import StreamListener
import time
import urllib
import json
import re # regular expression
from textblob import TextBlob
import matplotlib.pyplot as plt



negative=0
neutral=0
positive=0

plt.ion()
class Listener(StreamListener):

	def __init__(self):
		self.initalTime=time.time()

	def clearPlot(self):
		plt.clf()


	def calculateTime(self,time):
		# global initalTime
		return time-self.initalTime

	def sentimentAnalysis(self,block):
		global positive
		global negative
		global neutral

		t=int(self.calculateTime(time.time()))
		count=0
		for sen in block.sentences:
			count+=1
			
			print('time = ',t)
			if sen.sentiment.polarity >=0:
				positive+=sen.sentiment.polarity
				
			else:
				negative+=sen.sentiment.polarity
			print(count)

		print('positive = ',positive)
		print('negative = ',negative)
		plt.plot([t],[positive],'go',[t] ,[negative],'ro')
		plt.show()
		plt.pause(0.0001)
		pass

	

	def on_data(self,data):
		try:
			plt.axis([0,100,-15,15])
			plt.xlabel('time')
			plt.ylabel('Sentiment')


			all_data=json.loads(data)
			tweet=all_data["text"]
			pattern=re.compile(r"[a-zA-Z0-9 \t\n\r\f\v]+")
			lis=pattern.findall(tweet)
			string=''.join(lis)
			block=TextBlob(string.strip())
			self.sentimentAnalysis(block)

			return True

		except BaseException as e:
			print("Failed on data")
			print(str(e))
			time.sleep(5)

	def on_error(self,status):
		print(status)