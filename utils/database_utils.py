import psycopg2
from psycopg2.extras import RealDictCursor


def get_data_base_connection(host_ip):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname="mcp_production",
            user="postgres",
            password="P@ssw0rd",
            host=host_ip,  # "10.121.105.218"
            port="5432",
        )
    except psycopg2.Error as e:
        print("Error: ", e)
    finally:
        return connection


def get_data_from_table(host_ip, query_statement):
    connection = get_data_base_connection(host_ip)
    result_set = None
    cursor = None
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_statement)
        result_set = cursor.fetchall()
    except psycopg2.Error as e:
        print("Error : ", e)
    finally:
        if cursor != None:
            cursor.close()
        return result_set
