# PascalCase
# camelCase
# snake_case

class User():
    def __init__(self, username, user_id, age):
        self.name = username
        self.id = user_id
        self.followers = 0
        self.following = 0
        self.age = age

    def follow(self, user):
        user.followers += 1
        self.following =+1


user_1 = User("mohammad", "001", 25)
user_2 = User("ali", "002", 23)

user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_1.followers)
print(user_2.followers)

print(user_1.name)
print(user_1.id)
print(user_1.followers)
print(user_1.age)


# class User():
#     pass


# user_1 = User()
# user_1.name = "baraz"
# user_1.id = "001"
#
# print(user_1.id)
