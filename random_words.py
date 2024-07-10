import requests

def get_random_words():
    
    end_point = 'https://random-word-api.vercel.app/api?words=10'

    response = requests.get(end_point)
    data = response.json()

    return data

