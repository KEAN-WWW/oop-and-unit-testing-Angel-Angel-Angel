from app.add import add
from app.sub import sub
from app.mul import mul
from app.div import div
class Calculator(object):
    @staticmethod
    def addi(self, vala, valb):
        return add(vala, valb)

    @staticmethod
    def subt(self, vala, valb):
        return sub(vala,valb)

    @staticmethod
    def multi(self, vala, valb):
        return mul(vala,valb)

    @staticmethod
    def divi(self, vala, valb):
        return div(vala,valb)
