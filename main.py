from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def scrape():
    url = "https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%B9%E3%83%8E%E3%83%BC%E3%83%88_(%E6%98%A0%E7%94%BB)"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # ページの <title> を取得
    title = soup.title.string if soup.title else "No title found"
    return jsonify({"title": title})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
