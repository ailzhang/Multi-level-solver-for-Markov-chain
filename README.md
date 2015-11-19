# Multi-level-solver-for-Markov-chain
Implement "A multi-level solution algorithm for steady-state markov chains" by Graham Horton etc.
11/18/2015: Yongli Chen

The current GS.py is Gauss-Seidel implementation in python, based on the algorithm given in CS541 module3 ppt(slide 65). I manually debugged the program through several iterations, and it looks fine. However, the problem is that using example from CS 541 module3 ppt slide66, the result doesn't converge. If you double check with algorithm given in slide 65, Pi[i] always increases. We should discuss this more tomorrow.