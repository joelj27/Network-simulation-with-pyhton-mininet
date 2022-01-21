from mininet.net import Mininet
# from mininet.util import createLink
from mininet.node import CPULimitedHost,OVSKernelSwitch,Controller, RemoteController
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
import paho.mqtt.client as mqtt
import time

import subprocess
net = Mininet(switch=OVSKernelSwitch)


# creating a controller
c0 = net.addController('c0',controller=RemoteController)
print"CREATING THE Controller**********************"
time.sleep(3)
print"c0 Controller Created"
time.sleep(1)

#creatring CLIENT
client1 = net.addHost('client1')
client2 = net.addHost('client2')
client3 = net.addHost('client3')
client4 = net.addHost('client4')
client5 = net.addHost('client5')
client6 = net.addHost('client6')
client7 = net.addHost('client7')
client8 = net.addHost('client8')
client9 = net.addHost('client9')
client10= net.addHost('client10')
client11= net.addHost('client11')
client12= net.addHost('client12')
client13= net.addHost('client13')
client14= net.addHost('client14')
client15= net.addHost('client15')
client16= net.addHost('client16')
client17= net.addHost('client17')
client18= net.addHost('client18')
client19= net.addHost('client19')
client20= net.addHost('client20')
client21= net.addHost('client21')
client22= net.addHost('client22')
client23= net.addHost('client23')
client24= net.addHost('client24')
client25= net.addHost('client25')
client26= net.addHost('client26')
client27= net.addHost('client27')
client28= net.addHost('client28')
client29= net.addHost('client29')
client30= net.addHost('client30')
client31= net.addHost('client31')
client32= net.addHost('client32')
client33= net.addHost('client33')
client34= net.addHost('client34')
client35= net.addHost('client35')
client36= net.addHost('client36')
client37= net.addHost('client37')
client38= net.addHost('client38')
client39= net.addHost('client39')
client40= net.addHost('client40')



print"CREATING THE CLIENT**********************"
time.sleep(3)
print"client 1  Created"
print"client 2  Created"
print"client 3  Created"
print"client 4  Created"
print"client 5  Created"
print"client 6  Created"
print"client 7  Created"
print"client 8  Created"
print"client 9  Created"
print"client 10 Created"
print"client 11 Created"
print"client 12 Created"
print"client 13 Created"
print"client 14 Created"
print"client 15 Created"
print"client 16 Created"
print"client 17 Created"
print"client 18 Created"
print"client 19 Created"
print"client 20 Created"
print"client 21 Created"
print"client 22 Created"
print"client 23 Created"
print"client 24 Created"
print"client 25 Created"
print"client 26 Created"
print"client 27 Created"
print"client 28 Created"
print"client 29 Created"
print"client 30 Created"
print"client 31 Created"
print"client 32 Created"
print"client 33 Created"
print"client 34 Created"
print"client 35 Created"
print"client 36 Created"
print"client 37 Created"
print"client 38 Created"
print"client 39 Created"
print"client 40 Created"
time.sleep(1)

#creating SWITCHES
switch1 = net.addSwitch('switch1',inNamespace=False)
switch2 = net.addSwitch('switch2',inNamespace=False)
switch3 = net.addSwitch('switch3',inNamespace=False)
switch4 = net.addSwitch('switch4',inNamespace=False)
switch5 = net.addSwitch('switch5',inNamespace=False)
switch6 = net.addSwitch('switch6',inNamespace=False)
switch7 = net.addSwitch('switch7',inNamespace=False)
switch8 = net.addSwitch('switch8',inNamespace=False)
switch9 = net.addSwitch('switch9',inNamespace=False)
switch10 = net.addSwitch('switch10',inNamespace=False)
switch11 = net.addSwitch('switch11',inNamespace=False)
switch12 = net.addSwitch('switch12',inNamespace=False)
switch13 = net.addSwitch('switch13',inNamespace=False)
switch14 = net.addSwitch('switch14',inNamespace=False)
switch15 = net.addSwitch('switch15',inNamespace=False)
switch16 = net.addSwitch('switch16',inNamespace=False)
switch17 = net.addSwitch('switch17',inNamespace=False)
switch18 = net.addSwitch('switch18',inNamespace=False)
switch19 = net.addSwitch('switch19',inNamespace=False)
switch20 = net.addSwitch('switch20',inNamespace=False)


print"CREATING THE SWITCHES**********************"
time.sleep(3)
print"switch 1  Created"
print"switch 2  Created"
print"switch 3  Created"
print"switch 4  Created"
print"switch 5  Created"
print"switch 6  Created"
print"switch 7  Created"
print"switch 8  Created"
print"switch 9  Created"
print"switch 10 Created"
print"switch 11 Created"
print"switch 12 Created"
print"switch 13 Created"
print"switch 14 Created"
print"switch 15 Created"
print"switch 16 Created"
print"switch 17 Created"
print"switch 18 Created"
print"switch 19 Created"
print"switch 20 Created"
time.sleep(1)


