import requests
resp = requests.get("http://127.0.0.1/prediction/api/v1.0/some_prediction?&sl=5.1&pl=1.4")
print(resp.content)

