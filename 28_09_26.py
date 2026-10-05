# # x = int(input("Enter a number: "))

# # if x > 3 and x < 10:
# #     print("  ")
# # elif x >= 0 and x < 20:
# #     print("13")
# # else:
# #      print("Deny")
# # ---------------------------
# # while True:
# #     print("Hello")
# # ---------------------------
# # a = [3, 4, 7, 8]
# # a.pop()
# # a.append(9)
# # a[1] -> 4
# # a[-1] -> 8
# # a[1:3] -> 4, 7
# # ---------------------------
# # for n in a:
# #   print(n)
# # print("Finish")

# # for n in a:
# # if n % 2 == 0:
# #  print(n, "is even")
# # else:
# # print(n, "is odd")

# # a = []
# # for n in range(5):
# # number = int(input("Enter a number: "))
# # a.append(number)
# # print(a)

# n = int(input("Enter a number(>= 2 and <= 1000): "))
# i = 2
# isPrime = True

# while i - 2 < n:
#     if n % i == 0:
#         isPrime = False
#         break
#     i += 1


# if isPrime:
#     print(n, "isn't prime")
# else:
#     print(n, "is prime")


def isPalindrome(a: int, d: int) -> bool:
    for i in range(0, d // 2):
        if :
            return False
    return True


n = int(input("Enter a number: "))
m = n
digits = 0
while m > 0:
    m /= 10
    digits += 1

if isPalindrome(n, digits):
    print(n, "is palindrome")
else:
    print(n, "isn't palindrome")
