from datetime import datetime
from typing import Tuple

from src.lazy_reader_db.articles_evaluated_users.article_evaluated_user import ArticleEvaluatedUser


def tuple_to_article_evaluated_user(t: Tuple[int, str, datetime, bool]) -> ArticleEvaluatedUser:
    return ArticleEvaluatedUser(user_id=t[0],
                                guardian_id=t[1],
                                evaluated_on=t[2],
                                is_liked=t[3])


def tuple_to_article_evaluated_user_many(ts: Tuple[Tuple[int, str, datetime, bool]]) -> Tuple[ArticleEvaluatedUser]:
    return tuple(tuple_to_article_evaluated_user(t) for t in ts)
