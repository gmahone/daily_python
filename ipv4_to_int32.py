def ip_to_int32(ip):
  split_ip = ip.split(".")
  print(split_ip)
  print("".join([i.zfill(8) for i in split_ip]))
  pass
