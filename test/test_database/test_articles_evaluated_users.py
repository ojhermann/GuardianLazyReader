import psycopg2
import unittest

from secret_stuff.database import login_dict
from src.database.admin.get_tables import get_tables
from src.database.articles_evaluated_users import create_articles_evaluated_users


class TestArticlesEvaluatedUsers(unittest.TestCase):
    def test_it_can_create_articles_evaluated_users(self):
        try:
            connection = psycopg2.connect(**login_dict)

            cursor = connection.cursor()

            create_articles_evaluated_users(cursor)

            self.assertTrue('articles_evaluated_users' in get_tables(cursor))

        except (Exception, psycopg2.Error) as error:
            print('PostgreSQL Login Error: ', error)


if __name__ == '__main__':
    unittest.main()
