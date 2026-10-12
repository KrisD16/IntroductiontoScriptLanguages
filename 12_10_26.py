# # REVISION FOR ARRAYS AND DICTIONARIES

# my_nums = [3, 4, 7, 13, 20]
# my_strs = ["Petar", "Ivan", "Ogi"]

# my_nums[0]  # -> 3
# my_nums[2:4]  # -> 7, 13

# data = {
#     "name": "Petar",
#     "age": 48,
# }

# data["name"]  # -> Petar

# for k in data:
#     print(k)  # -> name, age (KEYS)

# for k, v in data.items():
#     print(k, v)  # -> name, Petar; age, 48 (KEY, VALUE)

# data.remove("name")
# data["city"] = "Sofia"

# ########################################

# for i, num in enumerate(my_nums):
#     if i % 2 == 0:
#         print(num)  # -> Indexes: 0, 2, 4; Values: 3, 7, 20

############## HOMEWORK 1 ################

# # ENCODING RLE
# to_encode = input("Enter a string: ")
# out = ""
# count = 0
# symbol = ""

# for s in to_encode:
#     if s == symbol:
#         count += 1
#     else:
#         if count > 0:
#             out += "{}{}".format(symbol, count)  # out += f"{symbol}{count}"
#         symbol = s
#         count = 1
# out += f"{symbol}{count}"

# print(out)

# # DECODING RLE
# to_decode = input("Enter a string: ")
# out = ""
# count = 0
# symbol = ""

# for i in range(0, len(to_decode)):
#     if i % 2 == 0:
#         symbol = to_decode[i]
#     else:
#         count = int(to_decode[i])
#         for j in range(1, count + 1):
#             out += symbol

# print(out)

# # .isalpha() -> returns True if every symbol in a string is a character("Koko", "Ivan", ...), returns False otherwise("Brat1", "Koko68", ...)

# #########################################

# text = "Hello"
# text += "Petar"  # -> HelloPetar
# name = "Petar"
# text = "Hello {}".format(name)  # --> STRING
# text = f"Hello {name}"  ######### --> FORMATING


# wel = """Welcome {}, to the server"""

# # def join(name):
# #     print(wel.format(name))

# wel.isalpha()  #
# wel.isdigit()  #
# wel.isalnum()  # --> BUILT-IN FUNCTIONS
# wel.isascii()  # --> IN DOCUMENTATION FOR REFERENCE
# wel.islower()  #
# wel.isupper()  #

#########################################

# EXERCISE

text = input("Enter sentence: ")
# indexes = []
# count = 0

# for i in range(0, len(text)):
#     if text[i] == " ":
#         count += 1
#         if count > 1:
#             indexes[count - 1] = i
#     else:
#         if count > 1:
#             for j in indexes:
#                 text[j] = ""
#         count = 0
# print(text)

out = ""

for i, symbol in enumerate(text):
    if symbol == " ":
        if text[i + 1].isalnum():
            out += symbol
    else:
        out += symbol

print(out)
