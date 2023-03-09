from itertools import cycle

def encode(message, key):
    code_vec = "_abcdefghijklmnopqrstuvwxyz"
    key_cycle = cycle(list(map(int, list(str(key)))))
    #for i in message:
        
