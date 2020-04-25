import unittest

import psycopg2

from secret_stuff.lazy_reader_db import login_dict
from src.lazy_reader_db.utils.functions import get_tables


class TestFunctions(unittest.TestCase):
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()

    def test_guardian_content_exists(self):
        self.assertTrue('guardian_content' in get_tables(TestFunctions.cursor))


if __name__ == '__main__':
    unittest.main()
