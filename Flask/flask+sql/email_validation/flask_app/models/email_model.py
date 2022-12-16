from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('emails_schema').query_db(query)
        all_emails = []
        for row in results:
            all_emails.append(Email(row))
        return all_emails
    
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('emails_schema').query_db(query,data)
        if len(results) > 0:
            one_email = Email(results[0])
            return one_email
        return False

    @classmethod
    def create(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL('emails_schema').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL('emails_schema').query_db(query,data)

    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['email']) < 1:
            is_valid = False
            flash('*Email Required')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('*Invalid Email')
        return is_valid