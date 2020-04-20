query: str = """
    CREATE TABLE IF NOT EXISTS articles_evaluated_users (
        user_id INTEGER,
        article_id TEXT,
        evaluated_on TIMESTAMP,
        liked BOOLEAN,
        PRIMARY KEY (
            user_id,
            article_id,
            evaluated_on));
    """


def create_articles_evaluated_users(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(query)
