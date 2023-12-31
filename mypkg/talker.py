#SPDX-FIleCopyrightTexy: 2023 Tsubokura Ryosuke
#SPDX-Lincense-Indentifier: BSD-3-Clause

import rclpy                     
from rclpy.node import Node      
from std_msgs.msg import Int16   

rclpy.init()
node = Node("talker")            
pub = node.create_publisher(Int16, "countup", 10)   
n = 1 
m = 1

def cb():          
    global n
    global m
    global l
    msg = Int16()  
    msg.data = m   
    pub.publish(msg)
    l = m
    m += n 
    n = l 

node.create_timer(1, cb)
rclpy.spin(node)            

