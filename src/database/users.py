create_users_query: str = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL,
        name TEXT,
        PRIMARY KEY (
            id));
    """

create_index_name_query: str = """
    CREATE INDEX IF NOT EXISTS name_index ON users (name ASC);
"""


def create_users(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(create_users_query)


def create_index_name(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(create_index_name_query)
