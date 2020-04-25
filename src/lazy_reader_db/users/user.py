class User:
    def __init__(self,
                 id: int,
                 name: str,
                 api_key: str,
                 deleted: bool):
        self.__id: int = id
        self.__name: str = name
        self.__api_key: str = api_key
        self.__deleted: bool = deleted

    def __repr__(self):
        return f'id: {self.get_id()}, ' \
               f'name: {self.get_name()}, ' \
               f'api_key: {self.get_api_key()}, ' \
               f'deleted: {self.is_deleted()}'

    def __str__(self):
        return self.__repr__()

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_api_key(self) -> str:
        return self.__api_key

    def is_deleted(self) -> bool:
        return self.__deleted
