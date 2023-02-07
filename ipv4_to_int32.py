def ip_to_int32(ip):
  split_ip = ip.split(".")
  bin_ip = [bin(int(i)).replace("0b", "") for i in split_ip]
  total_bin = "".join([i.zfill(8) for i in bin_ip]))
  pass
