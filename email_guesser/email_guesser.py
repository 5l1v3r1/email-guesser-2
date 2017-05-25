
class EmailGuesser:
    def __init__(self, guessers_names=None):
        self.guessers = self.generate_guessers(guessers_names) if guessers_names else self.defaults_guessers()

    def set_email(self, email):
        self.email = email

    def guess(self):
        """guess method try to guess gender by list of modules
        :return: "male", "female", None
        """
        # TODO
        pass

    def defaults_guessers(self):
        #TODO
        return ["", "a"]

    def generate_guessers(self, guessers_names):
        # TODO
        return 0