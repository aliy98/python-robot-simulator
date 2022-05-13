# Python Robotics Simulator
This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org/).

## Usage
The simulator requires a Python 2.7 installation, the [pygame](https://www.pygame.org/news) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.org/project/PyYAML/).

The program runs with:
```bashscript
$ python run.py assignment1.py
```
## Description
The robot will have the following behaviour
- constrantly drive the robot around the circuit in the counter-clockwise direction
- avoid touching the golden boxes
- when the robot is close to a silver box, it should grab it, and move it behind itself

The simulation envoirenment would look like this:

![Screenshot from 2021-10-24 11-41-30](https://user-images.githubusercontent.com/65722399/138586065-cbafe397-1772-4220-9853-2e29491dee4b.png)
