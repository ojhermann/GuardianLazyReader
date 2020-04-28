from typing import Tuple, Optional

import psycopg2
from guardian_api.main.guardian_api import GuardianApi
from guardian_api.main.guardian_content import GuardianContent

from secret_stuff.guardian_api import api_key_otto
from secret_stuff.lazy_reader_db import login_dict
from src.lazy_reader_db.guardian_content.utils import tuple_to_guardian_content
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


def create_guardian_content(gc: GuardianContent,
                            psycopg2_cursor) -> Optional[GuardianContent]:
    query: str = '''
        INSERT INTO guardian_content (api_url, 
                                      body_text, 
                                      guardian_id, 
                                      is_hosted, 
                                      pillar_id, 
                                      pillar_name, 
                                      section_id, 
                                      section_name, 
                                      guardian_type, 
                                      web_publication_date, 
                                      web_title, 
                                      web_url) 
        VALUES ( '{api_url}', 
                 '{body_text_value}', 
                 '{guardian_id_value}', 
                 '{is_hosted_value}', 
                 '{pillar_id_value}', 
                 '{pillar_name_value}', 
                 '{section_id_value}', 
                 '{section_name_value}', 
                 '{guardian_type_value}', 
                 '{web_publication_date_value}', 
                 '{web_title_value}', 
                 '{web_url_value}') 
        ON CONFLICT (guardian_id) DO NOTHING
        RETURNING *;
        '''.format(api_url=gc.get_api_url(),
                   body_text_value=gc.get_body_text(),
                   guardian_id_value=gc.get_guardian_id(),
                   is_hosted_value=gc.get_is_hosted(),
                   pillar_id_value=gc.get_pillar_id(),
                   pillar_name_value=gc.get_pillar_name(),
                   section_id_value=gc.get_section_id(),
                   section_name_value=gc.get_section_name(),
                   guardian_type_value=gc.get_guardian_type(),
                   web_publication_date_value=gc.get_web_publication_date(),
                   web_title_value=gc.get_web_title(),
                   web_url_value=gc.get_web_url())

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[str, str, str, str, bool, str, str, str, str, str, str, str, str] = psycopg2_cursor.fetchone()

    return None if t is None else tuple_to_guardian_content(t)


def delete_guardian_content(guardian_id: str,
                            psycopg2_cursor) -> Optional[GuardianContent]:
    query: str = '''
    DELETE FROM guardian_content
    WHERE guardian_id = '{guardian_id_value}'
    RETURNING *;
    '''.format(guardian_id_value=guardian_id)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[str, str, str, str, bool, str, str, str, str, str, str, str, str] = psycopg2_cursor.fetchone()

    return None if t is None else tuple_to_guardian_content(t)


def get_guardian_content(guardian_id: str,
                         psycopg2_cursor) -> Optional[GuardianContent]:
    query: str = '''
    SELECT *
    FROM guardian_content
    WHERE guardian_id = '{guardian_id_value}';
    '''.format(guardian_id_value=guardian_id)

    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)

    t: Tuple[str, str, str, str, bool, str, str, str, str, str, str, str, str] = psycopg2_cursor.fetchone()

    return None if t is None else tuple_to_guardian_content(t)


if __name__ == '__main__':
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()

    ga: GuardianApi = GuardianApi(guardian_api_key=api_key_otto)
    gcs = ga.generate_multiple_items(guardian_response=ga.get_response()).get_content()
    gc = gcs[0]

    gct = create_guardian_content(gc, cursor)

    print(type(gct))

    print(gct)
