import can

can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan_native', canfilters={"can_id": 0x2c1, "can_mask": 0xff, "extended": False})

#The message pool 
message_pool = set()
for message in bus:
    tmp_list = list(message.data)
    data_str = ' '.join(format(x,'x').capitalize() for x in tmp_list)
    if message.arbitration_id == 0x2c1:
        continue
    data_str = format(message.arbitration_id, 'x').capitalize() + "#" + data_str 
    if data_str not in message_pool:
        message_pool.add(data_str)
        print( data_str )