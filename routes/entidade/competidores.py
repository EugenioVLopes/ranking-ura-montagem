import pymongo
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from bson.objectid import ObjectId

competidores_routes = Blueprint('competidores_routes', __name__)

# conexao = pymongo.MongoClient(
#     host =  'localhost',
#     port = 27017
# )
    
conexao = pymongo.MongoClient(
    host = 'roundhouse.proxy.rlwy.net',
    port = 54006,
    username = "mongo",
    password = "44BCEhBbB52FB3GcFbHh5aHEb-12fe2E"
)

# class Competidor(MethodView):

db = conexao.get_database('ranking_ura')
collection_competidores = db.get_collection('ura_competidores_dia1')

@competidores_routes.route('/api/competidor/add', methods = ['POST'])
def adicionar_competidor():
    
    # Receiving Data
    dados_recebidos = request.json

    nome = dados_recebidos['nome']
    tempo = dados_recebidos['tempo']

    collection_competidores.insert_one(
        {
            "nome": nome,
            "tempo" : tempo
        }
    )  
    response = jsonify(
        {
            "nome": nome,
            "tempo" : tempo
        }
    )
    response.status_code = 201
        
    return response

@competidores_routes.route('/api/competidores', methods=['GET'])
def get_competidores():
    
    competidor = list(collection_competidores.aggregate([
        {
            "$sort" : {
                "tempo" : 1
            }
        },
        {
            "$project" : {
                "_id" : {"$toString" : "$_id"},
                "nome": 1,
                "tempo" : 1
            }
        }
    ]))
    
    return jsonify(competidor)

@competidores_routes.route('/api/competidores/<_id>', methods=['GET'])
def get_competidores_id(_id):
    
    competidor = collection_competidores.find_one(
        {
            "_id" : ObjectId(_id)
        },
        {
            "_id" : {"$toString" : "$_id"},
            "nome": 1,
            "tempo" : 1
        }
    )
    
    return jsonify(competidor)

@competidores_routes.route('/api/competidor', methods=['PUT'])
def put_competidor():

    dados_recebidos = request.json

    _id = dados_recebidos["_id"]
    novo_tempo = dados_recebidos["tempo"]
    
    collection_competidores.update_one(
        {
            "_id": ObjectId(_id) 
        },
        {"$set":
            {
                "tempo" : novo_tempo
            }
        }
    )
    response = jsonify({'message': 'Competidor: ' + _id + 'Updated Successfuly'})
        
    return response

@competidores_routes.route('/api/competidor', methods=['DELETE'])
def delete_competidor():

    dados_recebidos = request.json

    _id = dados_recebidos["_id"]
    
    collection_competidores.delete_one(
        {
            "_id": ObjectId(_id) 
        }
    )
    response = jsonify({'message': 'Competidor: ' + _id + ' DELETADO!!!'})
        
    return response