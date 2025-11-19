class Dog:
    # class variables
    breed = "Poodle"
    friends = []

    def __init__(self, name):
        # instance variable
        self.name = name
        self.closeFriends = []
    
    def addFriend(self, newFriend):
        self.friends.append(newFriend)
    
    def getFriendList(self):
        return self.friends
    
    def addCloseFriend(self, newFriend):
        self.closeFriends.append(newFriend)
    
    def getCloseFriendList(self):
        return self.closeFriends
        
    # setter
    def changeBreed(self, newBreed):
        self.breed = newBreed
    
    # getter
    def getBreed(self):
        return self.breed