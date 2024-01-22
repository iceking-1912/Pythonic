

import os


def envgetr(*args):
    envvar = os.environ.get(*args)
    print(envvar)

envgetr('ACCOUNT_SID')