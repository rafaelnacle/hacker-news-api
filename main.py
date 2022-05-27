import requests
from flask import Flask, render_template, request, redirect

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
    



app.run(host="0.0.0.0")


