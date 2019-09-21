class One:
    classvar = 33
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else 'vasia'
        self._age = kwargs['age'] if 'age' in kwargs else 18
        self.x = [22,42, 17]
        
    def name(self, n=None):
        if n:
            self._name = n
        return self._name
        
    def age(self, a=None):
        if a:
            self._age = a
        return self._age

    def __str__(self):
        return (f'{self.classvar}-{self.x[0]:2}:My name is {self.name()} and I am {self.age()} years old.')
        
def main():
    person1 = One(name='Nazar', age=17)
    person2 = One(name='Anton', age = 14)
  #  person1.classvar=31415
    print(id(person1.classvar))
    print(id(person2.classvar))
    print(id(person1))
    print(id(person2))
    person1.x[0] = 42
    person2.x[0] = 2
    print(person1)
    print(person2)

if __name__ == '__main__':main()