#creating BROKER
broker1='broker.emqx.io'
port=80
broker1 = net.addHost('broker1',bw=10)
broker2='broker.emqx.io'
port=80
broker2 = net.addHost('broker2',bw=10)
broker3='broker.emqx.io'
port=80
broker3 = net.addHost('broker3',bw=10)
broker4='broker.emqx.io'
port=80
broker4 = net.addHost('broker4',bw=10)
broker5='broker.emqx.io'
port=80
broker5 = net.addHost('broker5',bw=10)
broker6='broker.emqx.io'
port=80
broker6 = net.addHost('broker6',bw=10)
broker7='broker.emqx.io'
port=80
broker7 = net.addHost('broker7',bw=10)
broker8='broker.emqx.io'
port=80
broker8 = net.addHost('broker8',bw=10)
broker9='broker.emqx.io'
port=80
broker9 = net.addHost('broker9',bw=10)
broker10='broker.emqx.io'
port=80
broker10 = net.addHost('broker10',bw=10)

print"CREATING THE BROKER**********************"
time.sleep(3)
print"broker 1  Created"
print"broker 2  Created"
print"broker 3  Created"
print"broker 4  Created"
print"broker 5  Created"
print"broker 6  Created"
print"broker 7  Created"
print"broker 8  Created"
print"broker 9  Created"
print"broker 10  Created"
time.sleep(1)

#creating server
server1 = net.addSwitch('server1',inNamespace=False)
server2 = net.addSwitch('server2',inNamespace=False)
server3 = net.addSwitch('server3',inNamespace=False)
server4 = net.addSwitch('server4',inNamespace=False)
server5 = net.addSwitch('server5',inNamespace=False)
server6 = net.addSwitch('server6',inNamespace=False)
server7 = net.addSwitch('server7',inNamespace=False)
server8 = net.addSwitch('server8',inNamespace=False)
server9 = net.addSwitch('server9',inNamespace=False)
server10 = net.addSwitch('server10',inNamespace=False)

print"CREATING THE SERVER**********************"
time.sleep(3)
print" server 1 Created"
print" server 2 Created"
print" server 3 Created"
print" server 4 Created"
print" server 5 Created"
print" server 6 Created"
print" server 7 Created"
print" server 8 Created"
print" server 9 Created"
print" server 10 Created"

# Creating links between  in network
switch1.linkTo(client1)
switch1.linkTo(client2)

switch2.linkTo(client3)
switch2.linkTo(client4)

switch3.linkTo(client5)
switch3.linkTo(client6)

switch4.linkTo(client7)
switch4.linkTo(client8)

switch5.linkTo(client9)
switch5.linkTo(client10)

switch6.linkTo(client11)
switch6.linkTo(client12)

switch7.linkTo(client13)
switch7.linkTo(client14)

switch8.linkTo(client15)
switch8.linkTo(client16)

switch9.linkTo(client17)
switch9.linkTo(client18)

switch10.linkTo(client19)
switch10.linkTo(client20)

switch11.linkTo(client21)
switch11.linkTo(client22)

switch12.linkTo(client23)
switch12.linkTo(client24)

switch13.linkTo(client25)
switch13.linkTo(client26)

switch14.linkTo(client27)
switch14.linkTo(client28)

switch15.linkTo(client29)
switch15.linkTo(client30)

switch16.linkTo(client31)
switch16.linkTo(client32)

switch17.linkTo(client33)
switch17.linkTo(client34)

switch18.linkTo(client35)
switch18.linkTo(client36)

switch19.linkTo(client37)
switch19.linkTo(client38)

switch20.linkTo(client39)
switch20.linkTo(client40)
###############################
switch1.linkTo(broker1)
switch2.linkTo(broker1)

switch3.linkTo(broker2)
switch4.linkTo(broker2)

switch5.linkTo(broker3)
switch6.linkTo(broker3)

switch7.linkTo(broker4)
switch8.linkTo(broker4)

switch9.linkTo(broker5)
switch10.linkTo(broker5)

switch11.linkTo(broker6)
switch12.linkTo(broker6)

switch13.linkTo(broker7)
switch14.linkTo(broker7)

switch15.linkTo(broker8)
switch16.linkTo(broker8)

switch17.linkTo(broker9)
switch18.linkTo(broker9)

switch19.linkTo(broker10)
switch20.linkTo(broker10)
#########################################
broker1.linkTo(server1)
broker2.linkTo(server2)

broker3.linkTo(server3)
broker4.linkTo(server4)

