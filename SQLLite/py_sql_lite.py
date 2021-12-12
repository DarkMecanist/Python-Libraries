import sqlite3
from builtins import Exception


class SQLLite:
    """
    SQL Lite
    """

    def __init__(self, database_path):
            self.connection = sqlite3.connect(database_path)

    def create_table(self, table_name=None, schema=None, query=None, close_connection=False):
        """
        :param table_name: [String]
        :param schema: [Dictionary {String: List}]
        example schema: {col_name: [type, default]}
        :param close_connection: [Boolean]
        :param query: [String]
        """

        if not table_name and schema:
            raise Exception("No table name provided. This is mandatory if using schema.")

        if not schema and not query:
            raise Exception("No schema or query provided. Provide only one.")

        if schema and query:
            raise Exception("Both schema and query provided. Provide only one.")

        if not query:
            query = f"CREATE TABLE {table_name} ("

            for col in schema.keys():
                query += f"{col} {schema[col][0]} {schema[col][1]}, "

            query = query.rstrip(", ") + ")"

        cursor = self.connection.cursor()
        cursor.execute(query)

        if close_connection:
            self.connection.close()

    def execute_query(self, query=None, parameters=None, close_connection=False):
        """
        :param query: [String]
        :param parameters: [Dictionary {String: Object}]
        :param close_connection: [Boolean]
        :return: result
        """

        if not query:
            raise Exception("No query provided.")

        cursor = self.connection.cursor()

        if not parameters:
            result = cursor.execute(query).fetchall()
        else:
            result = cursor.execute(query, parameters).fetchall()

        self.connection.commit()

        if close_connection:
            self.connection.close()

        return result
