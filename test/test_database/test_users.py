import psycopg2
import unittest

from secret_stuff.database import login_dict
from src.database.admin import get_tables
from src.database.users import create_table, create_index_name


class TestUsers(unittest.TestCase):
    def test_it_can_create_users(self):
        try:
            connection = psycopg2.connect(**login_dict)

            cursor = connection.cursor()

            create_table(cursor)
            create_index_name(cursor)

            self.assertTrue('users' in get_tables(cursor))

        except (Exception, psycopg2.Error) as error:
            print('PostgreSQL Login Error: ', error)


if __name__ == '__main__':
    unittest.main()
