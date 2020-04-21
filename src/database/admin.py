from typing import List


def execute_query(query: str,
                  psycopg2_cursor) -> None:
    psycopg2_cursor.execute(query)


def drop_table(table: str,
               psycopg2_cursor) -> None:
    query: str = f'DROP TABLE IF EXISTS {table} RESTRICT;'

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def get_tables(
        psycopg2_cursor) -> List[str]:
    query: str = """
    SELECT *
    FROM information_schema.tables
    WHERE table_schema not in ('pg_catalog', 'information_schema')
          AND table_schema not like 'pg_toast%'
    """
    psycopg2_cursor.execute(query)

    return [tableTuple[2] for tableTuple in psycopg2_cursor.fetchall()]