broker5.linkTo(server5)
broker6.linkTo(server6)

broker7.linkTo(server7)
broker8.linkTo(server8)

broker9.linkTo(server9)
broker10.linkTo(server10)
#################################
broker1.linkTo(broker2)
broker2.linkTo(broker3)
broker3.linkTo(broker4)
broker4.linkTo(broker5)
broker5.linkTo(broker6)
broker6.linkTo(broker7)
broker7.linkTo(broker8)
broker8.linkTo(broker9)
broker9.linkTo(broker10)
#################################
switch1.linkTo(switch2)
switch2.linkTo(switch3)
switch3.linkTo(switch4)
switch4.linkTo(switch5)
switch5.linkTo(switch6)
switch6.linkTo(switch7)
switch7.linkTo(switch8)
switch8.linkTo(switch9)
switch9.linkTo(switch10)
switch10.linkTo(switch11)
switch11.linkTo(switch12)
switch12.linkTo(switch13)
switch13.linkTo(switch14)
switch14.linkTo(switch15)
switch15.linkTo(switch16)
switch16.linkTo(switch17)
switch17.linkTo(switch18)
switch18.linkTo(switch19)
switch19.linkTo(switch20)




print"CREATING THE lINK**********************"
time.sleep(3)
print"CONNECTING CLIENT WITH SWITCHES"
#time.sleep(3)
print"client1 linked with switch1"
print"client2 linked with switch1"
print"client3 linked with switch2"
print"client4 linked with switch2"
print"client5 linked with switch3"
print"client6 linked with switch3"
print"client7 linked with switch4"
print"client8 linked with switch4"
print"client9 linked with switch5"
print"client10 linked with switch5"
print"client11 linked with switch6"
print"client12 linked with switch6"
print"client13 linked with switch7"
print"client14 linked with switch7"
print"client15 linked with switch8"
print"client16 linked with switch8"
print"client17 linked with switch9"
print"client18 linked with switch9"
print"client19 linked with switch10"
print"client20 linked with switch10"
print"client21 linked with switch11"
print"client22 linked with switch11"
print"client23 linked with switch12"
print"client24 linked with switch12"
print"client25 linked with switch13"
print"client26 linked with switch13"
print"client27 linked with switch14"
print"client28 linked with switch14"
print"client29 linked with switch15"
print"client30 linked with switch15"
print"client31 linked with switch16"
print"client32 linked with switch16"
print"client33 linked with switch17"
print"client34 linked with switch17"
print"client35 linked with switch18"
print"client36 linked with switch18"
print"client37 linked with switch19"
print"client38 linked with switch19"
print"client39 linked with switch20"
print"client40 linked with switch20"
#time.sleep(1)

print"CONNECTING SWITCHES WITH BROKER"
#time.sleep(3)
print"switch1 linked with broker1"
print"switch2 linked with broker1"
print"switch3 linked with broker2"
print"switch4 linked with broker2"
print"switch5 linked with broker3"
print"switch6 linked with broker3"
print"switch7 linked with broker4"
print"switch8 linked with broker4"
print"switch9 linked with broker5"
print"switch10 linked with broker5"
print"switch11 linked with broker6"
print"switch12 linked with broker6"
print"switch13 linked with broker7"
print"switch14 linked with broker7"
print"switch15 linked with broker8"
print"switch16 linked with broker8"
print"switch17 linked with broker9"
print"switch18 linked with broker9"
print"switch19 linked with broker10"
print"switch20 linked with broker10"
#time.sleep(1)

print"CONNECTING BROKERS WITH SERVER"
#time.sleep(3)
print"broker1 linked with server1"
print"broker2 linked with server2"
print"broker3 linked with server3"
print"broker4 linked with server4"
print"broker5 linked with server5"
print"broker6 linked with server6"
print"broker7 linked with server7"
print"broker8 linked with server8"
print"broker9 linked with server9"
print"broker10 linked with server10"
#time.sleep(1)

net.start()
#connecting SERVER to the controller
c0.start()
server1.start([c0])
server2.start([c0])
server3.start([c0])
server4.start([c0])
server5.start([c0])
server6.start([c0])
server7.start([c0])
server8.start([c0])
server9.start([c0])
server10.start([c0])

print"CONNECTING SERVER WITH CONTROLLER"
time.sleep(3)
print"server1 linked with c0"
print"server2 linked with c0"
print"server3 linked with c0"
print"server4 linked with c0"
print"server5 linked with c0"
print"server6 linked with c0"
print"server7 linked with c0"
print"server8 linked with c0"
print"server9 linked with c0"
print"server10 linked with c0"
time.sleep(1)

print"CHECK THE PING REACHABLITY FOR ALL THE CLIENT*****************"
time.sleep(3)
net.pingAll()
time.sleep(1)

