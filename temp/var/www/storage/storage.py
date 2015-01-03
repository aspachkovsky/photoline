from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType, NotFound, BadRequest
import json
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient()
photostorage_db = client.photostorage
photostorage_fs = gridfs.GridFS(photostorage_db)

photostorage = Flask(__name__)

@photostorage.route('/', methods = ['GET'])
def hello_world():
    return 'Hello from storage!\n'

@photostorage.route('/photos/<photoId>', methods = ['GET'])
def get_photo(photoId):
    try:
        objectId = ObjectId(photoId)
    except InvalidId:
        raise BadRequest('Invalid id value.')

    if photostorage_fs.exists(objectId):
        gridout_file = photostorage_fs.get(objectId)
        return gridout_file.read()
    else:
        raise NotFound('Image file not found by id.')

@photostorage.route('/photos', methods = ['POST'])
def post_photo():
    gridin_file = photostorage_fs.new_file(content_type = request.headers['Content-Type'])    
    db_request = client.start_request()
    try:
        gridin_file.write(request.data)
        gridin_file.close()
    finally:
        db_request.end()
    photoId = str(gridin_file._id)
    return json.dumps({ 'photoId' : photoId }, indent = 4, ensure_ascii = False)

if __name__ == '__main__':
    photostorage.debug = True
    photostorage.run(host = '0.0.0.0', port = 8080)