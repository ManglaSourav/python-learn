from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.count = 0  # time or counting the number of tweets
        # userIds -> list of [count, tweetId]
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)  # userIds -> set of userids

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # order starting from the most recent
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # get the index of recent tweet of followee
                index = len(self.tweetMap[followeeId]) - 1
                # get the most recent tweet using index of the followee
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
# User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)  # User 1 follows user 2.
twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
# User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
# User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
print(twitter.getNewsFeed(1))
