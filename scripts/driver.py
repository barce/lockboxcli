#!/usr/bin/env python

from lockboxcli import LockboxClient
client = LockboxClient('staging')
client.show_config()
resp = client.generate_config()
print(resp)
print(resp.text)
var_list = client.get_keys()
for var in var_list:
    print(var)

print("--- get secrets ---")
r = client.get_secret('DJANGO_PASSWORD')
print(r)

r = client.get_secret('PIP_TEST')
print(r)

print("update PIP_TEST")
r = client.update_secret('PIP_TEST', 'bazquux')
print(r)
print("get PIP_TEST")
r = client.get_secret('PIP_TEST')
print(r)
