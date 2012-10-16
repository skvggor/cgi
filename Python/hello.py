#!/usr/bin/env python
# encoding: utf-8

def hello(name):
    print "Content-type: text/html\n"
    print """
        <!doctype html>
        <html>
            <head>
                <title>Hello, world!</title>
            </head>
            <body>
                <div class="hello">
                    <h1>Hello, %s!</h1>
                <div>
            </body>
        </html>
    """ % name
    
hello('Marcos')