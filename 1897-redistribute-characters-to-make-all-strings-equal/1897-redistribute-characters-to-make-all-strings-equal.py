class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_cnt = defaultdict(int)
        for word in words:
            for c in word:
                char_cnt[c] += 1
        
        for c in char_cnt:
            if char_cnt[c] % len(words):
                return False
        return True