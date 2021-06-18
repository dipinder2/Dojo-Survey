from ..config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.fav_language = data["fav_language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    
    @classmethod
    def insert_user(cls, data):
        q = "INSERT INTO users(name,location,fav_language,"\
            "comment,created_at,updated_at) VALUES("\
            "%(name)s,%(location)s,%(fav_language)s,%(comment)s,NOW(),NOW());"
        res = connectToMySQL("dojo_survey_schema").query_db(q,data)
        return res
    
    
    @classmethod
    def get_one(cls,data):
        q = "SELECT * FROM users WHERE id = %(id)s;"
        res = connectToMySQL("dojo_survey_schema").query_db(q,data)
        return cls(res[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if(len(user['name'])<2):
            is_valid=False
            flash("Name must be more than 2 characters")
        
        return is_valid