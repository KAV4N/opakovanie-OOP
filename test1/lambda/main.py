# def poly():
#     return x ** 2 - 3 * x
# print(poly)
# print(poly())
#
# funkcia = poly
# print(funkcia())
#
# ahoj = print
# ahoj("hey there")

#uloha1
# lsNums = [int(x) for x in "1969,2003,1978,1980,2015".split(",")]
# print(list(sorted(lsNums, key=lambda x: str(x)[-2:])))

#uloha2
# lsData = "aaay,bbz,cx".split(",")
# switch = 2
# kriterium = [lambda x: x, lambda x: x[::-1], lambda x: len(x)]
# print(list(sorted(lsData, key=kriterium[switch])))


#uloha3
# data = []
# with open("data1.txt", "r") as file:
#     data = [list(map(int, line.split(";"))) for line in file]
# count_occurrences = lambda data, switch_value: sum(1 for row in data if row[1] == switch_value)
# print(count_occurrences(data, 6))

# uloha4
# ciferny_sucin = lambda cislo: eval('*'.join(str(abs(cislo))))
# print(ciferny_sucin(1234))

#uloha5
# inData = "Jan,Max,Alexander,Milan,Robert".split(",")
# print(sorted(filter(lambda x: len(x) >= 5,inData),reverse=True))


# uloha6
# def prvocislo(x):
#     if x == 1:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True
#
#
# cisla = [int(x) for x in " 48 5 7 1 22 10 77 13 80".split()]
# print(list(filter(prvocislo, cisla)))

# uloha7
# dvojnasobok = lambda x: x * 2
# zvysok_po_deleni_4 = lambda x: x % 4
# test_parmosti = lambda x: x % 2 == 0
#
# cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(dvojnasobok, cisla)))
# print(list(map(zvysok_po_deleni_4, cisla)))
# print(list(map(test_parmosti, cisla)))
