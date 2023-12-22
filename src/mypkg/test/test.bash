#!/bin/bash

dir = ~
["$1" != ""] && dir ="$1"

cd $dir/
colcon build

source $dir/.bashrc

