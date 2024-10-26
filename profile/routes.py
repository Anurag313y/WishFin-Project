from flask import Blueprint, render_template, request, redirect, jsonify
from .reader import get_cities
import csv

routes = Blueprint('routes', __name__)

@routes.route('/')
def index(error=None):
    cities = get_cities()  # Always fetch latest cities
    return render_template('index.html', cities=cities, error=error)

@routes.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    city_id = request.form.get('city')

    if not name or not city_id:
        error = "Please enter your name and select a city!"
        return index(error=error)

    # Append the name and city_id to user_profiles.csv
    with open('user_profiles.csv', 'a', newline='') as user_csvfile:
        writer = csv.writer(user_csvfile)
        writer.writerow([name, city_id])

    return redirect('/')

@routes.route('/cities', methods=['GET'])
def cities():
    cities = get_cities()  # Fetch latest cities
    return jsonify(cities)  # Return cities as JSON
