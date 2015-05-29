import requests
data =  {"reply_user_id": "58374", "reply_text": "Hi from Python!", "token": "1234567", "post_id" :"28", "anonymous": "0"}


p = requests.post('http://localhost/alpha/urlinqyii/post/reply', data)

print p.text