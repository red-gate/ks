'database API'
import psycopg2

class Database():

    def __init__(self, conn_string):
        self.connection_string = conn_string

    def __connect(self):
        conn = psycopg2.connect(self.connection_string)
        return conn

    def insert_item(self, item):
        conn = self.__connect()
        cursor = conn.cursor()
        insert_statement = 'INSERT INTO todo_list (task_id, name, done) VALUES (%s, %s, %s)'
        cursor.execute(insert_statement, (item['id'], item['name'], item['done']))
        conn.commit()
        conn.close()

    def get_items(self):
        conn = self.__connect()
        cursor = conn.cursor()
        cursor.execute('SELECT task_id, name, done FROM todo_list ORDER BY task_id ASC')
        results = cursor.fetchall()
        items = []
        for result in results:
            items.append({'id': result[0], 'name': result[1], 'done': result[2]})
        return items

    def update_item(self, item):
        conn = self.__connect()
        cursor = conn.cursor()
        update_statement = 'UPDATE todo_list SET done = %s WHERE task_id = %s'
        cursor.execute(update_statement, (item['done'], item['id']))
        conn.commit()
        conn.close()

    def delete_item(self, item):
        conn = self.__connect()
        cursor = conn.cursor()
        delete_statement = 'DELETE FROM todo_list WHERE task_id = %s'
        cursor.execute(delete_statement, (item['id']))
        cursor.commit()
        conn.close()