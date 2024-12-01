# s = input("")
# x = s.split("、")
# a = []
# b = []
# n = 0
# for i in range(0, len(x)):
#     a.append(int(x[i]))
#     n = i + 1
#     b.append(n)
# for i in range(n-1):
#     for j in range(i+1, n):
#         if a[i] < a[j]:
#             a[i], a[j] = a[j], a[i]
#             b[i], b[j] = b[j], b[i]
# print(a)
# print(b)

n = int(input("请输入总人数:"))
num = []
for i in range(n):
    num.append(i+1)
i = 0
k = 0
m = 0
while m < n - 1:
    if num[i] != 0:
        k += 1
    if k == 3:
        num[i] = 0
        k = 0
        m += 1
    i += 1
    if i == n:
        i = 0
i = 0
while num[i] == 0:
    i += 1
print()

