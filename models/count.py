from config.mysqlconnection import connectToMySQL

class Count:
    DB = 'flask_counter'
    def __init__( self , data ):
        self.id = data['id']
        self.actual_count = data['actual_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #check
    @classmethod
    def return_count(cls):
        query = "SELECT actual_count FROM counter;"
        results = connectToMySQL(cls.DB).query_db(query)
        return results
    
    #increment count by one
    #UPDATE
    @classmethod
    def add_one(cls, data):
        query = """UPDATE counter
            SET actual_count = %(actual_count)s
            WHERE id = 1;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    #check
    @classmethod
    def reset_actual_count(cls):
        query = """UPDATE counter SET actual_count = 0 WHERE id = 1;"""
        return connectToMySQL(cls.DB).query_db(query)