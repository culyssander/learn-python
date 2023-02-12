friends = ["Raul", "Inock", "Quitumba", "Quinha"]

print(friends)
print(friends[-1])
print(friends[1:])
print(friends[1:3])


lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends.extend(lucky_numbers)
friends.append("Manuel")
print(friends)

friends.insert(1, "Bebucho")
print(friends)

friends.remove("Quitumba")
print(friends)

# friends.clear()
# print(friends)

print(friends.pop())
print(friends.index("Inock"))

print(len(friends))

print(friends.count("Raul"))
lucky_numbers.reverse()
print(lucky_numbers)
