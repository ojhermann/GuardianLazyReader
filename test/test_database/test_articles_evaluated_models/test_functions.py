import unittest
from datetime import datetime
from typing import Tuple, Optional

import psycopg2

from secret_stuff.lazy_reader_db import login_dict
from src.lazy_reader_db.articles_evaluated_models.article_evaluated_model import ArticleEvaluatedModel
from src.lazy_reader_db.articles_evaluated_models.functions import create, get, delete
from src.lazy_reader_db.utils.functions import get_tables


class TestFunctions(unittest.TestCase):
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()
    aem: ArticleEvaluatedModel = ArticleEvaluatedModel(user_id=12345,
                                                       guardian_id='tes_guardian_id',
                                                       model_id='test_model_id',
                                                       evaluated_on=datetime.now())

    def test_table_exists(self):
        self.assertTrue('articles_evaluated_models' in get_tables(TestFunctions.cursor))

    def test_it_can_create_and_delete(self):
        created_maybe: Optional[ArticleEvaluatedModel] = create(aem=TestFunctions.aem,
                                                                psycopg2_cursor=TestFunctions.cursor)
        self.are_equal(TestFunctions.aem, created_maybe)

        from_db: Tuple[ArticleEvaluatedModel] = get(user_id=TestFunctions.aem.get_user_id(),
                                                    psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(1, len(from_db))
        self.are_equal(TestFunctions.aem, from_db[0])
        self.are_equal(TestFunctions.aem, created_maybe)

        deleted_from_db: ArticleEvaluatedModel = delete(aem=TestFunctions.aem,
                                                        psycopg2_cursor=TestFunctions.cursor)
        self.are_equal(TestFunctions.aem, deleted_from_db)
        from_db = get(user_id=TestFunctions.aem.get_user_id(),
                      psycopg2_cursor=TestFunctions.cursor)
        self.assertFalse(from_db)

    def are_equal(self,
                  aem_one: ArticleEvaluatedModel,
                  aem_two: ArticleEvaluatedModel) -> None:
        self.assertTrue(aem_one.get_user_id(),
                        aem_two.get_user_id())
        self.assertTrue(aem_one.get_guardian_id(),
                        aem_two.get_guardian_id())
        self.assertTrue(aem_one.get_model_id(),
                        aem_two.get_model_id())
        self.assertTrue(aem_one.get_evaluated_on(),
                        aem_two.get_evaluated_on())


if __name__ == '__main__':
    unittest.main()
