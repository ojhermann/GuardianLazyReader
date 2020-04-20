query: str = """
    CREATE TABLE IF NOT EXISTS articles (
        guardian_id TEXT PRIMARY KEY,
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
        web_url TEXT);
    """


def create_articles(
        psycopg2_cursor) -> None:
    psycopg2_cursor.execute(query)
