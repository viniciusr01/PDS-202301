class ValidObject:
    def make(self, obj: dict, keys: list) -> bool:
        for key in keys:
            if key not in obj:
                return False
            
        return True
