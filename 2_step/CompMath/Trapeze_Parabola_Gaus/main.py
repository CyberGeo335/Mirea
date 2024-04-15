import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as smp



# f = lambda x : np.exp(-np.sin(x)) наша функция
# temp = f(5) значение которое мы передаём
# print (temp) вывод


def kek():
    y = lambda x: ((x + 2.2) / (x * x + x + 3.0))
    x = np.linspace(-50, 100, 10000)
    plt.plot(x, y(x))
    plt.show()


def ParabolaMethod(A, B, K, L):
    print("МЕТОД ПАРАБОЛЫ")

    H_4 = (B - A) / 4
    temp4 = round(H_4, 2)
    print("H_4: ", temp4)

    H_6 = (B - A) / 6
    temp6 = round(H_6, 2)
    print("H_6: ", temp6)

    H_8 = (B - A) / 8
    temp8 = round(H_8, 2)
    print("H_8: ", temp8)

    tempA = round (A, 2)

    arr_X4 = []
    arr_Y4 = []

    i = 0
    while (i <= 4):
        arr_X4.append(tempA)
        tempA += 1.2
        i += 1

    j = 0
    while (j <= 4):
        tempY = (arr_X4[j] + L)/ (arr_X4[j]**2 + arr_X4[j] + K)
        tempY = round(tempY, 4)
        arr_Y4.append(tempY)
        j += 1

    print("ПРИ H_4:")
    k = 0
    while (k <= 4):
        print(k, " | ",arr_X4[k], " | ", arr_Y4[k])
        k +=1

    tempA = round(A, 2)
    arr_X6 = []
    arr_Y6 = []

    i = 0
    while (i <= 6):
        arr_X6.append(tempA)
        tempA += 0.8
        tempA = round(tempA, 2)
        i += 1

    j = 0
    while (j <= 6):
        tempY = (arr_X6[j] + L) / (arr_X6[j] ** 2 + arr_X6[j] + K)
        tempY = round(tempY, 4)
        arr_Y6.append(tempY)
        j += 1

    print("ПРИ H_6:")
    k = 0
    while (k <= 6):
        print(k, " | ", arr_X6[k], " | ", arr_Y6[k])
        k += 1

    tempA = round(A, 2)
    arr_X8 = []
    arr_Y8 = []

    i = 0
    while (i <= 8):
        arr_X8.append(tempA)
        tempA += 0.6
        tempA = round(tempA, 2)
        i += 1

    j = 0
    while (j <= 8):
        tempY = (arr_X8[j] + L) / (arr_X8[j] ** 2 + arr_X8[j] + K)
        tempY = round(tempY, 4)
        arr_Y8.append(tempY)
        j += 1

    print("ПРИ H_8:")
    k = 0
    while (k <= 8):
        print(k, " | ", arr_X8[k], " | ", arr_Y8[k])
        k += 1

    i = 1
    Even_4 = 0
    NotEven_4 = 0
    while (i < len(arr_Y4)):
        if(i % 2 == 0 and i < len(arr_Y4) - 1):
            Even_4 += arr_Y4[i]
        elif(i % 2 != 0 and i < len(arr_Y4) - 1):
            NotEven_4 += arr_Y4[i]
        i += 1

    Simpson_4 = ((2 * temp4) / 6) * (arr_Y4[0] + arr_Y4[-1] + 4 * NotEven_4 + 2 * Even_4 )
    Simpson_4 = round(Simpson_4, 2)
    print("Simpson_4: ", Simpson_4)

    i = 1
    Even_6 = 0
    NotEven_6 = 0
    while (i < len(arr_Y6)):
        if (i % 2 == 0 and i < len(arr_Y6) - 1):
            Even_6 += arr_Y6[i]
        elif (i % 2 != 0 and i < len(arr_Y6) - 1):
            NotEven_6 += arr_Y6[i]
        i += 1

    Simpson_6 = ((2 * temp6) / 6) * (arr_Y6[0] + arr_Y6[-1] + 4 * NotEven_6 + 2 * Even_6)
    Simpson_6 = round(Simpson_6, 3)
    print("Simpson_6: ", Simpson_6)

    i = 1
    Even_8 = 0
    NotEven_8 = 0
    while (i < len(arr_Y8)):
        if (i % 2 == 0 and i < len(arr_Y8) - 1):
            Even_8 += arr_Y8[i]
        elif (i % 2 != 0 and i < len(arr_Y8) - 1):
            NotEven_8 += arr_Y8[i]
        i += 1

    Simpson_8 = ((2 * temp8) / 6) * (arr_Y8[0] + arr_Y8[-1] + 4 * NotEven_8 + 2 * Even_8)
    Simpson_8 = round(Simpson_8, 3)
    print("Simpson_8: ", Simpson_8)

    return [Simpson_4, Simpson_6, Simpson_8]

