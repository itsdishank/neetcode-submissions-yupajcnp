class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        # print(self.follows)
        # print(self.tweets)
        users = self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            i = 0
            while i <len(self.tweets[followee]):
                heapq.heappush(feed, self.tweets[followee][i])
                i+=1
        # print(feed)
        while len(feed) > 10:
            heapq.heappop(feed)

        res = []
        
        while feed:
            res.insert(0, heapq.heappop(feed)[1])
        
        # print(feed)
        # print()

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)