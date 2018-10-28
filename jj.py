# for i in range(6):
#     if i == 0 or i == 5:
#         print("* " * (i + 1),end = "")
#     else:
#         print("* " + (" "* (2 * i - 2)) + "*",end = "")
#     print()
#

def hannuota(n,a,b,c):
    if n == 1:
        print(a,"=>",c)
    else:
        hannuota(n-1,a,c,b)
        hannuota(1,a,b,c)
        hannuota(n-1,b,a,c)
hannuota(3,"A","B","C")