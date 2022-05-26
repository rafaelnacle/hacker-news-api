import requests
from flask import Flask, render_template, request

app = Flask("HackerNews")

@app.route('/')
def home():
    recent_news_url = f"http://hn.algolia.com/api/v1/search_by_date?tags=story"
    recent_news_json = requests.get(recent_news_url).json()
    
    return render_template('index.html', recent_news=recent_news_json)


app.run(host="0.0.0.0")


