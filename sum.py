#!/usr/bin/env python
# encoding: utf-8

import inspect

def sum(x, y):
    scope = inspect.currentframe()
    parameter = {
        'x' : str(inspect.getargvalues(scope).locals['x']),
        'y' : str(inspect.getargvalues(scope).locals['y'])
    }

    return 'Resultado da soma entre ' + \
            parameter['x'] + ' e ' + \
            parameter['y'] + ' é ' + \
            str(x+y)

def basicHtml(title, content):
    print "Content-type: text/html\n"
    print """
        <!doctype html>
        <html>
            <meta charset="utf-8" />
            <head>
                <title>%s</title>
            </head>
            <body>
                <div class="result">
                    <h1>%s</h1>
                <div>
            </body>
        </html>
    """ % (title, content)

basicHtml('Somando', sum(78, 10))