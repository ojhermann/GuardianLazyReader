from src.lazy_reader_db.articles_evaluated_users.functions import create_table_if_not_exists
from src.lazy_reader_db.utils.functions import update_table


def _1(psycopg2_cursor):
    create_table_if_not_exists(psycopg2_cursor=psycopg2_cursor)


if __name__ == '__main__':
    update_table(_1)
