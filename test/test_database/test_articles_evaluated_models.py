import psycopg2
import unittest

from secret_stuff.database import login_dict
from src.database.admin.get_tables import get_tables
from src.database.articles_evaluated_models import create_articles_evaluated_models


class TestArticlesEvaluatedUsers(unittest.TestCase):
    def test_it_can_create_articles_evaluated_models(self):
        try:
            connection = psycopg2.connect(**login_dict)

            cursor = connection.cursor()

            create_articles_evaluated_models(cursor)

            self.assertTrue('articles_evaluated_models' in get_tables(cursor))

        except (Exception, psycopg2.Error) as error:
            print('PostgreSQL Login Error: ', error)


if __name__ == '__main__':
    unittest.main()
