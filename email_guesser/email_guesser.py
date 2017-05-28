from email_guesser import name_guesser

class EmailGuesser:
    def __init__(self):
        self.defaults_guessers()

    def set_email(self, email):
        self.email = email
        for guesser in self.guessers:
            guesser.set_email(email)

    def guess(self):
        for guesser in self.guessers:
            result = guesser.guess()
            if result is not None:
                return result
        return None

    def defaults_guessers(self):
        self.guessers.append(name_guesser.NameGuesser())
