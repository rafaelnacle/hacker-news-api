import requests
from flask import Flask, render_template, request, redirect
import json

app = Flask("HackerNews")

@app.route('/')
def home():     
    if request.args.get('order_by') == "popular" or request.args.get('order_by') == "None":
        url_popular = f"https://hn.algolia.com/api/v1/search?tags=story"
        json_req = requests.get(url_popular).json()
        
        return render_template('index.html', json_req=json_req)
    elif request.args.get('order_by') == "new":
        url_new = f"http://hn.algolia.com/api/v1/search_by_date?tags=story"
        json_req = requests.get(url_new).json()
        
        return render_template('index.html', json_req=json_req)
    else:
        url_home = f"https://hn.algolia.com/api/v1/search?tags=story"
        json_req = requests.get(url_home).json()
        
        return render_template('index.html', json_req=json_req)
    
@app.route('/<id>')
def get_by_id(id):
  
    article_id = f"http://hn.algolia.com/api/v1/items/{id}"
    article_id_req = requests.get(article_id).json()

        
    return render_template('id.html', article=article_id_req)


app.run(host="0.0.0.0")


