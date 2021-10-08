import random


def GetPassword(data):

Max = 60


password="

while len(password) != Max:

value = random.choice(data)

password += value

return password



 data = '@#$%&*-+(0123450gbnmaq'

 for i in range(20):

 print(GetPassword (data))
