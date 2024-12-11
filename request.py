import requests as req
response = req.get("https://api.sampleapis.com/avatar/info")
print(response.content)