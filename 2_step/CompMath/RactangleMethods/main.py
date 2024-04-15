import numpy as np
import matplotlib.pyplot as plt

def foo(H_temp, arr_X):
    i = 1
    temp = 0
    while i < len(arr_X):
        temp += (arr_X[i] + 2.2) / (arr_X[i]**2 + arr_X[i] + 3.0)
        temp = round(temp, 3)
        i += 1
    return round(H_temp * temp, 4)

def foo2(H_temp, arr_X4):
    i = 0
    sum = 0
    while i < len(arr_X4)-1:
        temp = (arr_X4[i] + 2.2) / (arr_X4[i]**2 + arr_X4[i] + 3.0)
        temp = round(temp, 4)
        sum += temp
        i += 1
    return round(H_temp * sum, 3)

def LeftRactangles(A, B, K, L):
    print("ЛЕВЫЕ ПРЯМОУГОЛЬНИКИ:")

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

    print(arr_X4)
    LeftRectangle_4 = foo2(H_4, arr_X4)
    LeftRectangle_6 = foo2(H_6, arr_X6)
    LeftRectangle_8 = foo2(H_8, arr_X8)
    print("LeftRectangle_4: ", LeftRectangle_4)
    print("LeftRectangle_6: ", LeftRectangle_6)
    print("LeftRectangle_8: ", LeftRectangle_8)
    return [LeftRectangle_4, LeftRectangle_6, LeftRectangle_8]

def RightRactangles(A, B, K, L):
    print("ПРАВЫЕ ПРЯМОУГОЛЬНИКИ:")

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

    RightRactangle_4 = foo(H_4, arr_X4)
    RightRactangle_6 = foo(H_6, arr_X6)
    RightRactangle_8 = foo(H_8, arr_X8)
    print("RightRactangle_4: ", RightRactangle_4)
    print("RightRactangle_6: ", RightRactangle_6)
    print("RightRactangle_8: ", RightRactangle_8)
    return [RightRactangle_4, RightRactangle_6, RightRactangle_8]

def MiddleRactangles(A, B, K, L):
    print("СРЕДНИЕ ПРЯМОУГОЛЬНИКИ:")

    H_4 = (B - A) / 4
    temp4 = round(H_4, 2)
    print("H_4: ", temp4)

    H_6 = (B - A) / 6
    temp6 = round(H_6, 2)
    print("H_6: ", temp6)

    H_8 = (B - A) / 8
    temp8 = round(H_8, 2)
    print("H_8: ", temp8)

    arr_Xi_4 = []
    TempX = A + H_4 / 2
    i = 1
    arr_Xi_4.append(TempX)
    while i < 4:
        TempX += H_4
        arr_Xi_4.append(round(TempX,4))
        i += 1

    i = 0
    sum = 0
    while i < 4:
        sum += (arr_Xi_4[i] + 2.2 ) / (arr_Xi_4[i]**2 + arr_Xi_4[i] + 3.0)
        i += 1
    MiddleRactangle_4 = round(1.2 * sum, 3)

    arr_Xi_6 = []
    TempX = A + H_6 / 2
    i = 1
    arr_Xi_6.append(TempX)
    while i < 6:
        TempX += H_6
        arr_Xi_6.append(round(TempX,3))
        i += 1

    i = 0
    sum = 0
    while i < 6:
        sum += (arr_Xi_6[i] + 2.2 ) / (arr_Xi_6[i]**2 + arr_Xi_6[i] + 3.0)
        i += 1
    MiddleRactangle_6 = round(0.8 * sum, 3)


    arr_Xi_8 = []
    TempX = A + H_8 / 2
    i = 1
    arr_Xi_8.append(TempX)
    while i < 8:
        TempX += H_8
        arr_Xi_8.append(round(TempX,3))
        i += 1

    i = 0
    sum = 0
    while i < 8:
        sum += (arr_Xi_8[i] + 2.2 ) / (arr_Xi_8[i]**2 + arr_Xi_8[i] + 3.0)
        i += 1
    MiddleRactangle_8 = round(0.6 * sum, 3)

    print("MiddleRactangle_4: ", MiddleRactangle_4)
    print("MiddleRactangle_6: ", MiddleRactangle_6)
    print("MiddleRactangle_8: ", MiddleRactangle_8)

    return [MiddleRactangle_4, MiddleRactangle_6, MiddleRactangle_8]

if __name__ == "__main__":
    K = 3.0
    L = 2.2
    A = (K - L) / 2
    B = K + L

    ArrX = [4, 6, 8]
    GraphRightRactangles = RightRactangles(A, B, K, L)
    GraphLeftRactangles = LeftRactangles(A, B, K, L)
    GraphMiddleRactangless = MiddleRactangles(A, B, K, L)

    plt.title("RightRactangles + LeftRactangles + MiddleRactangles")
    plt.xlabel("OX")
    plt.ylabel("OY")

    plt.plot(ArrX, GraphRightRactangles, label = "RightRactangles", marker = "o")
    plt.plot(ArrX, GraphLeftRactangles, label = "LeftRactangles", marker = "^")
    plt.plot(ArrX, GraphMiddleRactangless, label="MiddleRactangles", marker = "o")

    plt.legend()
    plt.show()
