import json

file_path = "HAPP/DEFAULT.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

my_proxy = ["geosite:meta"]
my_direct = ["domain:dtpax.ru", "domain:tvoe.live"]

data["ProxySites"] = [site for site in data["ProxySites"] if site not in my_proxy]
data["DirectSites"] = [site for site in data["DirectSites"] if site not in my_direct]

data["ProxySites"] = my_proxy + data["ProxySites"]
data["DirectSites"] = my_direct + data["DirectSites"]

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
