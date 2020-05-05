import unittest
from datetime import datetime
from typing import Tuple, Optional

import psycopg2

from secret_stuff.lazy_reader_db import login_dict
from src.lazy_reader_db.articles_evaluated_users.article_evaluated_user import ArticleEvaluatedUser
from src.lazy_reader_db.articles_evaluated_users.functions import create_table_if_not_exists, create, get, delete
from src.lazy_reader_db.utils.functions import get_tables


class TestFunctions(unittest.TestCase):
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()
    aeu: ArticleEvaluatedUser = ArticleEvaluatedUser(user_id=12345,
                                                     guardian_id='test_it_can_create',
                                                     evaluated_on=datetime.now(),
                                                     is_liked=True)

    def test_it_can_create_table_if_not_exists(self):
        create_table_if_not_exists(psycopg2_cursor=TestFunctions.cursor)

        self.assertTrue('articles_evaluated_users' in get_tables(TestFunctions.cursor))

    def test_it_can_create_and_delete(self):
        create_table_if_not_exists(psycopg2_cursor=TestFunctions.cursor)

        created_maybe: Optional[ArticleEvaluatedUser] = create(aeu=TestFunctions.aeu,
                                                               psycopg2_cursor=TestFunctions.cursor)
        self.are_equal(TestFunctions.aeu, created_maybe)

        from_db: Tuple[ArticleEvaluatedUser] = get(aeu=TestFunctions.aeu,
                                                   psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(1, len(from_db))
        self.are_equal(TestFunctions.aeu, from_db[0])
        self.are_equal(TestFunctions.aeu, created_maybe)

        deleted_from_db: ArticleEvaluatedUser = delete(aeu=TestFunctions.aeu,
                                                       psycopg2_cursor=TestFunctions.cursor)
        self.are_equal(TestFunctions.aeu, deleted_from_db)
        from_db = get(aeu=TestFunctions.aeu,
                      psycopg2_cursor=TestFunctions.cursor)
        self.assertFalse(from_db)

    def are_equal(self,
                  aeu_one: ArticleEvaluatedUser,
                  aeu_two: ArticleEvaluatedUser) -> None:
        self.assertTrue(aeu_one.get_user_id(),
                        aeu_two.get_user_id())
        self.assertTrue(aeu_one.get_guardian_id(),
                        aeu_two.get_guardian_id())
        self.assertTrue(aeu_one.get_evaluated_on(),
                        aeu_two.get_evaluated_on())
        self.assertTrue(aeu_one.is_liked(),
                        aeu_two.is_liked())


if __name__ == '__main__':
    unittest.main()
