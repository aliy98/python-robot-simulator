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

## Pseudocode
```
***
  function for finding silver tokens:
  
  	for all the tokens which robot detects
  		if it is silver and also near the robot
  			detect the distance and angle from it 
  			
	  	if the detected angle is between -90 and 90
	  		set the token value to true
	  	else
	  	        set the token value to False
	  	        	  	        	
  return if there is any silver token and also the distance and angle from it
  	     
***
  function for finding golden tokens:
  
       for all the tokens which robot detects
  		if it is golden and also near the robot
  			detect the distance and angle from them
  			
       for any angle which is detected 
	  	if angle is between -45 and 45
	  		assign their distances to the front side obstacles 
	  	else if it is between 45 and 135
	  	        assign their distances to the right side obstacles 	
	  	else if it is between -135 and -45       
	  	        assign their distances to the left side obstacles
	  	        
       for any distance in the front side 
                if it is lower than 0.8
                	set the obstacle value to true
       
       if there is no golden token in the left side 
       		return 100m distance
       if there is no golden token in the right side
       		return 100m distance	       
	  	       	        	
    return if there is any obstacle in the front side and also the number of obstacles in the right and left sides 
    and also return the distace from obstacles which are located in the -45 and 45 angles 
  
  ***
    main loop
    
    	get the returned values from functions
    	
    	if there is a golden token but no silver token near the robot 
    		if the number of golden tokens in the right side are more than the left side 
    			move the robot to left
    		else if the number of golden tokens in the left side are more than the right side 
    			move the robot to right
    		else if the number of golden tokens in both sides are equal
    			memorize the distance from front_right side golden token (-45degree)
    			memorize the distance from front_left side golden token  (45degree)
    		while there is an obstacle in front of robot
    			get the returned values from functions
    			move the robot regarding the memorized values 
    	else
    		if there is no silver and golden token near the robot
    			move the robot forward
    		else
    			if the robot is well aligned with the token
    				move the robot forward
    			if the robot is not well aligned with the token 
    				we move it on the left or on the right
    			if we are close to the token 
    				we grab it
```
