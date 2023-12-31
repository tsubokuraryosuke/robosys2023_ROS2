# フィボナッチ数列計算
[![test](https://github.com/tsubokuraryosuke/robosys2023_ROS2/actions/workflows/test.yml/badge.svg)](https://github.com/tsubokuraryosuke/robosys2023_ROS2/actions/workflows/test.yml)

## ノードとそれぞれの持つ意味
* talker
毎秒フィボナッチ数列を計算し続ける

* listener
talkerのノードから送られてきた計算結果を表示する


## 実行方法
```
端末1　$ ros2 run mypkg talker　
端末2  $ ros2 run mypkg listener
```
実行後は以下のようにlistenerが表示する
```
[INFO] [1704022405.445705040] [listener]: Listen: 1
[INFO] [1704022406.440748786] [listener]: Listen: 2
[INFO] [1704022407.440829449] [listener]: Listen: 3
[INFO] [1704022408.440700373] [listener]: Listen: 5
[INFO] [1704022409.440617007] [listener]: Listen: 8
[INFO] [1704022410.440786230] [listener]: Listen: 13
[INFO] [1704022411.440581781] [listener]: Listen: 21
[INFO] [1704022412.440674221] [listener]: Listen: 34
```

## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 20.04
* ROS foxy

## 著作権及びライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
(https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/18)
(https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/18)
(https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/8)
* © 2023　Tsubokura Ryosuke
