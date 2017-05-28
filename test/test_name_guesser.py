import unittest

import email_guesser.name_guesser as name_guesser
import factories as factories

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
        name_guesser_obj1 = factories.name_guesser_factory("michal.mokrogulski@gmail.com")
        name_guesser_obj2 = factories.name_guesser_factory("arturrasicki@gmail.com")
        name_guesser_obj3 = factories.name_guesser_factory("agatamachowiec@gmail.com")
        name_guesser_obj4 = factories.name_guesser_factory("asfdsadfiec@gmail.com")
        name_guesser_obj5 = factories.name_guesser_factory("maciejopieka@gmail.com")
        self.assertEqual("male", name_guesser_obj1.guess())
        self.assertEqual("male", name_guesser_obj2.guess())
        self.assertEqual("female", name_guesser_obj3.guess())
        self.assertEqual(None, name_guesser_obj4.guess())
        self.assertEqual("male", name_guesser_obj5.guess())


if __name__ == '__main__':
    unittest.main()