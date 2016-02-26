from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import time
import json
from HTMLParser import HTMLParser


ckey = ''' #private
csecret = '''
atoken = '''
asecret = '''

m = Basemap(projection='mill', llcrnrlat=20, urcrnrlat=50,\
        llcrnrlon=-130, urcrnrlon=-60, resolution ='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

class listener(StreamListener):
    x = []
    y = []

    def on_status(self, status):

        if status.coordinates:
            print status.text
            print status.coordinates
            print("\n")
            coords  = status.coordinates
            latitude = coords['coordinates'][0]
            longitude = coords['coordinates'][1]
            xt,yt = m(latitude, longitude)
            self.x.append(xt)
            self.y.append(yt)
            m.plot(self.x, self.y, 'ro', markersize=5, alpha=.5)

        

Plotter = listener()
try:
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, Plotter)
    twitterStream.filter(track=["stolen", "thief", "thieve", "thiefs", "stole", "theft", "murder", "crime", "steal", "jail"])
    Plotter.plotAll()
except KeyboardInterrupt, e:
    plt.show()
