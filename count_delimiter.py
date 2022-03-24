def delete_nth(order,max_e):
    unique = []
    for i in range(0, len(order)):
        if order[i] not in unique:
            unique.append(order[i])
    
    for j in range(0, len(unique)):
        loop_end = len(order)
        k = 0
        loop_run = True
        current_count = 0
        while loop_run:
            if unique[j] == order[k] and current_count < max_e:
                current_count += 1
                k += 1
            elif unique[j] == order[k] and not current_count < max_e:
                order.pop(k)
                loop_end -= 1
            else:
                k += 1
            if k == loop_end:
                loop_run = False

    return order
