## Statistical Analysis
To perform a statistical analysis, two different implementations of robot controllers are compared to detect which one performs better in the circuit given, when silver tokens are randomly placed int the environment. To do so, the environment can be divided into 8 zones and silver tokens position is chosen using uniform distribution between the min-max cordinates of these zones.

The program runs with:
```bashscript
$ python run.py my_solution.py
```
```bashscript
$ python run.py given_solution.py
```
## Simulation Results
The outcomes for 20 iterations of simulations with different positions of silver tokens for both implementations is shown in the following table:
| given solution | my solution |
| -------------- | ----------- |
| 189.78 | wrong way |
| 177.71 | 220.71 |
| 189.32 | wrong way |
| 173.98 | 206.03 |
| wrong way | 267.66 |
| 184.31 | wrong way |
| 186.9 | wrong way |
| collision | crash |
| wrong way | wrong way |
| 193.44 | 213.25 |
| 192.86 | wrong way |
| 175.13 | wrong way |
| 182.85 | crash |
| 180.65 | 201.87 |
| 182.34 | 205.14 |
| 176.86 | crash |
| wrong way | crash |
| wrong way | wrong way |
| 190.82 | wrong way |
| wrong way | 214.97 |
