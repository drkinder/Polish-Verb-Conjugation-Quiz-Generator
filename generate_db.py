import sqlite3 as sq
import urllib.request as req
import re


class GenerateDB:
    """ Class for updating verb_conjugations.db database. Retrieves
        conjugation data from https://cooljugator.com/pl/ . Current tenses
        supported - present, past masculine, past feminine.
    """

    def __init__(self, verbs, filename):
        """
        :param verbs: list of verbs that you want to scrap conjugations for.
        :param filename: the generated database's filename.
        """
        
        self.verbs = verbs
        
        self.database_filename = filename
        self.root_url = "https://cooljugator.com/pl/"
        
        self.connect = sq.connect(self.database_filename)
        self.cursor = self.connect.cursor()
        
        self.failed_verbs = {"present": [], "past_masc": [], "past_fem": []}
        
        self.main()
        
    def main(self):
        self.cursor.execute("""CREATE TABLE conjugations (
                            verb text,
                            present text,
                            past_masc text,
                            past_fem text
                            )""")
        
        self.connect.commit()
                    
        for verb in self.verbs:
            try:
                verb_conjugations = {"verb": verb}
                verb_url = self.root_url+self.get_url(verb)
         
                content = self.get_verb_html(verb_url)
                verb_conjugations["present"] = self.get_present_tense(verb, 
                                                                      content)
                
                verb_conjugations["past_masc"] = self.get_pastmasc_tense(verb,
                                                                         content)
                verb_conjugations["past_fem"] = self.get_pastfem_tense(verb,
                                                                       content)
                #verb_conjugations["future"] = self.get_future_tense(content)

                self.write_verb(verb_conjugations)

            except Exception as e:
                print(e)
        
        self.connect.close()
    
    def get_present_tense(self, verb, content):
        
        keys = ["1s", "2s", "3s", "1p", "2p", "3p"]
        conjugation_indicator = "data-default=\""
        conjugations = {}
        
        start_key = ">Present tense</span>"
        end_key = ">Imperfective future tense</span>"
        
        try:
            search_result = re.search(start_key + "(.*)" + end_key, content)
            present_tense_raw = search_result.group(1)
            present_tense_list = present_tense_raw.split(" ")
            
            for string in present_tense_list:
                if conjugation_indicator in string:
                    for key in keys:
                        if key not in conjugations:
                            conjugations[key] = string[14:-1]
                            break
        except AttributeError:
            self.failed_verbs["present"].append(verb)
            return {}
                    
        return conjugations
    
    def get_pastmasc_tense(self, verb, content):
        
        keys = ["1s", "2s", "3s", "1p", "2p", "3p"]
        conjugation_indicator = "data-default=\""
        conjugations = {}
        
        start_key = ">Past masculine tense</span>"
        end_key = ">Future masculine tense</span>"
        
        try:
            search_result = re.search(start_key + "(.*)" + end_key, content)
            present_tense_raw = search_result.group(1)
            present_tense_list = present_tense_raw.split(" ")
            
            for string in present_tense_list:
                if conjugation_indicator in string:
                    for key in keys:
                        if key not in conjugations:
                            conjugations[key] = string[14:-1]
                            break
        except AttributeError:
            self.failed_verbs["past_masc"].append(verb)
            return {}
                    
        return conjugations
    
    def get_pastfem_tense(self, verb, content):
        
        keys = ["1s", "2s", "3s", "1p", "2p", "3p"]
        conjugation_indicator = "data-default=\""
        conjugations = {}
        
        start_key = ">Past feminine tense</span>"
        end_key = ">Future feminine tense</span>"
        
        try:
            search_result = re.search(start_key + "(.*)" + end_key, content)
            present_tense_raw = search_result.group(1)
            present_tense_list = present_tense_raw.split(" ")
            
            for string in present_tense_list:
                if conjugation_indicator in string:
                    for key in keys:
                        if key not in conjugations:
                            conjugations[key] = string[14:-1]
                            break
        except AttributeError:
            self.failed_verbs["past_fem"].append(verb)
            return {}
                    
        return conjugations
    
    def write_verb(self, conjugation_dict):

        db_dictionary = self.reformat_dict4db(conjugation_dict)
        
        with self.connect:
            self.cursor.execute("INSERT INTO conjugations VALUES " +
                                "(:verb, :present, :past_masc, :past_fem)",
                                {"verb": db_dictionary["verb"],
                                 "present": db_dictionary["present"],
                                 "past_masc": db_dictionary["past_masc"],
                                 "past_fem": db_dictionary["past_fem"]})
            
    def db_retrieve_raw_verb(self, verb):
        with self.connect:
            self.cursor.execute("SELECT * FROM conjugations WHERE verb=:verb",
                                {"verb": verb})
        return self.cursor.fetchall()
    
    def reformat_dict4db(self, dictionary):
        re_dictionary = {}
        for key in dictionary:
            if isinstance(dictionary[key], dict):
                new_value = self.convert_dict2string(dictionary[key])[:-1] #extra whitespace at end
                re_dictionary[key] = new_value
            elif dictionary[key] == None:
                re_dictionary[key] = ''
            else:
                re_dictionary[key] = dictionary[key]
        return re_dictionary

    def get_url(self, verb):
        """ Returns the final part of the cooljugator.com url associated with
        this specific verb. Non-ascii characters are handled strangly in URL.
        """
        url_verb = ""
        for char in verb:
            if self.is_ascii(char):
                url_verb += char
            else:
                url_verb += self.convert_byte2url_string(char.encode("utf-8"))

        return url_verb

    @staticmethod
    def check_verb_initialized(conjugation_dict):
        for key in conjugation_dict:
            if isinstance(list, conjugation_dict[key]):
                if len(conjugation_dict > 0):
                    return True
        return False

    @staticmethod
    def convert_dict2string(dictionary):
        string = ""
        for key in dictionary:
            string += dictionary[key] + " "
        return string

    @staticmethod
    def get_verb_page(verb_url):
        content = req.urlopen(verb_url)
        for line in content:
            content = line.decode("utf-8")
        return content

    @staticmethod
    def is_ascii(char):
        """ Returns boolean representing if character is ascii."""
        
        try:
            c = char.encode('ascii')
            return True
        except UnicodeEncodeError:
            return False

    @staticmethod
    def convert_byte2url_string(byte):
        """ Converts non ascii characters into the format used by 
        cooljugator.com url adresses.
        """
        
        original_string = repr(byte)[2:-1].upper()
        processed_string = ''
        for char in original_string:
            if char == '\\':
                processed_string += '%'
            elif char == 'X':
                pass
            else:
                processed_string += char
        return processed_string


if __name__ == "__main__":
   
    verbs = ['jechać', 'mówić', 'używać', 'potrzebować', 'uczyć', 'przeliterować', 
             'chcieć', 'iść', 'śmiać', 'kochać', 'próbować', 'pamiętać', 'umieć', 
             'gotować', 'mieć', 'dawać', 'słyszeć', 'wygrać', 'pomagać', 
             'wychodzić', 'tęsknić', 'zapomnieć', 'lubić', 'widzieć',
             'znać', 'płacić', 'ruszać', 'pracować', 'oglądać', 'spotykać',
             'nosić', 'kończyć', 'zamykać', 'otwierać', 'wymawiać', 'czytać', 
             'pisać', 'brać', 'czuć', 'rozumieć', 'przegrać', 'kłamać', 
             'przychodzić', 'żyć', 'słuchać', 'zatrzymać', 'pokazywać', 
             'zadzwonić', 'znaleźć', 'zgubić', 'szukać', 'zaczynać',
             'wiedzieć']
   
    gen = GenerateDB(verbs, "verb_conjugations.db")
