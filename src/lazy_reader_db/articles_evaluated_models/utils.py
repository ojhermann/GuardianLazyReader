from datetime import datetime
from typing import Tuple

from src.lazy_reader_db.articles_evaluated_models.article_evaluated_model import ArticleEvaluatedModel


def tuple_to_article_evaluated_model(t: Tuple[int, str, str, datetime]) -> ArticleEvaluatedModel:
    return ArticleEvaluatedModel(user_id=t[0],
                                 guardian_id=t[1],
                                 model_id=t[2],
                                 evaluated_on=t[3])


def tuple_to_article_evaluated_model_many(ts: Tuple[Tuple[int, str, str, datetime]]) -> Tuple[ArticleEvaluatedModel]:
    return tuple(tuple_to_article_evaluated_model(t) for t in ts)
