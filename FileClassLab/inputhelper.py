class InputHelper:
    @staticmethod
    def return_intresponse(field):
        result = input(f'Enter {field}: ')
        if InputHelper.dtype(result) != 'i':
            print(f"Invalid {field}!")
            return None
        return result

    @staticmethod
    def return_strresponse(field):
        result = input(f'Enter {field}: ')
        if InputHelper.dtype(result) != 's':
            print(f"Invalid {field}!")
            return None
        return result

    @staticmethod
    def dtype(x):
        if x is not None and x != '':
            if x.isdigit():
                return 'i'
            if x.replace(' ', '').isalnum():
                return 's'
        return 'u'
