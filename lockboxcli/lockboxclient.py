#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()


import json
import jwt
import requests
import time
import os
import urllib3
from urllib3._collections import HTTPHeaderDict



use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True


class LockboxClient:
    x_initialization_vector = None
    x_api_key = None
    x_decryption_key = None
    lockbox_host = None
    key = None
    secret = None
    new_secret = None
    template = None
    generated_config = None
    environment = None

    def __init__(self):
        self.x_initialization_vector = os.environ['X_INITIALIZATION_VECTOR']
        self.x_api_key = os.environ['X_API_KEY']
        self.x_decryption_key = os.environ['X_DECRYPTION_KEY']
        self.lockbox_host = os.environ['LOCKBOX_HOST']
        self.template = os.environ['SMP_SETUP_DIR'] + '/../../../etc/master_template.conf-debug'
        self.generated_config = os.environ['SMP_SETUP_DIR'] + '/generated-from-lockbox-master.conf-debug'
