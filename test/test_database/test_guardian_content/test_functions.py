import unittest
from typing import Tuple

import psycopg2
from guardian_api.main.guardian_api import GuardianApi
from guardian_api.main.guardian_content import GuardianContent

from secret_stuff.guardian_api import api_key_otto
from secret_stuff.lazy_reader_db import login_dict
from src.lazy_reader_db.guardian_content.functions import create_guardian_content, delete_guardian_content, \
    get_guardian_content
from src.lazy_reader_db.utils.functions import get_tables


class TestFunctions(unittest.TestCase):
    connection = psycopg2.connect(**login_dict)
    cursor = connection.cursor()

    ga: GuardianApi = GuardianApi(guardian_api_key=api_key_otto)
    gcs: Tuple[GuardianContent, ...] = ga.generate_multiple_items(guardian_response=ga.get_response()).get_content()
    gc: GuardianContent = gcs[0]

    def test_guardian_content_exists(self):
        self.assertTrue('guardian_content' in get_tables(TestFunctions.cursor))

    def test_it_can_create_and_delete_guardian_content(self):
        # todo https://github.com/ojhermann/GuardianApi/issues/18

        gc_from_db: GuardianContent = create_guardian_content(gc=TestFunctions.gc,
                                                              psycopg2_cursor=TestFunctions.cursor)
        self.assertEqual(TestFunctions.gc.get_api_url(),
                         gc_from_db.get_api_url())

        self.assertEqual(TestFunctions.gc.get_body_text(),
                         gc_from_db.get_body_text())

        self.assertEqual(TestFunctions.gc.get_guardian_id(),
                         gc_from_db.get_guardian_id())

        self.assertEqual(TestFunctions.gc.get_is_hosted(),
                         gc_from_db.get_is_hosted())

        self.assertEqual(TestFunctions.gc.get_pillar_id(),
                         gc_from_db.get_pillar_id())

        self.assertEqual(TestFunctions.gc.get_pillar_name(),
                         gc_from_db.get_pillar_name())

        self.assertEqual(TestFunctions.gc.get_section_id(),
                         gc_from_db.get_section_id())

        self.assertEqual(TestFunctions.gc.get_section_name(),
                         gc_from_db.get_section_name())

        self.assertEqual(TestFunctions.gc.get_guardian_type(),
                         gc_from_db.get_guardian_type())

        self.assertEqual(TestFunctions.gc.get_web_publication_date(),
                         gc_from_db.get_web_publication_date())

        self.assertEqual(TestFunctions.gc.get_web_title(),
                         gc_from_db.get_web_title())

        self.assertEqual(TestFunctions.gc.get_web_url(),
                         gc_from_db.get_web_url())

        # delete
        gc_from_db = delete_guardian_content(guardian_id=TestFunctions.gc.get_guardian_id(),
                                             psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(TestFunctions.gc.get_guardian_id(),
                        gc_from_db.get_guardian_id())

        # confirm deletion
        gc_from_db = get_guardian_content(guardian_id=TestFunctions.gc.get_guardian_id(),
                                          psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(gc_from_db is None)

    def test_it_can_fail_to_create_and_delete_gracefully(self):
        gc_from_db: GuardianContent = create_guardian_content(gc=TestFunctions.gc,
                                                              psycopg2_cursor=TestFunctions.cursor)
        gc_from_db = create_guardian_content(gc=TestFunctions.gc,
                                             psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(gc_from_db is None)

        gc_from_db = delete_guardian_content(guardian_id=TestFunctions.gc.get_guardian_id(),
                                             psycopg2_cursor=TestFunctions.cursor)
        gc_from_db = delete_guardian_content(guardian_id=TestFunctions.gc.get_guardian_id(),
                                             psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(gc_from_db is None)

        # confirm deletion
        gc_from_db = get_guardian_content(guardian_id=TestFunctions.gc.get_guardian_id(),
                                          psycopg2_cursor=TestFunctions.cursor)
        self.assertTrue(gc_from_db is None)


if __name__ == '__main__':
    unittest.main()
