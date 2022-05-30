#!/usr/bin/env python
from dotenv import set_key, get_key
from django.core.management.utils import get_random_secret_key

ENV_FILE = '.env.prod'

set_key(ENV_FILE, 'DJANGO_DEBUG', '0')
if get_key(ENV_FILE, 'DJANGO_SECRET_KEY') is None:
    set_key(ENV_FILE, 'DJANGO_SECRET_KEY', get_random_secret_key())
