from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for each_row in result:
            dojos.append(cls(each_row))
        return dojos
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        if len(result) > 0:
            one_dojo = cls(result[0])
            for row in result:
                data = {
                    **row,
                    'id' : row['ninjas.id'],
                    'created_at' : row['ninjas.created_at'],
                    'updated_at' : row['ninjas.updated_at']
                }
                one_dojo.ninjas.append(ninja_model.Ninja(data))
            return one_dojo
        return result