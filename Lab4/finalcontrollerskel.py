# Final Skeleton
#
# Hints/Reminders from Lab 3:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
# print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
#
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the
# switch should send the packets out:
#
# message = of.ofp_flow_mod()
# message.match = of.ofp_match.from_packet(packet)
# message.idle_timeout = 30
# message.hard_timeout = 30
#
# message.actions.append(of.ofp_action_output(port = <PORT>))
# message.data = packet_in
# self.connection.send(message)
#
# To drop packets, simply omit the action.
#
from pox.core import core
import pox.openflow.libopenflow_01 as of
log = core.getLogger()
class Final (object):
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
def do_final (self, packet, packet_in, port_on_switch, switch_id):
# This is where you'll put your code. The following modifications have
# been made from Lab 3:
# - port_on_switch: represents the port that the packet was received on.
# - switch_id represents the id of the switch that received the packet.
# (for example, s1 would have switch_id == 1, s2 would have switch_id ==
2, etc...)
# You should use these to determine where a packet came from. To figure out
where a packet
# is going, you can use the IP header information.
floor_one = ['10.1.1.10', '10.1.2.20', '10.1.3.30', '10.1.4.40']
floor_one_s1 = ['10.1.1.10', '10.1.2.20']
floor_one_s2 = ['10.1.3.30', '10.1.4.40']
floor_two = ['10.2.5.50', '10.2.6.60', '10.2.7.70', '10.2.8.80']
floor_two_s1 = ['10.2.5.50', '10.2.6.60']
floor_two_s2 = ['10.2.7.70', '10.2.8.80']
server = ['10.3.9.90']
trusted = ['108.24.31.112']
untrusted = ['106.44.82.103']
ipv4addr = packet.find('ipv4')
icmpaddr = packet.find('icmp')
arpaddr = packet.find('arp')
if arpaddr is not None:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
message.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
self.connection.send(message)
if ipv4addr is not None:
if switch_id == 3:
if ipv4addr.dstip == "10.1.1.10":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 1))
message.data = packet_in
self.connection.send(message)
elif ipv4addr.dstip == "10.1.2.20":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 2))
message.data = packet_in
self.connection.send(message)
else:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 10))
message.data = packet_in
self.connection.send(message)
if switch_id == 4:
if ipv4addr.dstip == "10.1.3.30":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 3))
message.data = packet_in
self.connection.send(message)
elif ipv4addr.dstip == "10.1.4.40":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 4))
message.data = packet_in
self.connection.send(message)
else:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 11))
message.data = packet_in
self.connection.send(message)
if switch_id == 5:
if ipv4addr.dstip == "10.2.5.50":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 5))
message.data = packet_in
self.connection.send(message)
elif ipv4addr.dstip == "10.2.6.60":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 6))
message.data = packet_in
self.connection.send(message)
else:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 12))
message.data = packet_in
self.connection.send(message)
if switch_id == 6:
if ipv4addr.dstip == "10.2.7.70":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 7))
message.data = packet_in
self.connection.send(message)
elif ipv4addr.dstip == "10.2.8.80":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 8))
message.data = packet_in
self.connection.send(message)
else:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 13))
message.data = packet_in
self.connection.send(message)
if switch_id == 1:
if ipv4addr.dstip == "10.3.9.90":
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 9))
message.data = packet_in
self.connection.send(message)
else:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 14))
message.data = packet_in
self.connection.send(message)
if switch_id == 2:
if packet.find('icmp'):
if ipv4addr.srcip in untrusted and (ipv4addr.dstip in floor_one or
ipv4addr.dstip in floor_two or ipv4addr.dstip in server):
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if packet.find('ipv4'):
if ipv4addr.srcip in untrusted and ipv4addr.dstip in server:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if packet.find('icmp'):
if ipv4addr.srcip in trusted and (ipv4addr.dstip in floor_two or
ipv4addr.dstip in server):
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if packet.find('ipv4'):
if ipv4addr.srcip in trusted and ipv4addr.dstip in server:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if packet.find('icmp'):
if ipv4addr.srcip in floor_one and ipv4addr.dstip in floor_two:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if ipv4addr.srcip in floor_two and ipv4addr.dstip in floor_one:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.buffer_id = packet_in.buffer_id
self.connection.send(message)
return
if ipv4addr.dstip in trusted:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 6))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in untrusted:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 7))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in floor_one_s1:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 1))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in floor_one_s2:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 2))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in floor_two_s1:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 3))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in floor_two_s2:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 4))
message.data = packet_in
self.connection.send(message)
return
if ipv4addr.dstip in server:
message = of.ofp_flow_mod()
message.match = of.ofp_match.from_packet(packet)
message.idle_timeout = 30
message.hard_timeout = 30
message.actions.append(of.ofp_action_output(port = 5))
message.data = packet_in
self.connection.send(message)
return
def _handle_PacketIn (self, event):
"""
Handles packet in messages from the switch.
"""
packet = event.parsed # This is the parsed packet data.
if not packet.parsed:
log.warning("Ignoring incomplete packet")
return
packet_in = event.ofp # The actual ofp_packet_in message.
self.do_final(packet, packet_in, event.port, event.dpid)
def launch ():
"""
Starts the component
"""
def start_switch (event):
log.debug("Controlling %s" % (event.connection,))
Final(event.connection)
core.openflow.addListenerByName("ConnectionUp", start_switch)