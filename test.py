from algorithm.apriori import combineItemSets


def testyield(r):
    a = 0
    for i in range(r):
        yield a
        a = a + 1
        a = a + 2


def main():
    # print("Hello World! \n")
    # aSet = [set(["a","b"]), set(["b","c"]), set(["a""c"])]
    # cSet = combineItemSets(aSet)
    # print(cSet)

    generator = testyield(5)

    for item in generator:
        print(item)

if __name__ == "__main__":
    main()


