class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if beginWord == endWord:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    next_word = word[:i]+ch+word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, steps+1))
                        visited.add(next_word)

        return 0