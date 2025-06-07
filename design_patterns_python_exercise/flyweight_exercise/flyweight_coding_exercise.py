class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self.tokens = [WordToken() for _ in self.words]

    def __getitem__(self, index):
        return self.tokens[index]

    def __str__(self):
        words_for_print = []
        for i, token in enumerate(self.tokens):
            word = self.words[i]
            if token.capitalize:
                words_for_print.append(word.upper())
            else:
                words_for_print.append(word)

        return " ".join(words_for_print)


class WordToken:
    def __init__(self):
        self.capitalize = False


sentence = Sentence("hello world")
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
