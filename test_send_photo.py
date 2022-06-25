import requests

with open('sample.jpeg', 'rb') as ph:
    headers = {
        'sensor': '2',
        'temperature': '21',
    }
    files = {'photo': ph.read()}
    response = requests.post('http://127.0.0.1:8000/api/measurements/', headers=headers, files=files)
