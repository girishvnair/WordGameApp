import json

class GameLogic:
    def __init__(self, words_file="frontend/assets/words.json"):
        with open(words_file, "r") as f:
            self.words_data = json.load(f)  # Load words for each level

    def check_answers(self, level, user_answers):
        """
        Compares user_answers with correct answers.
        user_answers: {"adjective": ["big"], "noun": ["hen"]}
        """
        correct_words = self.words_data[str(level)]
        return user_answers == correct_words
