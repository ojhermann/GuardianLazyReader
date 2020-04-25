from src.lazy_reader_db.utils.functions import execute_query


def create_articles_evaluated_users(
        psycopg2_cursor) -> None:
    query: str = """
    CREATE TABLE IF NOT EXISTS articles_evaluated_users (
        user_id INTEGER,
        guardian_id TEXT,
        evaluated_on TIMESTAMP,
        liked BOOLEAN,
        PRIMARY KEY (
            user_id,
            guardian_id,
            evaluated_on));
    """
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)
