from typing import Optional, Tuple

from src.lazy_reader_db.articles_evaluated_users.article_evaluated_user import ArticleEvaluatedUser
from src.lazy_reader_db.articles_evaluated_users.utils import tuple_to_article_evaluated_user, \
    tuple_to_article_evaluated_user_many
from src.lazy_reader_db.utils.functions import execute_query, return_optional, return_optionals


def create_table_if_not_exists(
        psycopg2_cursor) -> None:
    query: str = """
    CREATE TABLE IF NOT EXISTS articles_evaluated_users (
        user_id INTEGER,
        guardian_id TEXT,
        evaluated_on TIMESTAMP,
        is_liked BOOLEAN,
        PRIMARY KEY (
            user_id,
            guardian_id,
            evaluated_on));
    """
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def create(aeu: ArticleEvaluatedUser,
           psycopg2_cursor) -> Optional[ArticleEvaluatedUser]:
    query: str = '''
    INSERT INTO articles_evaluated_users (user_id,
                                          guardian_id,
                                          evaluated_on,
                                          is_liked) 
    VALUES ('{user_id_value}',
            '{guardian_id_value}',
            '{evaluated_on_value}',
            '{is_liked_value}')
    ON CONFLICT (user_id, guardian_id, evaluated_on) DO NOTHING
    RETURNING *;
    '''.format(user_id_value=aeu.get_user_id(),
               guardian_id_value=aeu.get_guardian_id(),
               evaluated_on_value=aeu.get_evaluated_on(),
               is_liked_value=aeu.is_liked())

    return return_optional(query=query,
                           psycopg2_cursor=psycopg2_cursor,
                           fnc=tuple_to_article_evaluated_user)


def delete(aeu: ArticleEvaluatedUser,
           psycopg2_cursor) -> Optional[ArticleEvaluatedUser]:
    query: str = '''
    DELETE FROM articles_evaluated_users
    WHERE user_id = '{user_id_value}'
          AND guardian_id = '{guardian_id_value}'
          AND evaluated_on = '{evaluated_on_value}'
    RETURNING *;
    '''.format(user_id_value=aeu.get_user_id(),
               guardian_id_value=aeu.get_guardian_id(),
               evaluated_on_value=aeu.get_evaluated_on())

    return return_optional(query=query,
                           psycopg2_cursor=psycopg2_cursor,
                           fnc=tuple_to_article_evaluated_user)


def get(aeu: ArticleEvaluatedUser,
        psycopg2_cursor) -> Tuple[ArticleEvaluatedUser]:
    query: str = '''
    SELECT *
    FROM articles_evaluated_users
    WHERE user_id = '{user_id_value}'
          AND guardian_id = '{guardian_id_value}'
          AND evaluated_on = '{evaluated_on_value}'
    '''.format(user_id_value=aeu.get_user_id(),
               guardian_id_value=aeu.get_guardian_id(),
               evaluated_on_value=aeu.get_evaluated_on())

    return return_optionals(query=query,
                            psycopg2_cursor=psycopg2_cursor,
                            fnc=tuple_to_article_evaluated_user_many)
