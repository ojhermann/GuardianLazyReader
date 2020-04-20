query: str = """
    DROP TABLE IF EXISTS {} RESTRICT;
    """


def drop_table(table: str) -> str:
    return f'DROP TABLE IF EXISTS {table} RESTRICT;'


if __name__ == '__main__':
    print(drop_table('some_table'))
