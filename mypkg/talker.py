1 import rclpy                     #ROS 2のクライアントのためのライブラリ
2 from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
3 from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）
4
5 rclpy.init()
6 node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
7 pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
8 n = 0 #カウント用変数
9
10 def cb():          #17行目で定期実行されるコールバック関数
11     global n       #関数を抜けてもnがリセットされないようにしている
12     msg = Int16()  #メッセージの「オブジェクト」
13     msg.data = n   #msgオブジェクトの持つdataにnを結び付け
14     pub.publish(msg)        #pubの持つpublishでメッセージ送信
15     n += 1
16
17 node.create_timer(0.5, cb)  #タイマー設定
18 rclpy.spin(node)            #実行（無限ループ）

