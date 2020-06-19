import  requests;
payload = {'key1': 'value1', 'key2': 'value2'}
html=requests.post("http://httpbin.org/post",data=payload)
print(html.text)
