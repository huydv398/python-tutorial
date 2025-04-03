
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


## Passing Parameters
```bash 
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)


#We can read the content of the server’s response

r = requests.get('https://api.github.com/events')
r.text

r.content

r.json() #JSON Response Content




#Custom Headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

r = requests.post('https://httpbin.org/post', data=payload)


# POST requests
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload) #or

# Response Status Codes
r = requests.get('https://httpbin.org/get')
r.status_code


#Header
r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}


r.headers['Content-Type']
#output: 'application/json'

```

### Advanced

```bash 

r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
r.headers
r.request.headers

# ignore verifying the SSL certificate 
requests.get('https://kennethreitz.org', verify=False)


# authentication

requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
#<Response [200]>


```


```bash 
def print_url(r, *args, **kwargs):
    print(r.url)
```

* `*args` cho phép hàm nhận một số lượng tham số không xác định và lưu trữ chúng dưới dạng một tuple. args chứa các tham số bổ sung không được đặt tên.

* `**kwargs` cho phép hàm nhận một số lượng tham số từ khóa không xác định và lưu trữ chúng dưới dạng một từ điển. kwargs chứa các tham số bổ sung có tên (key).



```bash
curl -k -H "Authorization: Token da6b8955f31e800827e0c4fd1dfc3316f1024683" \
-H "Accept: application/json; indent=4" \
https://172.16.66.29/api/tenancy/tenants/
```

curl -X 'POST' -k -H "Authorization: Token da6b8955f31e800827e0c4fd1dfc3316f1024683" \
-H "Content-Type: application/json" \
https://172.16.66.29/api/tenancy/tenants/ -d $'{"name": "huydv", "slug": "huydv"}

curl -X 'POST' -k -H "Authorization: Token da6b8955f31e800827e0c4fd1dfc3316f1024683" \
-H "Content-Type: application/json" \
https://172.16.66.29/api/dcim/devices/ -d $'{"name": "name_device", "role": {"id": "1"}, "site": {"id": "1"}, "description": "description", "status": "active", "device_type": {"model": "PowerEdge R630"}}'

```Python
# add device
def r_netbox():
    # tenant_name = str(input("Enter name tenant: "))
    url_api = url + 'api/dcim/devices/'

    data = {
        "name":"huydv1234",
        "role":{
            "id":"1"
        },
        "site":{
            "id":"1"
        },
        "description":"description",
        "status":"active",
        "device_type":{
            "model":"PowerEdge R630"
        }
        }
    r = requests.post(url_api, headers=headers, json=data, verify=False)
    print(r) #result Status code
```

curl -X 'PUT' -k -H "Authorization: Token da6b8955f31e800827e0c4fd1dfc3316f1024683" \
-H "Content-Type: application/json" \
https://172.16.66.29/api/tenancy/tenants/1 \
--data '{"name": "reserved"}'

curl -s -k -X PATCH \
-H "Authorization: Token da6b8955f31e800827e0c4fd1dfc3316f1024683" \
-H "Content-Type: application/json" \
https://172.16.66.29/api/tenancy/tenants/1/ \
--data '{"name": "reserved"}' | jq '.'

```python
# demo
def r_netbox():
    tenant_name = str(input("Enter name tenant: "))
    url_api = url + 'api/tenancy/tenants/'
    data = {
        'name': tenant_name,
        'slug': tenant_name.replace(" ", "-")
    }
    r = requests.post(url_api, headers=headers, json=data, verify=False)
    # print(r) #result Status code

r_netbox()
```



### print output python
```json
{'count': 1, 'next': None, 'previous': None, 'results': [{'id': 1, 'url': 'https://172.16.66.29/api/tenancy/tenants/1/', 'display_url': 'https://172.16.66.29/tenancy/tenants/1/', 'display': 'SUN', 'name': 'SUN', 'slug': 'sun', 'group': None, 'description': '', 'comments': '', 'tags': [{'id': 2, 'url': 'https://172.16.66.29/api/extras/tags/2/', 'display_url': 'https://172.16.66.29/extras/tags/2/', 'display': 'NetBox-synced', 'name': 'NetBox-synced', 'slug': 'netbox-synced', 'color': '9e9e9e'}, {'id': 3, 'url': 'https://172.16.66.29/api/extras/tags/3/', 'display_url': 'https://172.16.66.29/extras/tags/3/', 'display': 'Source: VCENTER', 'name': 'Source: VCENTER', 'slug': 'source-vcenter', 'color': '9e9e9e'}, {'id': 4, 'url': 'https://172.16.66.29/api/extras/tags/4/', 'display_url': 'https://172.16.66.29/extras/tags/4/', 'display': 'Source: VCENTER-SUNCLOUD', 'name': 'Source: VCENTER-SUNCLOUD', 'slug': 'source-vcenter-suncloud', 'color': '9e9e9e'}], 'custom_fields': {}, 'created': '2025-02-27T09:38:47.754916Z', 'last_updated': '2025-02-28T02:50:46.583943Z', 'circuit_count': 0, 'device_count': 1, 'ipaddress_count': 39, 'prefix_count': 0, 'rack_count': 0, 'site_count': 0, 'virtualmachine_count': 52, 'vlan_count': 0, 'vrf_count': 0, 'cluster_count': 1}]}
```


```python
def r_netbox():
    # tenant_name = str(input("Enter name tenant: "))
    url_api = url + 'api/tenancy/tenants/'
    r = requests.get(url_api, headers=headers, verify=False)
    # print(r.json()) #result Status code
    # parsed = json.loads(r.text)
    # print(json.dumps(parsed, indent=4))
    data = r.json()
    print(data['results'][0]['url'])
```


#### Use loop in var is json 
```python
# Loop through the tags and print the 'id' of each tag
for tag in data['results'][0]['tags']:
    print(tag['id'])
```