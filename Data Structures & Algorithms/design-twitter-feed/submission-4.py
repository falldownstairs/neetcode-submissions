class Twitter:

    def __init__(self):
        self.accounts = {}
        self.time = 0
        self.tweets = []
        self.tweetUsers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(tweetId)
        self.tweetUsers[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = 1
        if userId not in self.accounts.keys():
            self.accounts[userId] = set([userId])
        while len(res) < 10 and i <= len(self.tweets):
            if self.tweetUsers[self.tweets[-i]] in self.accounts[userId]:
                res.append(self.tweets[-i])
            i+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.accounts.keys():
            self.accounts[followerId] = set([followerId])
        self.accounts[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followerId in self.accounts.keys() and followeeId in self.accounts[followerId]:
            self.accounts[followerId].remove(followeeId)
