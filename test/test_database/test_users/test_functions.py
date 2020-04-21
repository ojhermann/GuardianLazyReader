import unittest

import psycopg2

from secret_stuff.database import login_dict
from secret_stuff.guardian_api import api_key_otto
from src.database.users.functions import get_user_by_name, get_user_by_id, update_user_api_key, create_user, \
    delete_user, resurrect_user
from src.database.users.user import User
from src.database.utils.functions import get_tables


class TestFunctions(unittest.TestCase):
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()

    def test_users_exists(self):
        self.assertTrue('users' in get_tables(TestFunctions.cursor))

    def test_it_can_create_user(self):
        name: str = 'test_it_can_create_user_name'
        api_key: str = 'test_it_can_create_user_api_key'
        deleted: bool = False

        user_created: User = create_user(name=name,
                                         api_key=api_key,
                                         psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(name,
                         user_created.get_name())
        self.assertEqual(api_key,
                         user_created.get_api_key())
        self.assertEqual(deleted,
                         user_created.is_deleted())

        self.assertEqual(None,
                         create_user(name=name,
                                     api_key=api_key,
                                     psycopg2_cursor=TestFunctions.cursor))

    def test_it_can_get_user_by_name(self):
        otto: User = get_user_by_name(name='otto',
                                      psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(1,
                         otto.get_id())
        self.assertEqual('otto',
                         otto.get_name())
        self.assertEqual(api_key_otto,
                         otto.get_api_key())
        self.assertEqual(False,
                         otto.is_deleted())

        bogus_user: User = get_user_by_name(name='test_it_can_get_user_by_name',
                                            psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(None,
                         bogus_user)

    def test_it_can_get_user_by_id(self):
        otto: User = get_user_by_id(id=1,
                                    psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(1,
                         otto.get_id())
        self.assertEqual('otto',
                         otto.get_name())
        self.assertEqual(api_key_otto,
                         otto.get_api_key())
        self.assertEqual(False,
                         otto.is_deleted())

        bogus_user: User = get_user_by_id(id=-1,
                                          psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(None,
                         bogus_user)

    def test_it_can_update_user_api_key(self):
        api_key_updated: str = 'test_it_can_update_user'

        otto_updated: User = update_user_api_key(name='otto',
                                                 api_key=api_key_updated,
                                                 psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(api_key_updated,
                         otto_updated.get_api_key())

        # changes not committed; resetting for other tests in the class
        otto_updated: User = update_user_api_key(name='otto',
                                                 api_key=api_key_otto,
                                                 psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(api_key_otto,
                         otto_updated.get_api_key())

    def test_it_can_delete_and_resurrect_user(self):
        otto_deleted: User = delete_user(name='otto',
                                         psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(otto_deleted.is_deleted())

        otto_resurrected: User = resurrect_user(name='otto',
                                                psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(not otto_resurrected.is_deleted())


if __name__ == '__main__':
    unittest.main()
