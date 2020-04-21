from src.database.admin import execute_query


def create_table(psycopg2_cursor) -> None:
    query: str = '''
    create TABLE IF NOT EXISTS users (
        id SERIAL,
        name TEXT,
        PRIMARY KEY (
            id));
    '''
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def create_index_name(psycopg2_cursor) -> None:
    query: str = '''
    create INDEX IF NOT EXISTS name_index ON users (name ASC);
    '''
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)
