class User:
    #when the object is created it constructs the object
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0
    def __str__(self):
        return "This is the object for the %s" % self.username
    def follow(self,user):
        user.followers +=1
        self.following +=1
        
        
        
        
user_1 = User("Faisal",2)
user_2 = User("Ali",3)
user_1.follow(user_2)
print(user_1.username)
print(user_2.username)
print(user_1.following)
print(user_2.followers)