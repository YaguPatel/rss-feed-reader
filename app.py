from flask import Flask, request, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    parsed_feed = []
    if request.method == 'POST':
        url = request.form.get('url')
        feed = fetch_feed(url)
        if feed:
            parsed_feed = parse_feed(feed)
    return render_template('index.html', parsed_feed=parsed_feed)

def fetch_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Unable to fetch feed: {e}")
        return None

def parse_feed(feed):
    try:
        root = ET.fromstring(feed)
        parsed_feed = []
        for item in root.findall(".//item"):
            title = item.find('title').text
            description = item.find('description').text
            link = item.find('link').text
            parsed_feed.append((title, description, link))
        return parsed_feed
    except Exception as e:
        print(f"Unable to parse feed: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True)
