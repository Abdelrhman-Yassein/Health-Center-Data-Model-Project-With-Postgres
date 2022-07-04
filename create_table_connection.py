import psycopg2 as ps
from create_table_sql_file import create_table_queries
from drop_table_sql_file import drop_table_queries
from insert_sql_query import insert_queries

def Create_Database_connection():
    """
    This Function 
    1-connect to deault postgres database
    2-Drop Database If Exists
    3-Create New DAtabase
    4-Connection to new database

    Returns:
        conn: connection to databse
        cur : cursoer 
    """
    # connect to default database
    conn = ps.connect(password="postgres", user="postgres", host="127.0.0.1")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create health center database
    cur.execute("DROP DATABASE IF EXISTS helth_center ")
    cur.execute(
        "CREATE DATABASE helth_center WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to helth center database
    conn = ps.connect(user="postgres", password="postgres",
                      database="helth_center", host="127.0.0.1")
    cur = conn.cursor()

    return cur, conn


def Drop_tables(cur, conn):
    """[summary]
    this function execute drop table query
    Args:
        cur :to execute query
        conn : connection to database
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def Create_table(cur, conn):
    """[summary]
    this function execute create table query
    Args:
        cur :to execute query
        conn : connection to database
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def Insert_into_table(cur, conn):
    """[summary]
    this function execute insert into table query
    Args:
        cur :to execute query
        conn : connection to database
    """
    for query in insert_queries:
        cur.execute(query)
        conn.commit()        


def main():
    """[summary]
        this function create a new database and connection 
        and related table
    """
    cur, conn = Create_Database_connection()
    Drop_tables(cur, conn)
    Create_table(cur, conn)


if __name__ == '__main__':
    main()
