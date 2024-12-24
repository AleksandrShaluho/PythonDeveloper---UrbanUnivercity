class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                file_string = file.read().lower()
                cleared_string = ''.join(
                    char for char in file_string if char not in [',', '.', '=', '!', '?', ';', ':', ' - '])
                all_words[name] = (cleared_string.split())
        return all_words

    def find(self, word):
        word_point = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                word_point[name] = words.index(word.lower()) + 1
        return word_point

    def count(self, word):
        word_count = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            for element in words:
                if word.lower() == element:
                    if name in word_count:
                        word_count[name] += 1
                    else:
                        word_count[name] = 1
        return word_count
