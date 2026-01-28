# Path planning with differential drive robot

Project to implement basic path planning with knowledge of obstacles in environment using MPC like modeling

~~Project uses a gradient based solver called IPOPT ([wrapper](https://github.com/mechmotum/cyipopt) for the library in python)~~

Project uses casadi for as library that contains the solvers and to define the problem. disregarded previous library due to insufficient ability to define the problem (could not set target state, or "subject to" function)
