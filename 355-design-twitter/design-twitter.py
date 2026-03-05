class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                latest_tweet_index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][latest_tweet_index]
                maxHeap.append([count, tweetId, followeeId, latest_tweet_index-1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res)<10:
            count, tweetId, followeeId, latest_tweet_index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if latest_tweet_index >= 0:
                count, tweetId = self.tweetMap[followeeId][latest_tweet_index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, latest_tweet_index-1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)