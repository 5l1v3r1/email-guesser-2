import re
import email_guesser.guesser as guesser
import gender_guesser.detector as gender

class NameGuesser(guesser.Guesser):
    def __init__(self, email):
        super(self.__class__, self).__init__(email)
        self.gender_detector = gender.Detector(case_sensitive=False)

    def guess(self):
        result_from_common_expresion =  self.common_expesions(self.email_content)
        if result_from_common_expresion:
            return result_from_common_expresion['gender']
        else:
            most_popular_name = self.get_most_popular_substring_name(self.email_content)
            if most_popular_name != 'name':
                return self.gender_detector.get_gender(most_popular_name)
        return None


    def common_expesions(self, email_content):
        #michelle(.or_)lagrande@example.com
        #michelle(.or_)lagr1ande123@example.com
        if re.fullmatch('[a-zA-Z]+[\._][a-zA-Z1-9]+', email_content):
            name = email_content.split(".")[0]
            if self.gender_detector.get_gender(name) != "unknown" :
                return {'name' : name.lower(), 'gender' : self.gender_detector.get_gender(name)}
        #lagrande(.or_)michelle@example.com
        #lag1rande132(.or_)michelle@example.com
        if re.fullmatch('[a-zA-Z1-9]+[\._][a-zA-Z]+', email_content):
            name = email_content.split(".")[1]
            if self.gender_detector.get_gender(name) != "unknown":
                return {'name' : name.lower(),'gender' : self.gender_detector.get_gender(name)}
        return None

    def get_most_popular_substring_name(self, email_content):
        most_popular_name_and_its_popular = ('name', 0)
        set_of_substrings = guesser.Guesser.generate_set_of_substrings_starting_from_begin(email_content)
        for potentially_name in set_of_substrings:
            potentially_name = potentially_name.lower()
            result = self.gender_detector.get_gender(potentially_name)
            if result != "unknown" and result != "andy":
                popularity_of_name = NameGuesser.get_max_popularity(self.gender_detector.names[potentially_name])
                if popularity_of_name > most_popular_name_and_its_popular[1] and popularity_of_name > 5:
                    most_popular_name_and_its_popular = (potentially_name, popularity_of_name)
        return most_popular_name_and_its_popular[0]

    @staticmethod
    def get_max_popularity(dictionary):
        max_popularity = -1
        for key in dictionary:
            popularity_list = dictionary[key].replace(" ", "")
            for sing in popularity_list:
                numer_from_sign = int(sing, 16)  # basez is 16
                if numer_from_sign > max_popularity:
                    max_popularity = numer_from_sign
        return max_popularity
