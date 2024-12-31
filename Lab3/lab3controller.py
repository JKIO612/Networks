

Page
1
of 2
# Lab 3 Skeleton
#
# Based on of_tutorial by James McCauley
from pox.core import core
import pox.openflow.libopenflow_01 as of
log = core.getLogger()
class Firewall (object):
"""
A Firewall object is created for each switch that connects.
A Connection object for that switch is passed to the __init__ function.
"""
def __init__ (self, connection):
# Keep track of the connection to the switch so that we can
# send it messages!
self.connection = connection
# This binds our PacketIn event listener
connection.addListeners(self)
def do_firewall (self, packet, packet_in):
# The code in here will be executed for every packet.
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
#set the timeouts
message.idle_timeout = 15
message.hard_timeout = 30
#finding each type of address
#IPV4addr = packet.find('ipv4')
TCPaddr = packet.find('tcp')
ARPaddr = packet.find('arp')
if ARPaddr is not None:
message.match.dl_type = 0x0806
message.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
self.connection.send(message)
elif TCPaddr is not None:
message.match.dl_type = 0x0800
message.match.nw_proto = 6
message.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
self.connection.send(message)
else:
message.match.dl_type = 0x0800
message.priority = 1
self.connection.send(message)
def _handle_PacketIn (self, event):
"""
Handles packet in messages from the switch.
"""
packet = event.parsed # This is the parsed packet data.
if not packet.parsed:
log.warning("Ignoring incomplete packet")
return
packet_in = event.ofp # The actual ofp_packet_in message.
self.do_firewall(packet, packet_in)
def launch ():
"""
Starts the component
"""
def start_switch (event):
log.debug("Controlling %s" % (event.connection,))
Firewall(event.connection)
core.openflow.addListenerByName("ConnectionUp", start_switch)
