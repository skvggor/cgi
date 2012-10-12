#!/usr/bin/env python
# encoding: utf-8

import inspect

def sum(x, y):
    scope = inspect.currentframe()
    return [
        x + y, 
        inspect.getargvalues(scope).locals['x'], 
        inspect.getargvalues(scope).locals['y']
    ]

def basicHtml(title, content, x, y):
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
                    <h1>Resultado entre %s e %s é %s</h1>
                <div>
            </body>
        </html>
    """ % (title, content, x, y)

basicHtml('Somando', sum(25,25)[1], sum(25,25)[2], sum(25,25)[0])