import random
xx = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
yy = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289]

class NeroNet():
    def __init__(self, w1,w2,w3,w4,w5,w6,b1,b2,b3,b4):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.w5 = w5
        self.w6 = w6
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def rely(self,x):
        if x > 0:
            return x
        else: return 0
    def firs_liner(self,x):
        n1_s = x*self.w1 + self.b1
        n2_s = x*self.w2 + self.b2
        n3_s = x*self.w3 + self.b3
        n1 = self.rely(n1_s)
        n2 = self.rely(n2_s)
        n3 = self.rely(n3_s)
        out = [n1,n2,n3]
        relyon = [n1_s, n2_s,n3_s ]
        return out, relyon
    def end_liner(self, x):
        y = x[0]*self.w4 + x[1]*self.w5 + x[2]*self.w6 + self.b4
        r = [x[0],x[1],x[2]]
        return y, r
    def funOn(self, x):
        s, relyonornot = self.firs_liner(x)
        y, r = self.end_liner(s)
        return y, r, relyonornot
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
w3 = random.uniform(-1, 1)
w4 = random.uniform(-1, 1)
w5 = random.uniform(-1, 1)
w6 = random.uniform(-1, 1)
b1 = random.uniform(-5, 5)
b2 = random.uniform(-5, 5)
b3 = random.uniform(-5, 5)
b4 = random.uniform(-1, 1)
neuroNet = NeroNet(w1,w2,w3,w4,w5,w6,b1,b2,b3,b4)
lr = 0.0001
for epoch in range(100000):
    for x,y in zip(xx,yy):
        y_pred, r, relyonornot = neuroNet.funOn(x)
        error = y_pred - y

        err_n1 = error * neuroNet.w4
        err_n2 = error * neuroNet.w5
        err_n3 = error * neuroNet.w6

        neuroNet.w4 -= error * lr * r[0]
        neuroNet.w5 -= error * lr * r[1]
        neuroNet.w6 -= error * lr * r[2]
        neuroNet.b4 -= error * lr

        if relyonornot[0] > 0:
            neuroNet.w1 -= err_n1 * lr * x
            neuroNet.b1 -= err_n1 * lr
        if relyonornot[1] > 0:
            neuroNet.w2 -= err_n2 * lr * x
            neuroNet.b2 -= err_n2 * lr
        if relyonornot[2] > 0:
            neuroNet.w3 -= err_n3 * lr * x
            neuroNet.b3 -= err_n3 * lr
print('Введите число:')
a = int(input())
res = neuroNet.funOn(a)
print('Возможно, ваше число выглядит так: ', res[0])

        

        
        
