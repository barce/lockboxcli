#!/usr/bin/env python

from lockboxcli import LockboxClient
client = LockboxClient()
client.show_config()
client.connect()
client.environments()
client.environment('test')

