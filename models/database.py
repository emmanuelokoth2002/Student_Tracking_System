import mysql.connector
import json

class Database:
    def __init__(self):
        self.dbname = "parent-student  Tracking"
        self.dbuser = "root"
        self.dbpassword = ""
        self.dbhost = "localhost"
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.dbhost,
                user=self.dbuser,
                password=self.dbpassword,
                database=self.dbname
            )
            cursor = self.conn.cursor()
            return self.conn, cursor
        except mysql.connector.Error as e:
            print("Connection failed:", e)
            raise

    def execute_query(self, query, args=None, multi=False):
        self.connect()
        cursor = self.conn.cursor()
        try:
            print("Executing query:", query)
            print("With args:", args)
            if multi:
                cursor.execute("SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")
        
            if args is not None:
                cursor.callproc(query, args) #cursor.execute(query, args, multi=multi)
            else:
                cursor.callproc(query) #cursor.execute(query, multi=multi)

            self.conn.commit()  # Always commit the transaction

            if multi:
                result = []
                for result_cursor in cursor.stored_results():
                    result.extend(result_cursor.fetchall())
                return result
        except Exception as e:
            print("Error executing query:", str(e))
            self.conn.rollback()  # Rollback the transaction in case of an error
            raise  # Re-raise the exception to handle it at a higher level
        finally:
            cursor.close()

    def get_data(self, query, args=None, multi=False):
        try:
            self.connect()  # Establish a database connection
            cursor = self.conn.cursor(dictionary=True)

            if args is not None:
                # Execute the stored procedure with parameters
                cursor.callproc(query, args)
            else:
                # Execute the stored procedure without parameters
                cursor.callproc(query)

            if multi:
                # Handle multiple result sets if needed
                result = []
                for result_cursor in cursor.stored_results():
                    result.extend(result_cursor.fetchall())
            else:
                # Fetch the result set from the stored procedure call
                result = cursor.fetchall()

            if result is None:
                result = []  # Initialize an empty list if result is None

            return result

        except Exception as e:
            print("Error executing stored procedure:", str(e))
            raise  # Re-raise the exception to handle it at a higher level
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()


    def get_json(self, query):
        data = self.get_data(query)
        json_data = json.dumps(data)
        return json_data
    
    def close_connection(self):
        if self.conn:
            self.conn.close()