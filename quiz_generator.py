from random import randint, choice
from verb_handler import VerbHandler


class QuizGenerator:
    
    def __init__(self, filtering, quiz_length = 3):
        """ Requires dictionary with desired verb tenses as keys connected to 
        a list of desired subjects for each tense. 
        """
        self.filtering = filtering
        self.quiz_length = quiz_length
        self.initialized_verbs = {}
        
        self.verb_handler = VerbHandler()
        self.initialize_conjugations()

    def main(self):
        questions = self.generate_questions()
        correct = 0
        for question in questions:
            user_answer = input("{}: ".format(question))
            if user_answer == questions[question]:
                correct += 1

    def generate_questions(self):
        questions = {}
        tense_options = [tense for tense in self.filtering]
        
        for q in range(self.quiz_length):
            found = False
            while not found:
                if len(tense_options) > 1:
                    rand_tense = tense_options[randint(0, len(tense_options)-1)]
                else:
                    rand_tense = tense_options[0]
                    
                verb_options = self.initialized_verbs[rand_tense]
                rand_verb = verb_options[randint(0, len(verb_options)-1)]

                unfiltered_subjects = self.verb_handler.verbs[rand_verb].conjugations[rand_tense]
                filtered_subjects = [sub for sub in unfiltered_subjects if
                                     sub in self.filtering[rand_tense]]
                rand_subject = choice(filtered_subjects)
                
                if rand_tense == "past_masc":
                    rand_tense = "past masculine"
                elif rand_tense == "past_fem":
                    rand_tense = "past feminine"
                    
                question_info = "{} {} {}".format(rand_verb, rand_tense,
                                                  rand_subject)
                
                if question_info not in questions:
                    questions[question_info] = unfiltered_subjects[rand_subject]
                    found = True
            
        return questions
              
    def initialize_conjugations(self):
        functions = {"present": self.verb_handler.filter_empty_present,
                     "past_masc": self.verb_handler.filter_empty_pastm,
                     "past_fem": self.verb_handler.filter_empty_pastf,
                     "future": self.verb_handler.filter_empty_future}
        for tense in self.filtering:
            if tense in functions:
                self.initialized_verbs[tense] = functions.get(tense, lambda: 'Invalid')()
