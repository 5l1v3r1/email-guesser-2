'''import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))'''

import unittest

import email_guesser.guesser as guesser
import email_guesser.name_guesser as name_guesser
from test import factories


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


class TestNameGuesser(unittest.TestCase):
    def test_max_popularity(self):
        name_dic = {'male' : "   3   4    2      ", "female" : "               4           3           1"}
        result = name_guesser.NameGuesser.get_max_popularity(name_dic)
        self.assertEqual(4, result)

    def test_emails_check_by_regex(self):
        mail_content1 = "agnieszka.lagrande"
        mail_content2 = "lagrande.Mark"
        mail_content3 = "Taylor.lagrande1992"
        mail_content4 = "laaagrande1992.tom"
        self.assertEqual({'name' : 'agnieszka', 'gender' : 'female'}, factories.name_guesser_factory().common_expesions(mail_content1))
        self.assertEqual({'name' : 'mark', 'gender' : 'male'}, factories.name_guesser_factory().common_expesions(mail_content2))
        self.assertEqual({'name' : 'taylor', 'gender' : 'mostly_male'}, factories.name_guesser_factory().common_expesions(mail_content3))
        self.assertEqual({'name' : 'tom', 'gender' : 'male'}, factories.name_guesser_factory().common_expesions(mail_content4))

    def test_emails_by_most_popular_substring(self):
        mail_content1 = "tatjanakowalska"
        mail_content2 = "marekDusza"
        self.assertEqual("tatjana", factories.name_guesser_factory().get_most_popular_substring_name(mail_content1))
        self.assertEqual("marek", factories.name_guesser_factory().get_most_popular_substring_name(mail_content2))

    def test_integrate(self):
        name_guesser_obj1 = name_guesser.NameGuesser("michal.mokrogulski@gmail.com")
        name_guesser_obj2 = name_guesser.NameGuesser("arturrasicki@gmail.com")
        name_guesser_obj3 = name_guesser.NameGuesser("agatamachowiec@gmail.com")
        name_guesser_obj4 = name_guesser.NameGuesser("asfdsadfiec@gmail.com")
        name_guesser_obj5 = name_guesser.NameGuesser("maciejopieka@gmail.com")
        self.assertEqual("male", name_guesser_obj1.guess())
        self.assertEqual("male", name_guesser_obj2.guess())
        self.assertEqual("female", name_guesser_obj3.guess())
        self.assertEqual(None, name_guesser_obj4.guess())
        self.assertEqual("male", name_guesser_obj5.guess())


if __name__ == '__main__':
    unittest.main()
