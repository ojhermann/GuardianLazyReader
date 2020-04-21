import unittest
from logging import Logger
from os import remove

from src.log_settings.log_settings import get_logger


class TestLogSettings(unittest.TestCase):
    def test_it_can_log(self):
        file_name: str = 'test_it_can_log.log'

        logger: Logger = get_logger(log_file_name=file_name)

        logger.info(file_name)

        with open(file_name) as source:
            self.assertEqual(file_name,
                             source.read().split(':')[-1].strip())

        remove(file_name)


if __name__ == '__main__':
    unittest.main()
