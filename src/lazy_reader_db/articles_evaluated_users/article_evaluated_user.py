from datetime import datetime


class ArticleEvaluatedUser:
    def __init__(self,
                 user_id: int,
                 guardian_id: str,
                 evaluated_on: datetime,
                 is_liked: bool):
        self.__user_id: int = user_id
        self.__guardian_id: str = guardian_id
        self.__evaluated_on: datetime = evaluated_on
        self.__is_liked: bool = is_liked

    def get_user_id(self) -> int:
        return self.__user_id

    def get_guardian_id(self) -> str:
        return self.__guardian_id

    def get_evaluated_on(self) -> datetime:
        return self.__evaluated_on

    def is_liked(self) -> bool:
        return self.__is_liked
