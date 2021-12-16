import random
import logging
import configparser

class Question:
    
    def __init__(self):
        self.parser = configparser.ConfigParser(interpolation=None)
        self.parser.read('topics.ini')
        self.sections = self.parser.sections()
        
        logging.basicConfig(format='%(asctime)s:-:%(levelname)s:-:%(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    
    def pick_topic_question(self, parser, section):
        """Pick a random question from a set topic."""
        number = str(random.randint(1,20))
        
        # logging.info(f"{section}, :{number}")
        
        print(parser[section][number])


    def pick_random_question(self):
        """Pick a random question."""
        logger = self.logger
        
        section = random.choice(self.sections)
        number = str(random.randint(1,20))
        
        logger.info(f"{section}, :{number}")
        
        return self.parser[section][number]