print"TAKING DOWN THE BROKER 1 DOWN**********************"
net.configLinkStatus( 'client1', 'switch1', 'down')
net.configLinkStatus( 'client2', 'switch1', 'down')
net.configLinkStatus( 'client3', 'switch2', 'down')
net.configLinkStatus( 'client4', 'switch2', 'down')
net.configLinkStatus( 'broker1', 'switch1', 'down')
net.configLinkStatus( 'broker1', 'switch2', 'down')
time.sleep(1)
print"BROKER 1 is down"
CLI(net)
time.sleep(3)
net.pingAll()

b2,b3,b4,b5,b6,b7,b8,b9,b10 = net.get('broker2','broker3','broker4','broker5','broker6','broker7','broker8','broker9','broker10' )
print"GETING THE BANDWIDTH OF broker2 broker3 broker4 *****************************"
bb2,ba2=net.iperf( (b2, b3) )
bb3,ba3=net.iperf( (b3, b4) )
bb4,ba4=net.iperf( (b4, b5) )
bb5,ba5=net.iperf( (b5, b6) )
bb6,ba6=net.iperf( (b6, b7) )
bb7,ba7=net.iperf( (b7, b8) )
bb8,ba8=net.iperf( (b8, b9) )
bb9,ba9=net.iperf( (b9, b10) )
bb10,ba10=net.iperf( (b10, b2) )
print"BANDWIDTH OF broker2"
print(bb2)
print"BANDWIDTH OF broker3"
print(bb3)
print"BANDWIDTH OF broker4"
print(bb4)
print"BANDWIDTH OF broker5"
print(bb5)
print"BANDWIDTH OF broker6"
print(bb6)
print"BANDWIDTH OF broker7"
print(bb7)
print"BANDWIDTH OF broker8"
print(bb8)
print"BANDWIDTH OF broker9"
print(bb9)
print"BANDWIDTH OF broker10"
print(bb10)



if bb2<40:
   print"CONNETING client1 client2 client3 client4 THE broker 2*******************"
   time.sleep(3)
   net.addLink(client1,net.get('switch1'))
   net.addLink(client2,net.get('switch1'))
   net.addLink(client3,net.get('switch2'))
   net.addLink(client4,net.get('switch2'))
   net.addLink(broker2,net.get('switch1'))
   net.addLink(broker2,net.get('switch2'))
elif bb3>20:
     print"CONNETING client1 client2 client3 client4 THE broker 3*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker3,net.get('switch1'))
     net.addLink(broker3,net.get('switch2'))
elif bb4>20:
     print"CONNETING client1 client2 client3 client4 THE broker 4*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker4,net.get('switch1'))
     net.addLink(broker4,net.get('switch2'))
elif bb5>20:
     print"CONNETING client1 client2 client3 client4 THE broker 5*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker5,net.get('switch1'))
     net.addLink(broker5,net.get('switch2'))
elif bb6>20:
     print"CONNETING client1 client2 client3 client4 THE broker 6*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker6,net.get('switch1'))
     net.addLink(broker6,net.get('switch2'))
elif bb7>20:
     print"CONNETING client1 client2 client3 client4 THE broker 7*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker7,net.get('switch1'))
     net.addLink(broker7,net.get('switch2'))
elif bb8>20:
     print"CONNETING client1 client2 client3 client4 THE broker 8*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker8,net.get('switch1'))
     net.addLink(broker8,net.get('switch2'))
elif bb9>20:
     print"CONNETING client1 client2 client3 client4 THE broker 9*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker9,net.get('switch1'))
     net.addLink(broker9,net.get('switch2'))
elif bb10>20:
     print"CONNETING client1 client2 client3 client4 THE broker 10*******************"
     time.sleep(3)
     net.addLink(client1,net.get('switch1'))
     net.addLink(client2,net.get('switch1'))
     net.addLink(client3,net.get('switch2'))
     net.addLink(client4,net.get('switch2'))
     net.addLink(broker10,net.get('switch1'))
     net.addLink(broker10,net.get('switch2'))

net.get('client1')
net.get('client2')
net.get('client3')
net.get('client4')
net.get('switch1')
net.get('switch2')

time.sleep(1)
net.configLinkStatus( 'client1', 'switch1', 'up')
net.configLinkStatus( 'client2', 'switch1', 'up')
net.configLinkStatus( 'client3', 'switch2', 'up')
net.configLinkStatus( 'client4', 'switch2', 'up')

CLI(net)
print"CHECK THE PING REACHABLITY FOR ALL THE CLIENT*****************"
time.sleep(3)
net.pingAll()
time.sleep(1)


CLI(net)

net.stop()
