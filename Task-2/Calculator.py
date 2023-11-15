import math
import os
#Arithmetic Operations
def Add():
    a=eval(input("Enter first number: "))
    b=eval(input("Enter second number: "))
    return print("The Sum of {0} + {1} = {2}".format(a,b,a+b))
def Sub():
    a=eval(input("Enter first number: "))
    b=eval(input("Enter second number: "))
    return print("The Sum of {0} - {1} = {2}".format(a,b,a-b))
def Mul():
    a=eval(input("Enter first number: "))
    b=eval(input("Enter second number: "))
    return print("The Sum of {0} * {1} = {2}".format(a,b,a*b))
def Div():
    a=eval(input("Enter first number: "))
    b=eval(input("Enter second number: "))
    if b==0:
        print("Division by zero Error")
    else:
        return print("The Sum of {0} / {1} = {2}".format(a,b,a/b))

#Trigonometric Operations
def Sin():
    x=eval(input("Enter in Degrees: "))
    print("The value of Sin({0}) = {1}".format(x,math.sin(math.radians(x))))
def Cos():
    x=eval(input("Enter in Degrees: "))
    print("The value of Cos({0}) = {1}".format(x,math.cos(math.radians(x))))
def Tan():
    x=eval(input("Enter in Degrees: "))
    print("The value of Tan({0}) = {1}".format(x,math.tan(math.radians(x))))
def SinI():
    x=eval(input("Enter in Degrees: "))
    print("The value of Sin⁻¹({0}) = {1}".format(x,math.asin(math.radians(x))))
def CosI():
    x=eval(input("Enter in Degrees: "))
    print("The value of Cos⁻¹({0}) = {1}".format(x,math.acos(math.radians(x))))
def TanI():
    x=eval(input("Enter in Degrees: "))
    print("The value of Tan⁻¹({0}) = {1}".format(x,math.atan(math.radians(x))))

#Hyperbolic Operations
def Sinh():
    x=eval(input("Enter in Degrees: "))
    print("The value of Sinh({0}) = {1}".format(x,math.sinh(math.radians(x))))
def Cosh():
    x=eval(input("Enter in Degrees: "))
    print("The value of Cosh({0}) = {1}".format(x,math.cosh(math.radians(x))))
def Tanh():
    x=eval(input("Enter in Degrees: "))
    print("The value of Tanh({0}) = {1}".format(x,math.tanh(math.radians(x))))
def SinhI():
    x=eval(input("Enter in Degrees: "))
    print("The value of Sinh⁻¹({0}) = {1}".format(x,math.asinh(math.radians(x))))
def CoshI():
    x=eval(input("Enter in Radians: "))
    print("The value of Cosh⁻¹({0}) = {1}".format(x,math.acosh(x)))
def TanhI():
    x=eval(input("Enter in Degrees: "))
    print("The value of Tanh⁻¹({0}) = {1}".format(x,math.atanh(math.radians(x))))

#Other Operations
def Xpn():
    x=eval(input("Enter x value: "))
    n=eval(input("Enter n value: "))
    return print("The value of {0}ⁿ: {0}^{1} = {2}".format(x,n,math.pow(x,n)))
def Xpt():
    x=eval(input("Enter x value: "))
    return print("The value of {0}² = {1}".format(x,math.pow(x,2)))
def Xpth():
    x=eval(input("Enter x value: "))
    return print("The value of {0}³ = {1}".format(x,math.pow(x,3)))
def logex():
    x=eval(input("Enter x value: "))
    return print("The value of logℯ{0} = {1}".format(x,math.log(x)))
def logx():
    x=eval(input("Enter x value: "))
    return print("The value of log{0} = {1}".format(x,math.log10(x)))
def Sqrtx():
    x=eval(input("Enter x value: "))
    return print("The value of √{0} = {1}".format(x,math.sqrt(x)))
def Cbrtx():
    x=eval(input("Enter x value: "))
    return print("The value of ∛{0} = {1}".format(x,x**(1/3)))
def Ntrtx():
    x=eval(input("Enter x value: "))
    n=eval(input("Enter n value: "))
    return print("The value of {2}√{0} = {1}".format(x,x**(1/n),n))
def Epn():
    n=eval(input("Enter n value: "))
    return print("The value of eⁿ: e^{0} = {1}".format(n,math.pow(math.e,2)))

print("Operations")
print("1. Arithmetic\n2. Trigonometric\n3. Hyperbolic\n4. Other")
i=int(input("Choose operation: "))
if i==1:
    print("\n\nArithmetic Operations")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    i=int(input("Choose Option: "))
    if i==1:
        Add()
    elif i==2:
        Sub()
    elif i==3:
        Mul()
    elif i==4:
        Div()
elif i==2:
    print("\n\nTrigonometric Operations")
    print("1. Sin\n2. Cos\n3. Tan\n4. Sin⁻¹\n5. Cos⁻¹\n6. Tan⁻¹")
    i=int(input("Choose Option: "))
    if i==1:
        Sin()
    elif i==2:
        Cos()
    elif i==3:
        Tan()
    elif i==4:
        SinI()
    elif i==5:
        CosI()
    elif i==6:
        TanI()
elif i==3:
    print("\n\nHyperbolic Operations")
    print("1. Sinh\n2. Cosh\n3. Tanh\n4. Sinh⁻¹\n5. Cosh⁻¹\n6. Tanh⁻¹")
    i=int(input("Choose Option: "))
    if i==1:
        Sinh()
    elif i==2:
        Cosh()
    elif i==3:
        Tanh()
    elif i==4:
        SinhI()
    elif i==5:
        CoshI()
    elif i==6:
        TanhI()
elif i==4:
    print("\n\nOther Operations")
    print("1. Xⁿ\n2. X²\n3. X³\n4. LogℯX\n5. LogX\n6. √X\n7. ∛\n8. n√\n9. eⁿ")
    i=int(input("Choose Option: "))
    if i==1:
        Xpn()
    elif i==2:
        Xpt()
    elif i==3:
        Xpth()
    elif i==4:
        logex()
    elif i==5:
        logx()
    elif i==6:
        Sqrtx()
    elif i==7:
        Cbrtx()
    elif i==8:
        Ntrtx()
    elif i==9:
        Epn()

os.system("pause")
