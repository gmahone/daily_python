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

# other solutions

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr 

def dirReduc(arr):
    i = 1
    while i < len(arr) and len(arr) > 1:
        if sorted([arr[i], arr[i-1]]) in [["NORTH", "SOUTH"], ["EAST", "WEST"]]:
            del arr[i-1:i+1]
            i = 1
        else:
            i += 1
    return arr

opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

def dirReduc(arr):
    print(arr)
    i = 0
    while i < len(arr)-1:
        current = arr[i]
        next = arr[i+1]
        if next == opposite[current]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return arr
