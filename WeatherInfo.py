import re
import urllib.request

city = input("Enter your city: ")

url = "http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

data = urllib.request.urlopen(url).read();
data1 = data.decode("utf-8")

m = re.search('span class="phrase">',data1)

start = m.end();
end = start + 300;

newString = data1[start:end]

m = re.search("</span>",newString)
end = m.start()

final = newString[0:end]
print(final)

