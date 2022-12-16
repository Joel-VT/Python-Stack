from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
                }
            recipe.user = user_model.User(data)
            all_recipes.append(recipe)
        return all_recipes
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name,description,instructions,date_cooked,under_30,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_cooked)s,%(under_30)s,%(user_id)s);"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if len(results) > 0:
            print(results)
            recipe = cls(results[0])
            data = {
                **results[0],
                'id' : results[0]['users.id'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at']
                }
            recipe.user = user_model.User(data)
            return recipe
        return False
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['name']) < 1:
            flash('*Name is required', 'rname')
            is_valid = False
        elif len(data['name']) < 3:
            flash('*Name should be atleast 3 characters' , 'rname')
            is_valid = False
        if len(data['description']) < 1:
            flash('*Description is required', 'description')
            is_valid = False
        elif len(data['description']) < 3:
            flash('*Description should be atleast 3 characters' , 'description')
            is_valid = False
        if len(data['instructions']) < 1:
            flash('*Instructions is required', 'instructions')
            is_valid = False
        elif len(data['instructions']) < 3:
            flash('*Instructions should be atleast 3 characters' , 'instructions')
            is_valid = False
        if len(data['date_cooked']) < 1:
            flash('*Date is required', 'date')
            is_valid = False
        if not 'under_30' in data:
            flash('*Choose Yes or No', 'under')
            is_valid = False
        return is_valid

