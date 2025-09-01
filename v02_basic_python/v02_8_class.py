# 1. 클래스 정의는 자유롭게
# 2. 파라미터는 self 제외 3개
# 3. 메서드 2개
# 4. 객체 생성 => 총 3개

class Fruit():
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def info(self):
        print(f"{self.name}는 {self.color}색이고, 가격은 {self.price}원 입니다.")
    def price_sum(self, fruit):
        print(f"{self.name}과 {fruit.name}의 합산 가격은 {self.price + fruit.price}원 입니다.")
        

peach = Fruit("복숭아", "peach", 3000)
kiwi = Fruit("키위", "green", 4000)
cherry = Fruit("체리", "cherry", 5000)

cherry.info()
kiwi.price_sum(peach)