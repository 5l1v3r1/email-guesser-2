import unittest

import email_guesser.guesser as guesser


class TestGuesser(unittest.TestCase):
    def test_mail_parser(self):
        email_params = guesser.Guesser.email_parser("jakis_mail@gmail.pl")
        email_content = email_params['content']
        email_sufix = email_params['sufix']
        self.assertEqual("jakis_mail", email_content)
        self.assertEqual("pl", email_sufix)

    def test_generate_set_of_substrings_starting_from_begin(self):
        s = guesser.Guesser.generate_set_of_substrings_starting_from_begin("abcd")
        self.assertEqual({'a', 'ab', 'abc', 'abcd'}, s)


if __name__ == '__main__':
    unittest.main()
