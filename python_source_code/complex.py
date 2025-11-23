class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img


    def showResult(self):
        print(self.real,"i" ,self.img,"j")

    
    def __add__(self,num):
        newReal=self.real+num.real
        newImg=self.img+num.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num):
        newReal=self.real-num.real
        newImg=self.img-num.img
        return Complex(newReal,newImg)
    
c=Complex(3,5)
c.showResult()
c1=Complex(6,7)
c1.showResult()
num3=c-c1
num3.showResult()
        