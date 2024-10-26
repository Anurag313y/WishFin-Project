import csv

def get_cities():
    cities = []
    with open('cities.csv', mode='r') as file:
        reader = csv.DictReader(file)  # Using DictReader to handle headers
        for row in reader:
            city_id = row["id"].strip('"')  # Remove any double quotes
            city_name = row["name"].strip('"')  # Remove any double quotes
            cities.append({"id": city_id, "name": city_name})
    return cities
