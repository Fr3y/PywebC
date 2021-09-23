admin = {"yerf":19, "Binny" :20, "pinchu":17}
print(admin[19])


d = {1:1, 2:4, 3:"lol", 4:"pinchu"}
d[8] = 64
d[3] = 9
print(d[2])
print(d[8])
d[99] = "samurai"
print(d[99])


a = {
  1: "tum",
  2: "hum",
  3: "sub",
}

print(4 in a)
print(1 in a)
print(3 in a)

# get method uwu

D = {1: "apple",
  "orang": [2,3,4],
  True: False,
  None: "True",
}

print(D.get("orang"))
print(D.get(7))
print(D.get(122332, "this is fucked up"))


# get method uwu

D = {1: "apple",
  "orang": [2,3,4],
  True: False,
  None: "True",
}

print(D.get("orang"))
print(D.get(1))
print(D.get(7))
print(D.get(122332, "this is fucked up"))

#Make a TypeError

# tuples are similar to list but they are immutabl
uwu = "one piece", "Death Note", "Tokyo Revengers"

print(uwu[1])
