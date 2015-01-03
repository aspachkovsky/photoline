from flask import Flask, request
import pymongo
import json
from datetime import datetime
import time
from bson.objectid import ObjectId
from bson.errors import InvalidId

from werkzeug.exceptions import UnsupportedMediaType, BadRequest, MethodNotAllowed

photoline = Flask(__name__)

mongo_client = pymongo.MongoClient()
photoline_db = mongo_client.photoline
places_collection = photoline_db.places
photos_collection = photoline_db.photos
photolines_collection = photoline_db.photolines

def check_required_fields(request, required_fields):
    if not all(field in request.json for field in required_fields):
        raise BadRequest('Invalid aggregate structure: a required field missing.')

def check_excess_fields(request, fields):
    if not all(field in fields for field in request.json):
        raise BadRequest('Invalid aggregate structure: an excess field detected.')

@photoline.route('/')
def hello_world():
    return 'Hello World!\n'

@photoline.route('/photos/<photoId>/', methods = ['GET', 'PUT'])
def route_photo(photoId):
    if request.method == 'GET':
        return get_photo(photoId)
    elif request.method == 'PUT':
        return put_photo(photoId)
    else:
        raise MethodNotAllowed('Only GET and PUT methods allowed.')

def get_photo(photoId):
    if not ObjectId.is_valid(photoId):
        raise BadRequest('Invalid id value.')

    objectId = ObjectId(photoId)

    photo = photos_collection.find_one({'_id' : objectId})
    photo['_id'] = str(photo['_id'])
    return json.dumps({'photo' : photo}, indent = 4, ensure_ascii = False)

def put_photo(photoId):
    if not ObjectId.is_valid(photoId):
        raise BadRequest('Invalid id value.')

    if request.mimetype != 'application/json':
        raise UnsupportedMediaType('Only Content-Type: application/json is supported.')

    objectId = ObjectId(photoId)

    required_fields = ('userId', 'placeId')
    check_required_fields(request, required_fields)
 
    optional_fields = ('histtimestamp', 'description')
    check_excess_fields(request, required_fields + optional_fields)

    photo_aggregate = json.loads(request.data)
    photo_aggregate['timestamp'] = int(time.time())
    photo_aggregate['_id'] = objectId
    photos_collection.insert(photo_aggregate)
    photo_aggregate['_id'] = str(objectid)
    return json.dumps({'photo' : photo_aggregate}, indent = 4, ensure_ascii = False)

@photoline.route('/places/<placeId>', methods = ['GET'])
def get_place(placeId):
    if not ObjectId.is_valid(photoId):
        raise BadRequest('Invalid id value.')  
    
    objectId = ObjectId(placeId)   
    place = places_collection.find_one({'_id' : objectId})
    place['_id'] = str(place['_id'])
    return json.dumps({'place' : place}, indent = 4, ensure_ascii = False)

@photoline.route('/places', methods = ['GET', 'POST'])
def route_places():
    if request.method == 'GET':
        return get_places()
    elif request.method == 'POST':
        return post_place()
    else:
        raise MethodNotAllowed('Only GET and POST methods allowed.')

def get_places():
    if 'offset' in request.args:
        if request.args['offset'].isdigit():
            offset = int(request.args['offset'])
        else:
            raise BadRequest('Invalid argument value: offset must be a positive number.')  
    else:
        offset = 0

    if 'amount' in request.args:
        if request.args['amount'].isdigit():
            amount = int(request.args['amount'])
        else:
            raise BadRequest('Invalid argument value: amount must be a positive number.')    
    else:
        amount = 20
    
    places_cursor = places_collection.find().skip(offset).limit(amount) 

    places = []
    for place in places_cursor:
        place['_id'] = str(place['_id'])
        places.append(place)
    
    result = {'amount' : len(places), 'places' : places}

    return json.dumps(result, indent = 4, ensure_ascii = False)
   
def post_place():
    if request.mimetype != 'application/json':
        raise UnsupportedMediaType('Only Content-Type: application/json is supported.')
    
    required_fields = ('userId', 'location', 'name')
    check_required_fields(request, required_fields)
 
    optional_fields = ('address', 'description')
    check_excess_fields(reques, required_fields + optional_fields)

    place_aggregate = json.loads(request.data)
    place_aggregate['timestamp'] = int(time.time())
    placeId = str(places_collection.insert(place_aggregate))     
    return json.dumps({'userId' : place_aggregate['userId'], 'placeId' : placeId})

if __name__ == '__main__':
    photoline.debug = True
    photoline.run(host = '0.0.0.0', port = 8080)
