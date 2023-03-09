from itertools import cycle

def encode(message, key):
    key_cycle = cycle(list(map(int, list(str(key)))))
    #for i in message:
        
