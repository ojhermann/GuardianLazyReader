from src.lazy_reader_db.guardian_content.functions import create_guardian_content_if_not_exists, \
    create_index_web_publication_date_if_not_exists
from src.lazy_reader_db.utils.functions import update_table


def _1(psycopg2_cursor):
    create_guardian_content_if_not_exists(psycopg2_cursor)


def _2(psycopg2_cursor):
    create_index_web_publication_date_if_not_exists(psycopg2_cursor)


if __name__ == '__main__':
    update_table(_1)
    update_table(_2)
