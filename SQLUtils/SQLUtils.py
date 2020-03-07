import mysql.connector


class SQL:

    def __init__(self, host, db, user, password):
        self.conn = mysql.connector.connect(host=host, database=db, user=user, password=password)

    def insert(self, origin, data_type, data):
        cursor = self.conn.cursor()
        query = 'INSERT INTO SENSOR_DATA (origin, data_type, data)  VALUES (%s, %s, %s);'
        _tuple = (origin, data_type, data)
        cursor.execute(query, _tuple)
        self.conn.commit()
