#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for

# initialize template

app = Flask(__name__,template_folder='public_html')
    
# define routes
@app.route('/')
def index():
    return render_template('index.html',title="Home",description="Home")
    
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=True)


