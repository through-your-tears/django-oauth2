import datetime, random, string
import pytz
from django.conf import settings

import jwt


def generate_jwt(pk):
    dt = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')) + datetime.timedelta(seconds=20)
    token = jwt.api_jwt.encode({
        'id': pk,
        'exp': dt,
    }, settings.SECRET_KEY, algorithm='HS256')
    return token


def generate_rt():
    return ''.join([random.choice(string.ascii_letters) for i in range(128)])
