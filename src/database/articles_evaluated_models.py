from src.database.utils.functions import execute_query


def create_articles_evaluated_models(
        psycopg2_cursor) -> None:
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

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)
