from flask import Flask, render_template
import requests
import threading
import time
import schedule

app = Flask(__name__)

# Replace with your NewsAPI key
NEWS_API_KEY = 'f09e72c394ab40dab884afedd35db4f4'

# Global variables to store headlines for each category
sports_headlines = []
entertainment_headlines = []
politics_headlines = []
environment_headlines = []
technology_headlines = []
health_headlines = []

def fetch_headlines():
    global sports_headlines, entertainment_headlines, politics_headlines, environment_headlines, technology_headlines, health_headlines
    print("Fetching headlines...")

    # Fetch sports headlines
    sports_url = f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={NEWS_API_KEY}'
    sports_response = requests.get(sports_url)
    sports_data = sports_response.json()
    sports_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in sports_data.get('articles', [])]

    # Fetch entertainment headlines
    entertainment_url = f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={NEWS_API_KEY}'
    entertainment_response = requests.get(entertainment_url)
    entertainment_data = entertainment_response.json()
    entertainment_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in entertainment_data.get('articles', [])]

    # Fetch politics headlines
    politics_url = f'https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey={NEWS_API_KEY}'
    politics_response = requests.get(politics_url)
    politics_data = politics_response.json()
    politics_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in politics_data.get('articles', [])]

    # Fetch environment headlines
    environment_url = f'https://newsapi.org/v2/everything?q=environment&apiKey={NEWS_API_KEY}'
    environment_response = requests.get(environment_url)
    environment_data = environment_response.json()
    environment_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in environment_data.get('articles', [])]

    # Fetch technology headlines
    technology_url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={NEWS_API_KEY}'
    technology_response = requests.get(technology_url)
    technology_data = technology_response.json()
    technology_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in technology_data.get('articles', [])]

    # Fetch health headlines
    health_url = f'https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={NEWS_API_KEY}'
    health_response = requests.get(health_url)
    health_data = health_response.json()
    health_headlines = [{
        'title': article['title'],
        'url': article['url'],
        'urlToImage': article['urlToImage'],
        'description': article['description']
    } for article in health_data.get('articles', [])]

    print("Headlines updated!")

# Schedule the task to run every hour
schedule.every().hour.do(fetch_headlines)

# Function to run the scheduler in a separate thread
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def home():
    return render_template(
        'index.html',
        sports_headlines=sports_headlines,
        entertainment_headlines=entertainment_headlines,
        politics_headlines=politics_headlines,
        environment_headlines=environment_headlines,
        technology_headlines=technology_headlines,
        health_headlines=health_headlines
    )

if __name__ == '__main__':
    # Fetch headlines immediately when the app starts
    fetch_headlines()

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # Run the Flask app
    app.run(debug=True)