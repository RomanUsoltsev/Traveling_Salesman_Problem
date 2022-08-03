import random
import math as mt
import numpy as np
import matplotlib.pyplot as plt


# нарисовать маршрут
def route_image(list_cities, route):
    # пронумеруем города
    for i in range(list_cities.shape[0]):
        plt.annotate(i, (list_cities[i][0], list_cities[i][1]), fontsize=14)
    # нарисуем города
    plt.scatter(list_cities[:, 0], list_cities[:, 1], c='red')
    # нарисуем маршрут
    x = [list_cities[route[-1]][0]]
    y = [list_cities[route[-1]][1]]
    for i in range(len(route)):
        x.append(list_cities[route[i]][0])
        y.append(list_cities[route[i]][1])
    plt.plot(x, y, c='blue')
    # выведем изображение
    plt.show()


# if (xy == 0):
#     print("x1: |", list_cities[route[j]][xy], "| x2: |", list_cities[route[j + 1]][xy], "|")
# else:
#     print("y1: |", list_cities[route[j]][xy], "| y2: |", list_cities[route[j + 1]][xy], "|\n")


def route_length(list_cities, route):
    length_penalty = 0
    length = 0
    for i in range(len(list_cities) - 1):
        if i not in route:
            length_penalty += 10
    for j in range(route.size - 1):
        sum = 0
        for xy in range(2):
            sum += (list_cities[route[j]][xy] - list_cities[route[j + 1]][xy]) ** 2
        length += sum ** (1 / 2)

    sum = 0
    for xy in range(2):
        sum += (list_cities[route[0]][xy] - list_cities[route[-1]][xy]) ** 2
    length += sum ** (1 / 2)
    # print("penal = |", length_penalty, "|\n len = |", length, "|\n")
    return length + length_penalty


# качество особей (маршрутов)
def quality(list_cities, routes):
    # проведем оценку маршрутов
    length_penalty = np.zeros([len(routes)])
    for i in range(len(routes)):
        length_penalty[i] = route_length(list_cities, routes[i])

    return length_penalty


def generate_routes(number_cities, number_routes):
    list_cities = np.random.random([number_cities, 2])  # координаты городов
    routes = []
    for i in range(number_routes):
        routes.append(np.random.permutation(number_cities))
    routes = np.array(routes)
    return routes, list_cities


# мутация маршрута
def mutation(list_cities, routes, count_permit, count_routes, detla, max_iteration):
    len_qu = quality(list_cities, routes)
    short = len_qu.min()
    if count_routes != len(routes):
        new_routes, arr_len = selection_routes(list_cities, routes, count_routes)
    else:
        new_routes, arr_len =  sort_routes(list_cities, routes)

    new_arr_len = np.zeros(len(arr_len))

    for i in range(len(new_routes) - 1):
        new_route = permit_routes(routes[i], count_permit)
        new_arr_len[i] = route_length(list_cities, new_route)
        count = 0
        while arr_len[i] - detla < new_arr_len[i] and count < max_iteration:
            new_route = permit_routes(routes[i], count_permit)
            new_arr_len[i] = route_length(list_cities, new_route)
            count += 1

        # if count >= max_iteration:
        #     print("number of iterations exceeded")
        routes[i] = new_route

    routes, sort_arr = selection_routes(list_cities, routes, count_routes)

    return routes, sort_arr

def permit_routes(route, count_permit):
    for i in range(count_permit):
        num_city_1 = random.randint(0, len(route) - 1)
        num_city_2 = random.randint(0, len(route) - 1)
        while num_city_1 == num_city_2:
            num_city_2 = random.randint(0, len(route) - 1)
        index_1 = np.where(route == num_city_1)
        index_2 = np.where(route == num_city_2)

        route[index_1] = num_city_2
        route[index_2] = num_city_1

    return route


def clear_routes_with_penalty(list_cities, routes):
    new_routes = []
    for j in range(len(routes) - 1):
        i = 0
        flag = True
        while i > len(list_cities) - 1 and flag:
            if i not in routes[j]:
                flag = False
            i += 1
        if flag:
            new_routes.append(routes[j])

    new_routes = np.array(new_routes)
    return new_routes


def index_permit(count_permit, count_cities):
    arr_index = np.zeros(count_permit, dtype=int)
    for i in range(count_permit):
        arr_index[i] = -1
    i = 0
    while i < count_permit:
        index = random.randint(0, count_cities)
        if index not in arr_index:
            arr_index[i] = index
            i += 1
    return arr_index


def sort_routes(list_cities, routes):
    unsort_dict = {}
    arr_len = np.zeros(len(routes))
    for i in range(len(routes)):
        arr_len[i] = route_length(list_cities, routes[i])
        a = {arr_len[i]: routes[i]}
        unsort_dict.update(a)

    sort_arr = np.sort(arr_len)
    sorted_dict = {k: unsort_dict[k] for k in sorted(unsort_dict)}

    return sorted_dict, sort_arr


def selection_routes(list_cities, routes, count_routes):
    sorted_dict, arr_len = sort_routes(list_cities, routes)
    new_routes = np.zeros((count_routes, len(list_cities)), dtype= int)
    for i in range(count_routes):
        new_routes[i] = sorted_dict.get(arr_len[i])
    return new_routes, arr_len