import email_guesser.guesser as guesser
import email_guesser.name_guesser as name_guesser
import gender_guesser.detector as gender


def name_guesser_factory():
    return name_guesser.NameGuesser("marek.piotrowicz@gmail.com")
