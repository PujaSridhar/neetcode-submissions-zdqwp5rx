class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)  # userId -> deque of (timestamp, tweetId)
        self.followees = defaultdict(set)  # userId -> set of followeeIds
        self.feed_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        # Push user's own tweets to the heap
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > self.feed_size:
                    heapq.heappop(min_heap)
        
        # Push followees' tweets to the heap
        if userId in self.followees:
            for followeeId in self.followees[userId]:
                if followeeId in self.tweets:
                    for tweet in self.tweets[followeeId]:
                        heapq.heappush(min_heap, tweet)
                        if len(min_heap) > self.feed_size:
                            heapq.heappop(min_heap)
        
        # Extract tweets from heap and return them in reverse order
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)