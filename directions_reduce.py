def dirReduc(arr):
    while True:
        curr_length = len(arr)
        for i in range(1, len(arr)):
            if arr[i] == "NORTH" and arr[i-1] == "SOUTH":
                del arr[i]
                del arr[i-1]
                break
            elif arr[i] == "SOUTH" and arr[i-1] == "NORTH":
                del arr[i]
                del arr[i-1]
                break
            elif arr[i] == "EAST" and arr[i-1] == "WEST":
                del arr[i]
                del arr[i-1]
                break
            elif arr[i] == "WEST" and arr[i-1] == "EAST":
                del arr[i]
                del arr[i-1]
                break
            else:
                next
            
        if curr_length == len(arr):
            break
    return arr


print(reduce_directions(["East", "West", "North", "North", "South"]))

print(reduce_directions(["East", "North", "West", "South"]))
