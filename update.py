import urllib.request
import json

url = "https://raw.githubusercontent.com/hydraponique/roscomvpn-routing/main/HAPP/DEFAULT.json"

response = urllib.request.urlopen(url)
text = response.read()
data = json.loads(text)

data["ProxySites"] = ["geosite:meta"] + data["ProxySites"]
data["DirectSites"] = ["domain:dtpax.ru", "domain:tvoe.live"] + data["DirectSites"]

file = open("HAPP/DEFAULT.json", "w", encoding="utf-8")
json.dump(data, file, indent=4, ensure_ascii=False)
file.close()
