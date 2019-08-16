import sys
class WordAnagram:

    def __init__(self):
        self.wordList = []
        self.input = []
        if len(sys.argv) > 1:
            for char in sys.argv[1]:
                self.input.append(char)

    def solution(self, chars):
        if not self.input:
            self.input = chars

        res = set()
        for word in self.wordList:
            letters = self.letterCounts(word)
            valid = 1
            for l in letters:
                if l not in self.input:
                    valid = 0
                    break
                else:
                    if self.input.count(l) != letters[l]:
                        valid = 0
                        break

            if valid == 1:
                res.add(word)

        return res

    def letterCounts(self, word):
        dict = {}
        for l in word:
            dict[l] = dict.get(l, 0) + 1
        return dict

    def readWords(self):

        filepath = '/usr/share/dict/words' or './words'
        with open(filepath) as file:
            lines = file.readlines()
            if not lines:
                return self.wordList
            for word in lines:
                self.wordList.append(word.strip('\n').lower())

if __name__ == '__main__':
    wordAnagram = WordAnagram()
    wordAnagram.readWords()
    res = wordAnagram.solution('kwamme')
    print(res)