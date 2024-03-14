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
    long = data['longitude']
    # Process latitude and longitude variables here
    ShowMap(lat, long)
    return render_template('map.html')

@app.route('/map')
def show_map():
    # Additional processing if needed
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)

