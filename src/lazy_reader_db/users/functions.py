from typing import Optional, Tuple

from src.lazy_reader_db.users.user import User
from src.lazy_reader_db.utils.functions import execute_query


def create_table_if_not_exists(psycopg2_cursor) -> None:
    query: str = '''
    create TABLE IF NOT EXISTS users (
        id SERIAL,
        name TEXT UNIQUE,
        api_key TEXT,
        deleted BOOLEAN,
        PRIMARY KEY (
            id));
    '''
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def create_index_name_if_not_exists(psycopg2_cursor) -> None:
    query: str = '''
    create INDEX IF NOT EXISTS name_index ON users (name ASC);
    '''
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def create_user(name: str,
                api_key: str,
                psycopg2_cursor) -> Optional[User]:
    query: str = '''
    INSERT INTO users (name, api_key, deleted) 
    VALUES ('{name_value}', '{api_key_value}', FALSE)
    ON CONFLICT (name) DO NOTHING
    RETURNING *;
    '''.format(name_value=name,
               api_key_value=api_key)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])


def delete_user(name: str,
                psycopg2_cursor) -> Optional[User]:
    query: str = '''
    UPDATE users
    SET deleted = True
    WHERE name = '{name_value}'
    RETURNING *;
    '''.format(name_value=name)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])


def get_user_by_id(id: int,
                   psycopg2_cursor) -> Optional[User]:
    query: str = '''
    SELECT *
    FROM users
    WHERE id = '{id_value}';
    '''.format(id_value=id)
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])


def get_user_by_name(name: str,
                     psycopg2_cursor) -> Optional[User]:
    query: str = '''
    SELECT *
    FROM users
    WHERE name = '{name}';
    '''.format(name=name)
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])


def resurrect_user(name: str,
                   psycopg2_cursor) -> Optional[User]:
    query: str = '''
    UPDATE users
    SET deleted = False
    WHERE name = '{name_value}'
    RETURNING *;
    '''.format(name_value=name)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])


def update_user_api_key(name: str,
                        api_key: str,
                        psycopg2_cursor) -> Optional[User]:
    query: str = '''
    UPDATE users
    SET api_key = '{api_key_value}'
    WHERE name = '{name_value}'
    RETURNING *;
    '''.format(name_value=name,
               api_key_value=api_key)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[int, str, str, bool] = psycopg2_cursor.fetchone()

    return None if t is None else User(id=t[0], name=t[1], api_key=t[2], deleted=t[3])
