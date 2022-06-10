from dataclasses import dataclass

from src.dbConnections.mongoConnection import get_collection, get_database
from fastapi.encoders import jsonable_encoder
from src.generics.utils_functions import json_auto_formatter

from src.models.Notification import Notification

dbname = get_database('qm')
@dataclass
class NotificationAdapter():
    

    def create_notification_for_user(self,request:Notification):  
        collection_name = get_collection(dbname,'notification')
        collection_name.insert_one(jsonable_encoder(request))
        return True

    def get_notification_for_user(self,client_id:str):
        collection_as_list = []
        collection_name = get_collection(dbname,'notification')
        collection_details = collection_name.find({'client_id':client_id}).sort('timestamp', -1)
        collection_as_list = [x for x in collection_details]
        return json_auto_formatter(collection_as_list)

    def update_notification_for_user(self,request:Notification):
        collection_name = get_collection(dbname,'notification')
        encoded_request = jsonable_encoder(request)
        print(encoded_request)
        collection_name.update_one({'client_id':encoded_request["client_id"]},{'$set':{'title':encoded_request['title'],
        'text':encoded_request['text'],
        'timestamp':encoded_request['timestamp']}})

        return True

    def delete_notification_for_user(self,client_id:str):
        collection_name = get_collection(dbname,'notification')
        collection_name.delete_one({'client_id':client_id})
        return True