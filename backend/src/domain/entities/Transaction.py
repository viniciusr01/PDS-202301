from src.utils.ValidDateTime import ValidDateTime
from datetime import date


class Transaction:


    def __init__(self, 
                 description: str, 
                 value: float, 
                 reference_date: str, 
                 id_category: int
                 ) -> None:
        
        if(not ValidDateTime(reference_date)):
            raise Exception("It isn't a valid datetime")
        
        date_arr = reference_date.split('-')

        self.reference_date = date(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
        self.description = description
        self.value = value
        self.id_category = id_category

