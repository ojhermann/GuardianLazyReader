from src.database.utils.functions import execute_query


def create_articles(psycopg2_cursor) -> None:
    query: str = """
    CREATE TABLE IF NOT EXISTS articles (
        guardian_id TEXT,
        body_text TEXT,
        api_url TEXT,
        is_hosted BOOLEAN,
        pillar_id TEXT,
        pillar_name TEXT,
        section_id TEXT,
        section_name TEXT,
        guardian_type TEXT,
        web_publication_date TEXT,
        web_title TEXT,
        web_url TEXT,
        PRIMARY KEY (
            guardian_id));
    """
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)
