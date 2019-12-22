import sqlite3 as sq
from verb import Verb


class VerbHandler:
    
    def __init__(self):
        
        self.database_filename = "verb_conjugations.db"
        
        self.connect = sq.connect(self.database_filename)
        self.cursor = self.connect.cursor()
        
        self.verbs = {}
        self.main()
        
    def main(self):
        data = self.cursor.execute("SELECT * FROM conjugations")
        all_verb_data = data.fetchall()
        for verb_data in all_verb_data:
            infinitive = verb_data[0]
            verb_dict = self.convert_list2dict(verb_data)
            self.verbs[infinitive] = Verb(verb_dict)
        
    def convert_list2dict(self, db_list):
        keys = ["verb", "present", "past_masc", "past_fem" "future"]
        new_dict = {}
        for idx, entry in enumerate(db_list):
            new_dict[keys[idx]] = entry
        return new_dict
    
    def filter_empty_present(self):
        """ Returns a list with all verb infinitives that do not have
        blank conjugation data for the present tense"""
        new_verbs = []
        for verb in self.verbs:
            infinitive = self.verbs[verb].infinitive
            if len(self.verbs[verb].conjugations["present"]) > 0:
                new_verbs.append(infinitive)
        return new_verbs
    
    def filter_empty_pastf(self):
        new_verbs = []
        for verb in self.verbs:
            infinitive = self.verbs[verb].infinitive
            if len(self.verbs[verb].conjugations["past_fem"]) > 0:
                new_verbs.append(infinitive)
        return new_verbs
    
    def filter_empty_pastm(self):
        new_verbs = []
        for verb in self.verbs:
            infinitive = self.verbs[verb].infinitive
            if len(self.verbs[verb].conjugations["past_masc"]) > 0:
                new_verbs.append(infinitive)
        return new_verbs
    
    def filter_empty_future(self):
        pass
