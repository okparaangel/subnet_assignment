# ip = '10.23.23.20'
# sub = 13
# giving the above i.p, divide into 13 subnet
def server(ip, sub):
    ips = ip.split('.')
    last_index = int(ips[3])
    subnet = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    host = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    submask = ['/24', '/25', '/26', '/27', '/28', '/29', '/30', '/31', '/32']
    
    index = 0
    for i in subnet:
        if sub < i:
            break
        index = index + 1

    _subnet = subnet[index]
    _host = host[index]
    _submask = submask[index]

    network_id_arr = []
    submask_arr = []

    for i in range(_subnet):
        ips[3] = str(last_index)
        ip_value = '.'.join(ips)
        
        network_id_arr.append(ip_value)
        submask_arr.append(_submask)
        
        last_index = last_index + _host

    idx = 0
    print(f"Network ID \t\t Subnet Mask \t\t Host Range \t\t Valuable Host \t Broadcast Id")
     
    for i in network_id_arr:
        idx_2 = idx + 1
        if idx_2 >= len(network_id_arr):
            idx_2 = idx
        
        host_range_1 = '.'.join(network_id_arr[idx].split('.')[:-1]) + '.' + str(int(network_id_arr[idx].split('.')[-1]) + 1)
        host_range_2 = '.'.join(network_id_arr[idx_2].split('.')[:-1]) + '.' + str(int(network_id_arr[idx_2].split('.')[-1]) - 2)
        host_range = f"{host_range_1} - {host_range_2}"
        broadcast = '.'.join(host_range_2.split('.')[:-1]) + '.' + str(int(host_range_2.split('.')[-1]) + 1)
        valuable_host = _host - 2
        
        print(f"{network_id_arr[idx]} \t\t {_submask} \t\t {host_range} \t  {valuable_host} \t\t {broadcast}")
        idx = idx + 1

ip = '10.23.23.20'
sub = 13
server(ip, sub)

