names = ["Jose", "Alberto", "Ricardo"]
print(names[1])

sports = ["futebol, basket", "voleibol"]
sports[1] = "golf"

nums = [4 ,9 ,5, 7 ,4 ,3]
del nums[4]

nums1 = [19, 42 ,24 ,51]

nums3 = nums + nums1
print(nums3)

print(len(nums1))
print(min(nums1))
print(max(nums1))

students = {
    "aluno1" : 15,
    "aluno2" : 20,
    "aluno3" : 14
}

print(students["aluno1"])
print(students["aluno2"])
print(students["aluno3"])


pessoas = {
    "Ricardo" : 25,
    "Mike" : 35,
    "Luis" : 84
}

del pessoas["Mike"]

print(pessoas)

tup = ("The perks of being a wallflower", "The thing", "IT 2")
print(tup[0:2])
