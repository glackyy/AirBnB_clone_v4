#!/usr/bin/python3
"""flask app that integrates with AirBnB static html template"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session"""
    storage.close()


@app.route('/0-hbnb/')
def hbnb_filters(the_id=None):
    """handling request to custom template with states, cities & amentities"""
    st_objs = storage.all('State').values()
    states = dict([st.name, st] for st in st_objs)
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """Main Flask app"""
    app.run(host=host, port=port)
