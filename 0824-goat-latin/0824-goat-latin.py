class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = set(('a','e','i','o','u'))
        answer = ''
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            word = sentence[i]
            if word[0].lower() in vowel:
                answer += word
            else:
                answer += word[1:] + word[0]
            answer += 'ma' + ((i+1) * 'a') + ' '
        return answer[:-1]