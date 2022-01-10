class Sentence:
    def __init__(self, string):
        self.string = string

    def get_sentence(self):
        return self.string

    def get_words(self):
        return self.string.split()

    def get_length(self):
        return len(self.string)

    def get_num_words(self):
        return len(self.get_words())
