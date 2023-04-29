import re

class ValidDateTime:
    def __init__(self, date: str) -> bool:
        return re.fullmatch("/^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$/", date)