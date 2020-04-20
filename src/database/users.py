create_users_query: str = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT);
    """


def create_users(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(create_users_query)
