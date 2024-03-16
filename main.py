import os

from flask import Flask, render_template, request
from show_map import ShowMap


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geodata', methods=['POST'])
def geodata():
    data = request.get_json()
    lat = data['latitude']
    long_ = data['longitude']
    # Process latitude and longitude variables here
    show_map = ShowMap()
    map_html = show_map.make_map(lat, long_)
    return render_template('index.html', map_html=map_html)

@app.route('/map', methods=['GET', 'POST'])
def show_map():
    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Additional processing if needed
        show_map = ShowMap()
        map_html = show_map.make_map(latitude, longitude)
        return map_html
    else:
        # Handle GET request, e.g., return a form to input latitude and longitude
        return 'Please use a POST request to generate the map.'

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000), debug=True)

