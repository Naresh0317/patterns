	# Right-Angled Triangle (Left-Aligned)# n=5
# for i in range(1,n+1):
#     stars=""
#     for j in range(1,i+1):
#         stars+="* "
#     print(stars)
	# Right-Angled Triangle (Right-Aligned)
n=5
# for i in range(1,n+1):
#     spaces=""
#     for  j in range(n-i,0,-1):
#         spaces+="  "
#     stars=""
#     for k in range(1,i+1):
#         stars+="* "
#     print(spaces+stars)
# 5.	Inverted Triangle (Left-Aligned)
# n=5
# for i in range(n,0,-1):
#     stars=""
#     for j in range(1,i+1):
#         stars+="* "
#     print(stars)
# 6.	Inverted Triangle (Right-Aligned)
# n=5
# for i in range(n,0,-1):
#     space=""
#     for j in range(n,i,-1):
#         space+="  "
#     stars=""
#     for k in range(1,i+1):
#         stars+="* "
#     print(space+stars)
# 7.	Centered Pyramid Pattern
# n=5
# for i in range(1,n+1):
#     space=""
#     for j in range(n,i,-1):
#         space+="  "
#     stars=""
#     for k in range(1,2*i):
#         stars+="* "
#     print(space+stars)
# 7.	 inverted Centered Pyramid Pattern
# n=5
# for i in range(n,0,-1):
#     space=""
#     for j in range(n,i,-1):
#         space+="  "
#     stars=""
#     for k in range(1,2*i):
#         stars+="* "
#     print(space+stars)
# 10.	Left-Aligned Half Diamond
# n=5
# for i in range(1,n+1):
#     stars=""
#     for j in range(1,i+1):
#         stars+="* "
#     print(stars)
# for i in range(n-1,0,-1):
#     stars=""
#     for k in range(1,i+1):
#         stars+="* "
#     print(stars)
# n=5
# for i in range(1,n+1):
#     space=""
#     for j in range(n-i):
#         space+="  "
#     stars=""
#     for k in range(1,i+1):
#         stars+="* "
#     print(space+stars)
# for i in range(n-1,0,-1):
#     space=""
#     for j in range(n-i):
#         space+="  "
#     stars=""
#     for k in range(1,i+1):
#         stars+="* "
#     print(space+stars)
# for i in range(1,n+1):
#     stars=""
#     for j in range(1,i+1):
#         stars+="* "
#     space=""
#     for k in range(1,(n-i)*2+1):
#         space+="  "
#     star=""
#     for l in range(1,i+1):
#         star+="* "
#     print(stars+space+star)
# for i in range(n-1,0,-1):
#     stars=""
#     for j in range(1,i+1):
#         stars+="* "
#     space=""
#     for k in range(1,(n-i)*2+1):
#         space+="  "
#     star=""
#     for l in range(1,i+1):
#         star+="* "
#     print(stars+space+star)
# for i in range(1,n+1):
#    stars=""
#    for j in range(1,i+1):
#       if i==1 or i==n:
#          stars+="* "
#       elif j==1 or j==i :
#          stars+="* "
#       else:
#          stars+="  "
#    print(stars)
# n=5
# for i in range(n,0,-1):
#    stars=""
#    for j in range(1,i+1):
#       if i==1 or i==n:
#          stars+="* "
#       elif j==1 or j==i :
#          stars+="* "
#       else:
#          stars+="  "
#    print(stars)
# n=5
# for i in range(1,n+1):
#    space=""
#    stars=""
#    for j in range(n,i,-1):
#       space+="  "
#    for k in range(1,2*i):
#       if i==n or i==1:
#          stars+="* "
#       elif k==1 or k==2*i-1:
#          stars+="* "
#       else:
#          stars+="  "
#    print(space+stars)

# n = 5
# for i in range(1, n + 1):
#     stars = ""
#     space = ""

#     for j in range(n, i, -1):
#         space += "  "
#     for k in range(1, 2 * i):
#         if i == 1:
#             stars += "* "
#         elif k == 1 or k == 2 * i - 1:
#             stars += "* "
#         else:
#             stars += "  "
#     print(space + stars)
# for i in range(n - 1, 0, -1):
#     stars = ""
#     space = ""
#     for j in range(n, i, -1):
#         space += "  "
#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1:
#             stars += "* "
#         else:
#             stars += "  "
#     print(space + stars)
# n=5
# for i in range(1,n+1):
#    stars=""
#    for j in range(1,i+1):
#       if i==1 or i==n:
#          stars+="* "
#       elif j==1 or j==i:
#           stars+="* "
#       else:
#           stars+="  "
#    space=""
#    for k in range(1,(n-i)*2-)
n = 4

# upper half
# for i in range(1, n + 1):

#     stars = ""

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             stars += "* "
#             stars+=" *"
#         else:
#             stars += "  "

#     spaces = ""

#     for k in range((n - i) * 2):
#         spaces += "  "

#     print(stars + spaces + stars)


# # lower half
# for i in range(n - 1, 0, -1):

#     stars = ""

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             stars += "* "
#         else:
#             stars += "  "

#     spaces = ""

#     for k in range((n - i) * 2):
#         spaces += "  "

#     print(stars + spaces + stars)


num=123
sum=0
mul=1
while num!=0:
    rem=num%10
    sum+=rem
    mul*=rem
    num=num//10
if sum==mul:
    print("secret number")
else:
    print("not secret")