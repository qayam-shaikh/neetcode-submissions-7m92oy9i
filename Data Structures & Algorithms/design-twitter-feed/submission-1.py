class Twitter:

    def __init__(self):
        self.time=0
        self.tweetmap=defaultdict(list)
        self.followmap=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweetmap[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxheap=[]
        self.followmap[userId].add(userId)
        for followee in self.followmap[userId]:
            if followee in self.tweetmap:
                index=len(self.tweetmap[followee])-1
                time,tweetId=self.tweetmap[followee][index]
                heapq.heappush(maxheap,(-time,tweetId,followee,index-1))
        while maxheap and len(res)<10:
            negTime,tweetId,followee,index=heapq.heappop(maxheap)
            res.append(tweetId)
            if index>=0:
                time,tweetId=self.tweetmap[followee][index]
                heapq.heappush(maxheap,(-time,tweetId,followee,index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
