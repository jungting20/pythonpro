class Car():
    def exclaim(self):
        print("i'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("asasdasd")

aa = Yugo()
bb = Car()
aa.exclaim()
bb.exclaim()