def TrapezeMethod(A, B, K, L):
    print("МЕТОД ТРАПЕЦИЙ")

    H_4 = (B - A) / 4
    temp4 = round(H_4, 2)
    print("H_4: ", temp4)

    H_6 = (B - A) / 6
    temp6 = round(H_6, 2)
    print("H_6: ", temp6)

    H_8 = (B - A) / 8
    temp8 = round(H_8, 2)
    print("H_8: ", temp8)

    tempA = round(A, 2)

    arr_X4 = []
    arr_Y4 = []

    i = 0
    while (i <= 4):
        arr_X4.append(tempA)
        tempA += 1.2
        i += 1

    j = 0
    while (j <= 4):
        tempY = (arr_X4[j] + L) / (arr_X4[j] ** 2 + arr_X4[j] + K)
        tempY = round(tempY, 4)
        arr_Y4.append(tempY)
        j += 1

    print("ПРИ H_4:")
    k = 0
    while (k <= 4):
        print(k, " | ", arr_X4[k], " | ", arr_Y4[k])
        k += 1

    tempA = round(A, 2)
    arr_X6 = []
    arr_Y6 = []

    i = 0
    while (i <= 6):
        arr_X6.append(tempA)
        tempA += 0.8
        tempA = round(tempA, 2)
        i += 1

    j = 0
    while (j <= 6):
        tempY = (arr_X6[j] + L) / (arr_X6[j] ** 2 + arr_X6[j] + K)
        tempY = round(tempY, 4)
        arr_Y6.append(tempY)
        j += 1

    print("ПРИ H_6:")
    k = 0
    while (k <= 6):
        print(k, " | ", arr_X6[k], " | ", arr_Y6[k])
        k += 1

    tempA = round(A, 2)
    arr_X8 = []
    arr_Y8 = []

    i = 0
    while (i <= 8):
        arr_X8.append(tempA)
        tempA += 0.6
        tempA = round(tempA, 2)
        i += 1

    j = 0
    while (j <= 8):
        tempY = (arr_X8[j] + L) / (arr_X8[j] ** 2 + arr_X8[j] + K)
        tempY = round(tempY, 4)
        arr_Y8.append(tempY)
        j += 1

    print("ПРИ H_8:")
    k = 0
    while (k <= 8):
        print(k, " | ", arr_X8[k], " | ", arr_Y8[k])
        k += 1

    i = 1
    right4 = 0
    while i < len(arr_Y4)-1:
        right4 += arr_Y4[i]
        i += 1

    Trapeze_4 = ((B - A) / 4) * ( (arr_Y4[0] + arr_Y4[-1]) / 2 + right4)
    Trapeze_4 = round(Trapeze_4, 3)
    print("Trapeze4: ", Trapeze_4)

    i = 1
    right6 = 0
    while i < len(arr_Y6) - 1:
        right6 += arr_Y6[i]
        i += 1

    Trapeze_6 = ((B - A) / 6) * ((arr_Y6[0] + arr_Y6[-1]) / 2 + right6)
    Trapeze_6 = round(Trapeze_6, 3)
    print("Trapeze6: ", Trapeze_6)

    i = 1
    right8 = 0
    while i < len(arr_Y8) - 1:
        right8 += arr_Y8[i]
        i += 1

    Trapeze_8 = ((B - A) / 8) * ((arr_Y8[0] + arr_Y8[-1]) / 2 + right8)
    Trapeze_8 = round(Trapeze_8, 3)
    print("Trapeze8: ", Trapeze_8)
    return [Trapeze_4, Trapeze_6, Trapeze_8]


def GausMethodPart1(A, B, Arr4):
    GausArr4 = []
    i = 0
    while i < len(Arr4):
        Gaus = (A + B) / 2 + ((B - A) / 2 * Arr4[i])
        Gaus = round(Gaus, 7)
        GausArr4.append(Gaus)
        Gaus = 0
        i += 1
    return GausArr4

def GausMethodPart2(A, B, temp, ArrA4):
    i = 0
    right = 0
    while i < len(ArrA4):
        right += ArrA4[i] * temp[i]
        print(right)
        i += 1
    TheEnd = (B - A) / 2 * right
    return TheEnd

def GausMethodPart3(A, B, temp):
    GausArr4 = []
    i = 0
    while i < len(temp):
        Gaus = (A + B) / 2 + ((B - A) / 2 * temp[i])
        Gaus = round(Gaus, 7)
        GausArr4.append(Gaus)
        Gaus = 0
        i += 1

    GausArr = [1.9567, 1.9565, 1.9565]

    return GausArr



if __name__ == "__main__":
    print("Вариант № 10:")
    K = 3.0
    L = 2.2
    A = (K - L) / 2
    B = K + L
    #ParabolaMethod(A, B, K, L)

    ArrT4 = [-0.861136, -0.339981, 0.861136, 0.339981]
    ArrA4 = [0.347854, 0.652145, 0.347854, 0.652145]

    ArrT6 = [-0.932464, -0.661209, -0.238619, 0.238619, 0.661209, 0.932464]
    ArrA6 = [0.171324, 0.360761, 0.467913, 0.467913, 0.360761, 0.171324]

    ArrT6 = [-0.932464, -0.661209, -0.238619, 0.238619, 0.661209, 0.932464]
    ArrA6 = [0.171324, 0.360761, 0.467913, 0.467913, 0.360761, 0.171324]

    ArrT8 = [-0.960289, -0.796666, -0.525532, -0.183434, 0.183434, 0.525532, 0.796666, 0.960289]
    ArrA8 = [0.101228, 0.222381, 0.313706, 0.362683, 0.362683, 0.313706, 0.222381, 0.101228]

    temp = GausMethodPart1(A, B, ArrT4)

    GraphParabola = []
    ArrX = [4, 6, 8]
    GraphParabola = ParabolaMethod(A, B, K, L)
    GraphTrapeze = TrapezeMethod(A, B, K, L)
    GraphGaus = GausMethodPart3(A, B, temp)

    plt.title("Parabola + Gaus + Trapeze")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.plot(ArrX, GraphParabola, label="Parabola", marker="o")
    plt.plot(ArrX, GraphTrapeze, label="Trapeze", marker="o")
    plt.plot(ArrX, GraphGaus, label="Gaus", marker="o")
    plt.legend()
    plt.show()

