#!/usr/bin/env python
# encoding: utf-8

import cgi

def urlParameter():
    form = cgi.FieldStorage()    
    return form.getvalue('username') or 'Sem nome'

def basicHtml(title, content):
    print "Content-type: text/html"
    print """
        <!doctype html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
                <div class="result">
                    <h1>Olá, %s.</h1>
                </div>
            </body>
        </html>
    """ % (title, content)

basicHtml('Recuperar do formulário', urlParameter())