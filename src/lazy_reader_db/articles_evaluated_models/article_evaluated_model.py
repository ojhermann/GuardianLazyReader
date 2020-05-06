from datetime import datetime


class ArticleEvaluatedModel:
    def __init__(self,
                 user_id: int,
                 guardian_id: str,
                 model_id: str,
                 evaluated_on: datetime):
        self.__user_id: int = user_id
        self.__guardian_id: str = guardian_id
        self.__model_id: str = model_id
        self.__evaluated_on: datetime = evaluated_on

    def get_user_id(self) -> int:
        return self.__user_id

    def get_guardian_id(self) -> str:
        return self.__guardian_id

    def get_model_id(self) -> str:
        return self.__model_id

    def get_evaluated_on(self) -> datetime:
        return self.__evaluated_on
