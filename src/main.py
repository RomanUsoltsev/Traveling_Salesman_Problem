import numpy as np
import fun


def test_length_route():
    list_cities = np.array([[0.22545213, 0.47175503],
                            [0.7215346, 0.01659324],
                            [0.29019241, 0.63847256],
                            [0.42587585, 0.11428757]])
    print(list_cities)
    route = np.array(range(4))
    len = fun.route_length(list_cities, route)
    assert (len == 2.3813634047264274)


def base():
    number_cities = 15  # количество городов
    list_cities = np.random.random([number_cities, 2]) # координаты городов
    # route = np.random.randint(number_cities, size=number_cities)  # сгенерированный маршрут
    # print("Маршрут:", route)
    # fun.route_image(list_cities, route)
    # len = fun.route_length(list_cities, route)
    routes = []
    number_routes = 100
    for i in range(number_routes):
        routes.append(np.random.permutation(number_cities))
    routes = np.array(routes)

    len_qu = fun.quality(list_cities, routes)
    min = len_qu.min()
    print(min)
    # index = np.where(len_qu == min)
    index = list(len_qu).index(min)
    print("len_q\n", len_qu)
    print("min = ", min, " i = ", index, "l_q = ", len_qu[index])

    print("Маршрут:", routes[index])
    fun.route_image(list_cities, routes[index])

def base_2():
    number_cities, number_routes = 15, 100
    routes, list_cities = fun.generate_routes(number_cities, number_routes)
    count_permit = 1
    count_routes = int(number_routes / 4)
    delta = 0.5
    max_iter = 100

    len_qu = fun.quality(list_cities, routes)
    min = len_qu.min()
    index = list(len_qu).index(min)
    print("Route to mutation", routes[index], " len :", min)
    fun.route_image(list_cities, routes[index])

    mut_routes, arr_len = fun.mutation(list_cities, routes, count_permit, count_routes, delta, max_iter)

    # print(count_routes, mut_routes, arr_len)
    for i in range(1):
        print("Route after mutation:", mut_routes[i], " len :", arr_len[i])
        fun.route_image(list_cities, mut_routes[i])



if __name__ == '__main__':
    base_2()