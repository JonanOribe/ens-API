from pymongo import MongoClient
from src.generics.security_layer import cipher_data, get_decoded_data
from src.generics.utils_functions import get_config_file_data, json_auto_formatter

config,config_file = get_config_file_data()
config.read(config_file)

user:bytes = str.encode('')
password:bytes = str.encode('')
mongo_cluster:bytes = str.encode('')

nonce_user,ciphertext_user,tag_user = cipher_data(user)
nonce_pass,ciphertext_pass,tag_pass = cipher_data(password)
nonce_mongo_cluster,ciphertext_mongo_cluster,tag_mongo_cluster = cipher_data(mongo_cluster)

def get_database(db:str):

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://{user}:{password}@{mongo_cluster}/{db}?retryWrites=true&w=majority".format(
        user = get_decoded_data(nonce_user,ciphertext_user,tag_user), password = get_decoded_data(nonce_pass,ciphertext_pass,tag_pass),
        mongo_cluster = get_decoded_data(nonce_mongo_cluster,ciphertext_mongo_cluster,tag_mongo_cluster), db = db)

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[db]
    
def get_collection(db,collec:str):
    return db[collec]