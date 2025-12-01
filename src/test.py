import json
import requests

url = "https://water-drinkability-pipeline.onrender.com/predict"

x_new = {
  "ph": 6.623613565745125,
  "Hardness": 203.030141349452,
  "Solids": 17167.301297022455,
  "Chloramines": 6.049600899198109,
  "Sulfate": 311.72628825094733,
  "Conductivity": 410.2432474590725,
  "Organic_carbon": 15.9145000730461,
  "Trihalomethanes": 65.02122896904768,
  "Turbidity": 2.9151659507443948
}

x_new_json = json.dumps(x_new)
response = requests.post(url, data = x_new_json)
print("Response Text:",response.text)
print("Status Code:", response.status_code)