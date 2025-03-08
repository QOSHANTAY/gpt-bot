import requests

url = "https://chatgpt-42.p.rapidapi.com/o3mini"

async def get_response(question):
	payload = {
		"messages": [
			{
				"role": "user",
				"content": question
			}
		],
		"web_access": False
	}
	headers = {
		"x-rapidapi-key": "ab899f1834mshaec6e09fab6fb14p13c281jsn81d8c7a63614",
		"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.json()['result']