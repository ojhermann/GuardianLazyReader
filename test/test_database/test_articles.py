import psycopg2
import unittest

from secret_stuff.database import login_dict
from src.database.admin.get_tables import get_tables
from src.database.articles import create_articles


class TestArticlesEvaluatedUsers(unittest.TestCase):
    def test_it_can_create_articles(self):
        try:
            connection = psycopg2.connect(**login_dict)

            cursor = connection.cursor()

            create_articles(cursor)

            self.assertTrue('articles' in get_tables(cursor))

        except (Exception, psycopg2.Error) as error:
            print('PostgreSQL Login Error: ', error)


if __name__ == '__main__':
    unittest.main()
