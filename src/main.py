import fun


def main():
    number_cities, number_routes = 15, 100
    routes, list_cities = fun.generate_routes(number_cities, number_routes)
    count_permit = 1
    count_routes = int(number_routes / 4)
    delta = 0.2
    max_iter = 100
    count_insert = 5

    len_qu = fun.quality(list_cities, routes)
    min = len_qu.min()
    index = list(len_qu).index(min)
    print("Route to mutation:   ", routes[index], " len :", min)
    fun.route_image(list_cities, routes[index])

    mut_routes, arr_len = fun.mutation(list_cities, routes, count_permit, count_routes, delta, max_iter)

    for i in range(1):
        print("Route to crossbreeding:", mut_routes[i], " len :", arr_len[i])
        fun.route_image(list_cities, mut_routes[i])

    cros_route, cros_len = fun.crossbreeding(list_cities, mut_routes, count_routes, count_insert, delta, max_iter)

    for i in range(1):
        print("Route after crossbreeding:", cros_route[i], " len :", cros_len[i])
        fun.route_image(list_cities, cros_route[i])

    print("Ok")


if __name__ == '__main__':
    main()
