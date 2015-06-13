#!/usr/bin/python3


import sys
import cgitb
import cgi
import os
import importlib

cgitb.enable()

# base path.
BASE = '/home/folkert/webdev/'


from contextlib import contextmanager
@contextmanager
def timer(task, display=True):
    from time import time
    t = time()
    yield
    if display:
        print("task {} took {:.3f}s".format(task, time() - t))


def application(env, start_response):
    uri = env.get('PATH_INFO')
    sys.path.append(BASE + os.path.dirname(uri))
    module = os.path.basename(uri).split('.')[0]
    try:
        module = importlib.__import__(module)
    except ImportError:
        # look for the right folder
        import glob
        path = glob.glob("{}/**/{}".format(BASE, uri))
        sys.path.append(os.path.dirname(path[0]))
        module = importlib.__import__(module)

    importlib.reload(module)
    start_response('200 OK', [('Content-Type', 'text/html')])
    with timer("creating page"):
        return [module.main(env=env)]
