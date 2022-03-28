import json
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# uri = 'mongodb://rasa-db-shard-00-02.457iv.mongodb.net:27017/admin'
client = pymongo.MongoClient("mongodb+srv://Naruedee:nnew.w06@rasa-db.457iv.mongodb.net/rasadb?retryWrites=true&w=majority")
# client = MongoClient( uri )
db = client.get_database("rasa-db-test1")

class StockRepository:

    # @staticmethod
    # def check_tel(tel):
    #     all_user = db.get_collection("User")
    #     user = all_user.find_one({"user_tel": tel})
    #     return user

    @staticmethod
    def add_user(jsonreq):
        all_user = db.get_collection("User")
        if all_user.find_one({"user_tel": jsonreq["user_tel"]}) == None:
            all_user.insert_one({"_id": ObjectId(),
                                "user_tel": jsonreq["user_tel"],
                                "title": jsonreq["title"],
                                "name": jsonreq["name"],
                                "surname": jsonreq["surname"],
                                "Address": "",
                                "Amphoe" :"",
                                "Tambol" :"",
                                "Province" :"",
                                "Zipcode":""})
            return "register complete"
        else:
            return "this number already have account"

    @staticmethod
    def retrieve_profile(tel):
        all_user = db.get_collection("User")
        user = all_user.find_one({"user_tel": tel})
        if user != None:
            user.pop("_id", None)
        return user

    @staticmethod
    def update_profile(jsonreq):
        all_user = db.get_collection("User")
        user = all_user.find_one({"user_tel": jsonreq["user_tel"]})
        if user != None:
            _id = user["_id"]
            all_user.update_one({"_id": _id},
                            {"$set": {"title": jsonreq["title"],
                                    "name": jsonreq["name"],
                                    "surname": jsonreq["surname"],
                                    "Address": jsonreq["Address"],
                                    "Amphoe": jsonreq["Amphoe"],
                                    "Tambol": jsonreq["Tambol"],
                                    "Zipcode": jsonreq["Zipcode"]}})
            return "update complete"
        else:
            return "not found user"