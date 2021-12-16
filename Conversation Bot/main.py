import logging
from bot.question_class import Question

logger = logging.basicConfig(format='%(asctime)s:-:%(levelname)s:-:%(message)s', level=logging.INFO)

def main():
    """Run main. Obviously."""
    question = Question()
    question.pick_random_question()

if __name__ == '__main__':
    main()
