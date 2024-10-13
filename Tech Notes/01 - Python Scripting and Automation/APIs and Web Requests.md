
Using `requests` library.

# REST
## GET

```python ln:False
>>> import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/1"
>>> response = requests.get(api_url)

>>> response.json()
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>> response.status_code
200
>>> response.headers["Content-Type"]
'application/json; charset=utf-8'
```

## POST

```python ln:False hl:3,5,6
>>> import requests
>>> import json
>>> api_url = "https://jsonplaceholder.typicode.com/todos"
>>> todo = {"userId": 1, "title": "Buy milk", "completed": False}
>>> headers =  {"Content-Type":"application/json"}
>>> response = requests.post(api_url, data=json.dumps(todo), headers=headers)
>>> response.json()
{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

>>> response.status_code
201
```

## PUT vs PATCH

`PATCH` differs from `PUT` in that it doesn’t completely replace the existing resource. It only modifies the values set in the JSON sent with the request.

## DELETE

```python ln:False
>>> import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/10"
>>> response = requests.delete(api_url)
>>> response.json()
{}

>>> response.status_code
200
```

---

# Authentication

> Basic Authentication
```python
import requests from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('user', 'pass')
print(requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth)) 

# Returns: <Response [200]>
```

- simplified
```python
print(requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass')))

# Returns: <Response [200]>
```

> Token Authentication
```python
# Using an Authorization Token as Credentials
import requests headers = {'Authorization': 'Bearer <your_token>'}
print(requests.get('https://httpbin.org/basic-auth/user/pass', headers=headers))

# Returns: <Response [200]>
```

---

# Session Storage

```python
>>> import requests
>>>
>>> s = requests.Session()
>>> s.headers.update({'accept': 'datagy'})
>>>
>>> resp = s.get('https://httpbin.org/headers')
>>> print(resp.text)
{
  "headers": {
    "Accept": "datagy",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-670be376-1eabf4c910aba6527a3b518f"
  }
}
```

```python
>>> import requests
>>>
>>> s = requests.Session()
>>> s.get('https://httpbin.org/cookies/set/sessioncookie/jeswins')
<Response [200]>
>>> resp = s.get('https://httpbin.org/cookies')
>>> print(resp.text)
{
  "cookies": {
    "sessioncookie": "jeswins"
  }
}
```
> The `httpbin.org` site is a simple HTTP request and response service.
> - `https://httpbin.org/cookies/set`: This part is setting a cookie.
> - `/sessioncookie/jeswins`: It's setting a cookie named `sessioncookie` with the value `jeswins`.

1. We created a session object, `s`
2. We then placed a `GET` request to set a session cookie, labeling the cookie `'jeswins'`
3. We then sent another request to get the cookies of the session
4. Finally, we printed the `.text` attribute of the `Response` object

---

# SSL Cert Verification

You can pass `verify` the path to a CA_BUNDLE file or directory with certificates of trusted CAs:

```python
requests.get('https://github.com', verify='/path/to/certfile')
```

or persistent:

```python
s = requests.Session()
s.verify = '/path/to/certfile'
```

> [!note] 
> If `verify` is set to a path to a directory, the directory must have been processed using the `c_rehash` utility supplied with OpenSSL.


---

# Multipart-Encoded Requests

```python
url = 'https://httpbin.org/post'
>>> multiple_files = [
...     ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
...     ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
>>> r = requests.post(url, files=multiple_files)
>>> r.text
{
  ...
  'files': {'images': 'data:image/png;base64,iVBORw ....'}
  'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
  ...
}
```
- `'rb'` stands for read binary

> [!warning] 
> It is strongly recommended that you open files in [binary mode](https://docs.python.org/3/tutorial/inputoutput.html#tut-files "(in Python v3.12)"). This is because Requests may attempt to provide the `Content-Length` header for you, and if it does this value will be set to the number of _bytes_ in the file. Errors may occur if you open the file in _text mode_.


