from typing import List, Optional

import psycopg2

from secret_stuff.lazy_reader_db import login_dict


def drop_table(table: str,
               psycopg2_cursor) -> None:
    query: str = f'DROP TABLE IF EXISTS {table} RESTRICT;'

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def execute_query(query: str,
                  psycopg2_cursor) -> None:
    psycopg2_cursor.execute(query)


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


def return_optional(query: str,
                    psycopg2_cursor,
                    fnc) -> Optional:
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    result = psycopg2_cursor.fetchone()

    return None if result is None else fnc(result)


def return_optionals(query: str,
                     psycopg2_cursor,
                     fnc) -> Optional:
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    result = psycopg2_cursor.fetchall()

    return None if result is None else fnc(result)


def update_table(fnc) -> None:
    connection = None

    try:
        connection = psycopg2.connect(**login_dict)

        cursor = connection.cursor()

        fnc(cursor)

        connection.commit()

    except psycopg2.DatabaseError as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
