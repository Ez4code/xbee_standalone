import codecs
import numpy as np
from digi.xbee.devices import XBeeDevice
from digi.xbee.models.message import XBeeMessage
#msg = XBeeMessage(rx_data ="None",rx_remote_node= None,rx_timestamp=None)
msg = None
device = XBeeDevice("/dev/ttyUSB0",9600)
device.open()
device.send_data_broadcast("hello life")
while 1:
    msg = device.read_data()
    if msg:
        rx_bytearray = msg.data
        rx_message = codecs.decode(rx_bytearray)
        print (rx_message)
        print(type(rx_message))

#device.close()
