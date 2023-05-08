from collections import Counter

class Estatistica:
    def __init__(self, numbers):
        self.numbers = numbers


    def media(self):
        num = 0
        for number in self.numbers:
            num += number
        return num  / len(self.numbers)
    

    def mediana(self):
        numbers = sorted(self.numbers)
        sum = 0
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            sum += numbers[index]
            sum += numbers[index - 1]
            return sum / 2
        else:
            sum += numbers[index]
        return sum
    

    def moda(self):
        counter = Counter(self.numbers)
        return counter.most_common()[0]
    


meu_estatistica = Estatistica([1,1,1,2,5,6,7])
print(meu_estatistica.media())
print(meu_estatistica.mediana())
print(meu_estatistica.moda())
    