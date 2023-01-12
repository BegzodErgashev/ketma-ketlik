# # kk13
# x = int(input("x="))
# s = 0
# while x != 0:
#     if x > 0:
#         s += x
#     x = int(input("x="))
# print(s)


# # kk11
# n = int(input("n="))
# k = int(input("k="))
# b = True
# for i in range(1, n + 1):
#     x = int(input("x="))
#     if x < k:
#         # print(True)
#         b*=b
#     else:
#         b = False
#         # print(False)
#         b*=b
# print(b)


# # kk20
#
# n = int(input("n="))
# b = int(input("x="))
# k = 0
# while n > 1:
#     x = int(input("x="))
#     if x > b:
#         print(b)
#         b = x
#         k += 1
#     else:
#         b = x
#     n -= 1
# print("k=", k)

# # kk1
# n = int(input("n="))
# s = 0
# for i in range(1, n + 1):
#     x = float(input("x="))
#     s += x
# print(s)

# # kk2
# n = int(input("n="))
# s = 1
# for i in range(1, n + 1):
#     x = float(input("x="))
#     s *= x
# print(s)


# # kk3
# n = int(input("n="))
# s = 0
# for i in range(1, n + 1):
#     x = float(input("x="))
#     s += x
# s = s/n
# print(s)

# # kk5
# n = int(input("n="))
# s = 0
# for i in range(1, n + 1):
#     x = float(input("x="))
#     print(int(x))
#     s += int(x)
# print(s)

# # # kk6
# n = int(input("n="))
# s = 0
# for i in range(1, n + 1):
#     x = float(input("x="))
#     frac = x % 1 * 10
#     print(frac)
#     print(type(frac))
#     s += frac
# print(s)

# # kk7
# n = int(input("n="))
# s = 0
# while n > 0:
#     x = float(input("x="))
#     print(round(x))
#     s += round(x)
#     n -= 1
# print(s)

# # kk8
# n = int(input("n="))
# k = 0
# for i in range(1, n + 1):
#     x = int(input("x="))
#     if x % 2 == 0:
#         print(x)
#         k += 1
# print("juft sonlar soni", k)

# kk15

x=k = int(input("x="))
while k>0:
    k = int(input("k="))
    if x<k:
        print(k)
    else:
        print(0)
