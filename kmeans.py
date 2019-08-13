import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas import DataFrame

def read_data():
    data_n_stress = pd.read_csv('AI-Practice02-Data-notStressed.csv')
    data_stress = pd.read_csv('AI-Practice02-Data-Stressed.csv')
    n_stress_li = data_n_stress.values.tolist()
    stress_li = data_stress.values.tolist()
    return n_stress_li, stress_li

def plot_data(class_1, class_2=None, fault=None):
    plt.scatter([x[1] for x in class_1], [x[0] for x in class_1], s=15, c='g')
    plt.scatter([x[1] for x in class_2], [x[0] for x in class_2], s=15, c='b')
    if fault!=None:
        plt.scatter([x[1] for x in fault], [x[0] for x in fault], s=15, c='r')
    plt.show()

def accuracy(p_n_s, p_s, test_n_s, test_s):
    fault = []
    for i in range(len(p_n_s)):
        f = 1
        for j in range(len(test_n_s)):
            if test_n_s[j] == p_n_s[i]:
                f = 0
                break
        if f==1:
            fault.append(p_n_s[i])
    for i in range(len(p_s)):
        f = 1
        for j in range(len(test_s)):
            if test_s[j] == p_s[i]:
                f = 0
                break
        if f==1:
            fault.append(p_s[i])
    accuracy = (1-len(fault)/(len(test_n_s)+len(test_s)))
    return accuracy, fault

def k_means(data):
    random.shuffle(data)
    mean_1 = data[0]
    mean_2 = data[1]
    class_1 = []
    class_2 = []
    temp_list = []
    count = 0
    while 1:
        count+=1
        class_1 = []
        class_2 = []
        for i in data:
            distance_1 = (mean_1[0] - i[0])**2 + (mean_1[1] - i[1])**2
            distance_2 = (mean_2[0] - i[0])**2 + (mean_2[1] - i[1])**2
            if distance_1 < distance_2:
                class_1.append(i)
            else:
                class_2.append(i)
        if class_1 == temp_list:
            break
        else:
            temp_list = class_1

            mean_1 = [np.mean([x[0] for x in class_1]), np.mean([x[1] for x in class_1])]
            mean_2 = [np.mean([x[0] for x in class_2]), np.mean([x[1] for x in class_2])]
    
    return class_1, class_2
        
def main():
    n_stress_li, stress_li = read_data()
    plot_data(n_stress_li, stress_li)

    data = n_stress_li + stress_li

    class_1, class_2 = k_means(data)
    plot_data(class_1, class_2)
    # acc, fault = accuracy(class_1, class_2, n_stress_li, stress_li)
    # print(acc)

main()