from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace with your NewsAPI key
NEWS_API_KEY = 'f09e72c394ab40dab884afedd35db4f4'

@app.route('/')
def home():
    # Fetch headlines from NewsAPI
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract headlines and links
    articles = data.get('articles', [])
    headlines = [{'title': article['title'], 'url': article['url']} for article in articles]

    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)