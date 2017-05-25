class Guesser:
    def __init__(self):
        pass


    def set_email(self, email):
        self.email = email
        email_params = Guesser.email_parser(email)
        self.email_content = email_params['content']
        self.email_sufix = email_params['sufix']

    def guess(self):
        try:
            getattr(self, "email")
        except AttributeError:
            raise EmailNotSetError

    @staticmethod
    def email_parser(email):
        email_params = {}
        email_params['content'] = email.split("@")[0]
        email_params['sufix'] = email.split("@")[1].split(".")[-1]
        return email_params
    
    @staticmethod
    def generate_set_of_substrings(string):
        substring_len = 1
        set_of_substrings = set()
        while True:
            for i in range(len(string) - substring_len + 1):
                set_of_substrings.add(string[i:i + substring_len])
            if substring_len == len(string):
                break
            substring_len += 1
        return set_of_substrings

    @staticmethod
    def generate_set_of_substrings_starting_from_begin(string):
        set_of_substrings = set()
        for i in range(1,len(string)+1):
            set_of_substrings.add(string[0:i])
        return set_of_substrings

class EmailNotSetError(Exception):
    pass