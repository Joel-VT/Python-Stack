from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_and_registration').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_and_registration').query_db(query,data)
        if len(results) > 0:
            return User(results[0])
        return False

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_and_registration').query_db(query,data)
        if len(results) > 0:
            return User(results[0])
        return False
    
    @classmethod
    def create(cls,data):
        
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL('login_and_registration').query_db(query,data)
    
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['first_name']) < 1:
            flash('*First name required', 'first')
            is_valid = False
        elif len(data['first_name']) < 2:
            flash('*First name has to be at least 2 characters', 'first')
            is_valid = False
        elif not data['first_name'].isalpha():
            flash('*First name should comprise of alphabets only', 'first')
            is_valid = False
        if len(data['last_name']) < 1:
            flash('*Last name required', 'last')
            is_valid = False
        elif len(data['last_name']) < 2:
            flash('*Last name has to be at least 2 characters', 'last')
            is_valid = False
        elif not data['last_name'].isalpha():
            flash('*Last name should comprise of alphabets only', 'last')
            is_valid = False
        if len(data['email']) < 1:
            is_valid = False
            flash('*Email Required', 'email')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('*Invalid Email', 'email')
        if len(data['password']) < 1:
            flash('*Password required', 'pass')
            is_valid = False
        elif len(data['password']) < 8:
            flash('*Password has to be at least 8 characters', 'pass')
            is_valid = False
        elif not any(ele.isupper() for ele in data['password']):
            flash('*Password must contain atleast one upper case', 'pass')
            is_valid = False
        elif not any(ele.isnumeric() for ele in data['password']):
            flash('*Password must contain atleast one number', 'pass')
            is_valid = False
        if len(data['confirm_password']) < 1:
            flash('*Confirm Password', 'confirm')
            is_valid = False
        elif data['password'] != data['confirm_password']:
            flash('*Paswords dont match', 'confirm')
            is_valid = False
        return is_valid


    