def queue_time(customers, n):
    queue_list = [0] * n
    for customer in customers:
        shortest_length = min(queue_list)
        shortest_line = queue_list.index(shortest_length)
        queue_list[shortest_line] += customer
    print(queue_list)
    pass
