"""
s = "istanbul"
s2 = s
s = "ankara"
print(s, s2)
"""
"""
list1 = [10,20,30]
list2 = list1
list1 = [50, 60]
print(list1, list2)
"""
"""
list1 = [10,20,30] # lists are mutable
list2 = list1
list1[1] = 50
#list1.append(40)
print(list1, list2)
"""

import dog as d

rosie = d.Dog(name="Rosie")
kont = d.Dog(name="Kont")

rosie.addFriend("John") # I am changing a mutable class variable
print("Rosie friend list:", rosie.getFriendList())
print("Kont friend list:", kont.getFriendList())

rosie.addCloseFriend("Alice") # I am changing a mutable instance variable
print("Rosie close friends:", rosie.getCloseFriendList())
print("Kont close friends:", kont.getCloseFriendList())

rosie.changeBreed("Rottweiller")
print("Rosie breed", rosie.getBreed())
print("Kont breed", kont.getBreed())