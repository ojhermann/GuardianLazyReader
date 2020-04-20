query: str = """
    CREATE TABLE IF NOT EXISTS articles_evaluated_models (
        user_id INTEGER,
        guardian_id TEXT,
        model_id TEXT,
        evaluated_on TIMESTAMP,
        PRIMARY KEY (
            user_id,
            guardian_id,
            model_id,
            evaluated_on));
    """


def create_articles_evaluated_models(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(query)
