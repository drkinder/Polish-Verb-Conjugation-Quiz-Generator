import sqlite3 as sq


class Verb:
    
    def __init__(self, conjugation_dict):
        self.infinitive = conjugation_dict["verb"]
        self.conjugations = self.initialize_conjugations(conjugation_dict)
        
    def initialize_conjugations(self, conjugation_dict):
        """
        subjects = {1 : [],
                    6 : ["1s", "2s", "3s", "1p", "2p", "3p"],
                    7 : ["1s", "2s", "3s-m", "3s-f", "1p", "2p", "3p"]}
        """
        subjects = {1: [],
                    6: ["ja", "ty", "on/ona", "my", "wy", "oni/one"],
                    7: ["1s", "2s", "3s-m", "3s-f", "1p", "2p", "3p"]}
        formatted_dict = {}
        for key in conjugation_dict:
            if key != "verb":
                formatted_dict[key] = {}
                conj_list = conjugation_dict[key].split(" ")
                try:
                    for idx, subject in enumerate(subjects[len(conj_list)]):
                        formatted_dict[key][subject] = conj_list[idx]
                except KeyError:
                    exception_msg = "{} tense in {} has {} subjects"
                    raise Exception(exception_msg.format(key, self.infinitive, 
                                                         str(len(conj_list))))
        return formatted_dict

