from typing import Optional, Tuple

from src.lazy_reader_db.articles_evaluated_models.article_evaluated_model import ArticleEvaluatedModel
from src.lazy_reader_db.articles_evaluated_models.utils import tuple_to_article_evaluated_model, \
    tuple_to_article_evaluated_model_many
from src.lazy_reader_db.utils.functions import execute_query, return_optional, return_many


def create_table_if_not_exists(
        psycopg2_cursor) -> None:
    query: str = """
    CREATE TABLE IF NOT EXISTS articles_evaluated_models (
        user_id INTEGER,
        guardian_id TEXT,
        model_id TEXT,
        evaluated_on TIMESTAMP,
        PRIMARY KEY (
            user_id,
            guardian_id,
            model_id,
            evaluated_on));
    """
    execute_query(query=query,
                  psycopg2_cursor=psycopg2_cursor)


def create(aem: ArticleEvaluatedModel,
           psycopg2_cursor) -> Optional[ArticleEvaluatedModel]:
    query: str = '''
    INSERT INTO articles_evaluated_models (user_id,
                                           guardian_id,
                                           model_id,
                                           evaluated_on) 
    VALUES ('{user_id_value}',
            '{guardian_id_value}',
            '{model_id_value}',
            '{evaluated_on_value}')
    ON CONFLICT (user_id, guardian_id, model_id, evaluated_on) DO NOTHING
    RETURNING *;
    '''.format(user_id_value=aem.get_user_id(),
               guardian_id_value=aem.get_guardian_id(),
               model_id_value=aem.get_model_id(),
               evaluated_on_value=aem.get_evaluated_on())

    return return_optional(query=query,
                           psycopg2_cursor=psycopg2_cursor,
                           fnc=tuple_to_article_evaluated_model)


def delete(aem: ArticleEvaluatedModel,
           psycopg2_cursor) -> Optional[ArticleEvaluatedModel]:
    query: str = '''
    DELETE FROM articles_evaluated_models
    WHERE user_id = '{user_id_value}'
          AND guardian_id = '{guardian_id_value}'
          AND model_id = '{model_id_value}'
          AND evaluated_on = '{evaluated_on_value}'
    RETURNING *;
    '''.format(user_id_value=aem.get_user_id(),
               guardian_id_value=aem.get_guardian_id(),
               model_id_value=aem.get_model_id(),
               evaluated_on_value=aem.get_evaluated_on())

    return return_optional(query=query,
                           psycopg2_cursor=psycopg2_cursor,
                           fnc=tuple_to_article_evaluated_model)


def get(user_id: int,
        psycopg2_cursor) -> Tuple[ArticleEvaluatedModel]:
    query: str = '''
    SELECT *
    FROM articles_evaluated_models
    WHERE user_id = '{user_id_value}'
    '''.format(user_id_value=user_id)

    return return_many(query=query,
                       psycopg2_cursor=psycopg2_cursor,
                       fnc=tuple_to_article_evaluated_model_many)
