from secret_stuff.guardian_api import api_key_otto
from src.lazy_reader_db.users.functions import create_table_if_not_exists, create_index_name_if_not_exists, create_user
from src.lazy_reader_db.utils.functions import update_table

USER_OTTO_NAME: str = 'otto'
USER_OTTO_API_KEY: str = api_key_otto


def _1(psycopg2_cursor):
    create_table_if_not_exists(psycopg2_cursor=psycopg2_cursor)

    create_index_name_if_not_exists(psycopg2_cursor=psycopg2_cursor)

    create_user(name=USER_OTTO_NAME,
                api_key=USER_OTTO_API_KEY,
                psycopg2_cursor=psycopg2_cursor)


if __name__ == '__main__':
    update_table(_1)
