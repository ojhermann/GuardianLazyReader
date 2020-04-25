from src.lazy_reader_db.utils.functions import execute_query


def create_guardian_content_if_not_exists(psycopg2_cursor) -> None:
    query: str = """
    CREATE TABLE IF NOT EXISTS guardian_content (
        api_url TEXT,
        body_text TEXT,
        guardian_id TEXT,
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


def create_index_web_publication_date_if_not_exists(psycopg2_cursor) -> None:
    query: str = '''
    create INDEX IF NOT EXISTS web_publication_date_index ON guardian_content (web_publication_date DESC);
    '''
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)
