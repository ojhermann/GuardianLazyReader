from typing import List

query: str = """
    SELECT *
    FROM information_schema.tables
    WHERE table_schema not in ('pg_catalog', 'information_schema')
          AND table_schema not like 'pg_toast%'
    """


def get_tables(
        psycopg2_cursor) -> List[str]:
    psycopg2_cursor.execute(query)

    return [tableTuple[2] for tableTuple in psycopg2_cursor.fetchall()]
