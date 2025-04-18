from Project.db import DATABASE

class User(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50), nullable = False)