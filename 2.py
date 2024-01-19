import random
class Mylist(list):
    def __init__(self,N):
        self.N=[random.randint(-100,100) for i in range(N)]
    def get_random_number(self):
        return f"{N} uzunlikda random sonlar {self.N}"
N=int(input('N: '))
lst=Mylist(N)
print(lst.get_random_number())