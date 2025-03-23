class SorterMethod:

    def __init__(self,ascending=True):
        self.ascending = ascending

    def run(self, lst):
        return sorted(lst, reverse=not self.ascending)

    def __call__(self, lst):
        return sorted(lst, reverse=not self.ascending)


if __name__ == '__main__':
    sortAscending = SorterMethod(ascending=True)
    sortDescending = SorterMethod(ascending=False)
    l = [1,5,7,8,3,2]
    print(sortAscending.run(l))
    print(sortAscending(l))
    print(sortDescending.run(l))
    print(sortDescending(l))
