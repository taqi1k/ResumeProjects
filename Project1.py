import flask
import hashlib
from flask import jsonify
from flask import request
from sql import create_connection, execute_query
from sql import execute_read_query

app = flask.Flask(__name__)  # Created the Application
app.config["DEBUG"] = True

username = "admin"
password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

# Login

@app.route('/', methods=['GET'])
def auth_flights():
    if request.authorization:
        encoded = request.authorization.password.encode() 
        hashedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == username and hashedResult.hexdigest() == password:
            return '<h1> WE ARE ALLOWED TO BE HERE </h1>'
    return ('COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

# Show Flights once Logged in

@app.route('/api/flights', methods=["GET"])
def get_flights():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    sql = "SELECT * from flights"
    gem = execute_read_query(conn, sql)              
    return jsonify(gem) 

# View The Planes
@app.route('/api/planes', methods=["GET"])
def get_planes():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    sql = "SELECT * from planes"
    gem = execute_read_query(conn, sql)
    return jsonify(gem)

# Post a Plane
@app.route('/api/planes', methods=["POST"])
def post_plane():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    make = request_data['make']
    model = request_data['model']
    year = request_data['year']
    capacity = request_data['capacity']

    sql = "INSERT into planes (make, model, year, capacity) VALUES ('%s', '%s', '%s', '%s')" % (make, model, year, capacity)
    execute_query(conn, sql)
    return "Plane Added Successfully!"

# Delete a Plane
@app.route('/api/planes', methods=["DELETE"])
def delete_plane():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    id = request_data['id']
    sql = "DELETE from planes WHERE id = %s" % (id)
    execute_query(conn, sql)
    return "Plane Removed Successfully"

# Update a Planes Capacity
@app.route('/api/planes', methods=["PUT"])
def update_plane():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    id = request_data["id"]
    capacity = request_data["capacity"]

    sql = "UPDATE from planes SET capacity = %s WHERE id = %s" % (capacity, id)
    execute_query(conn, sql)
    return "Plane Updated Successfully"

# View the Airports
@app.route('/api/airports', methods=["GET"])
def get_airports():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    sql = "SELECT * from airports"
    gem = execute_read_query(conn, sql)
    return jsonify(gem) 

# Post a Airport
@app.route('/api/airports', methods=["POST"])
def post_airport():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    airportcode = request_data['airportcode']
    airportname = request_data['airportname']
    country = request_data['country']

    sql = "INSERT into airports (airportcode, airportname, country) VALUES ('%s', '%s', '%s')" % (airportcode, airportname, country)
    execute_query(conn, sql)
    return "Airport Added Successfully"

# Delete a Airport
@app.route('/api/airports', methods=["DELETE"])
def delete_airport():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    id = request_data['id']
    sql = "DELETE from airports WHERE id = %s" % (id)
    execute_query(conn, sql)
    return "Airport Removed Successfully"

# Update a Airports Code
@app.route('/api/airports', methods=["PUT"])
def update_airport():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    id = request_data["id"]
    airportcode = request_data["airportcode"]

    sql = "UPDATE from planes SET airportcode = %s WHERE id = %s" % (airportcode, id)
    execute_query(conn, sql)
    return "Airport Updated Successfully"

# Post a Flight 
@app.route('/api/flights', methods=["POST"])
def post_flight():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    planeid = request_data['planeid']
    airporttoid = request_data['airporttoid']
    airportfromid = request_data['airportfromid']
    date = request_data['date']

    sql = "INSERT into flights (planeid, airporttoid, airportfromid, date) VALUES (%s, %s, %s, '%s')" % (planeid, airporttoid, airportfromid, date)
    execute_query(conn, sql)
    return "Flight Added Successfully"

# Delete a Flight
@app.route('/api/flights', methods=["DELETE"])
def delete_flight():
    conn = create_connection('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
    request_data = request.get_json()
    id = request_data['id']
    sql = "DELETE from flights WHERE id = %s" % (id)
    execute_query(conn, sql)
    return "Flight Removed Successfully"


app.run()