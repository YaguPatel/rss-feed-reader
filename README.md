# rss-feed-reader

This project is a simple RSS Feed Reader built using Python and Flask. The application fetches an RSS feed from a user-provided URL, parses the feed, and displays the title, description, and link for each item in the feed.

Getting Started

These instructions will get you a copy of the project up and running on your local machine.

Prerequisites

You'll need the following installed:

Python 3.6 or later

Flask

You can install Flask using pip:

Copy code

pip install flask

Installing

To run this project, follow these steps:


Clone this repository to your local machine.

Navigate to the project directory in your terminal.

Run the following command to start the Flask server:

Copy code

python app.py

Open a web browser and navigate to http://localhost:5000.

Usage

To use the RSS Feed Reader:


Enter an RSS feed URL in the form on the homepage and click "Fetch feed".

The title, description, and link for each item in the feed will be displayed below the form.

Built With

Python - The programming language used.

Flask - The web framework used.

xml.etree.ElementTree - The XML parsing library used.
