from __future__ import print_function
import time
from sr.robot import *
import time

"""
Assignment 1 python script

"""
a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

R = Robot()
""" instance of the class Robot"""


def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the distance and angle for near silver tokens 

    Returns:
	dist (float): distance of the closest silver token
	rot_y (float): angle between the robot and the silver token
    token (bolean): True if there is a silver token near the robot
    """
    silver_token_dist = 100
    silver_token_rot_y = 360
    silver_token_detected = False

    # loop for reading the values from sensor
    for token in R.see():
        if token.dist < 3*d_th and token.info.marker_type is MARKER_TOKEN_SILVER:
            silver_token_dist = round(token.dist,2)  #reading the distance from the near silver token
            silver_token_rot_y = round(token.rot_y,2)  #reading the angle with the near silver token
        
        if silver_token_dist < 2.5*d_th: #detect if there is a silver token near the robot
            if -180 < silver_token_rot_y < -90 or 90 < silver_token_rot_y < 180: # back side is not included
                silver_token_detected = False
            if -90 < silver_token_rot_y < 90: # front side is included
                silver_token_detected = True
        else:
            silver_token_detected = False
    return silver_token_dist, silver_token_rot_y, silver_token_detected
    
def find_golden_token():
    """
    Function to find the number and distance of the near golden tokens 

    Returns:
    left_obs[-1] (float): distance from the golden token which is located in the front left side of the robot (45 degrees)
    right_obs[0]: (float): distance from the golden token which is located in the front right side of the robot (-45 degrees)
	len(left_obs) (int): number of golden tokens in the left side of the robot
	len(right_obs) (int): number of golden tokens in the right side of the robot
    obs (boolean): True if there is a golden token near the robot
    """
    dists = []
    rots_y = []
    front_obs = []
    right_obs = []
    left_obs = []
    obs_detected = False

    # loop for reading the values from sensor
    for token in R.see():
        if token.dist < 3.5*d_th and token.info.marker_type is MARKER_TOKEN_GOLD:
            dists.append(round(token.dist,2)) #reading the distances
            rots_y.append(round(token.rot_y,2)) #reading the angles

    for rot_y in rots_y:
        if -45 < rot_y < 45:
            front_obs.append(dists[rots_y.index(rot_y)]) # assigning the distance from golden tokens which are located in the front side of robot (from -45 to 45 degrees)
        elif 45 < rot_y < 135:        
            right_obs.append(dists[rots_y.index(rot_y)]) # assigning the distance from golden tokens which are located in the right side of robot (from 45 to 135 degrees)
        elif -135 < rot_y < -45:
            left_obs.append(dists[rots_y.index(rot_y)]) # assigning the distance from golden tokens which are located in the left side of robot (from -135 to -45 degrees)
        
    for dist in front_obs: # detect if there is a golden token in front of robot
        if dist < 2*d_th:
            obs_detected = True
    
    if len(left_obs) == 0: # if there is no golden token in the left side return 100m distance
        left_obs = [100] 

    if len(right_obs) == 0: # if there is no golden token in the right side return 100m distance
        right_obs = [100] 
        
    return left_obs[-1], right_obs[0], len(left_obs), len(right_obs), obs_detected

silver_token_counter = 0

# main loop
while 1:
    left_obs_dist, right_obs_dist, left_obs_num, right_obs_num, obs_detected  = find_golden_token()
    silver_token_dist, silver_token_rot_y, silver_token_detected = find_silver_token()

    if obs_detected == True and silver_token_detected == False:  # there is a golden token but no silver token near the robot 
        if right_obs_num > left_obs_num: # if the number of golden tokens in the right side are more than the left side, we move the robot to left
            turn(-10,0.25)
            print("left a bit")
        elif right_obs_num < left_obs_num: # if the number of golden tokens in the left side are more than the right side, we move the robot to right
            turn(10,0.25)
            print("right a bit...")
        elif right_obs_num == left_obs_num: # the number of golden tokens in both sides are equal
            const_right_obs = right_obs_dist # memorizing the distance from front_right side golden token (-45degree)
            const_left_obs = left_obs_dist  # memorizing the distance from front_left side golden token  (45degree)
            while obs_detected == True: # moving the robot regarding the memorized values until there is no golden token in front of robot
                left_obs_dist, right_obs_dist, left_obs_num, right_obs_num, obs_detected  = find_golden_token()
                if const_right_obs < const_left_obs:
                    turn(-10,0.25)
                    print("left a bit")
                else:
                    turn(10,0.25)
                    print("right a bit")

             
    else:
        if silver_token_detected == False: # if there is no silver and golden token near the robot, we move it forward
            drive(60,0.25)
            print("looking for silver token...")
        else: # there is a silver token  but no golden token near the robot
            if -a_th<= silver_token_rot_y <= a_th and silver_token_dist > d_th: # if the robot is well aligned with the token, we go forward
                print("Ah, here we are!.")
                drive(10,0.5)     
            elif silver_token_rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
                print("Left a bit...")
                turn(-2, 0.5)
            elif silver_token_rot_y > a_th:
                print("Right a bit...")
                turn(2, 0.5)
            elif -a_th<= silver_token_rot_y <= a_th and silver_token_dist <d_th: 
                print("Found it!")
                R.grab() # if we are close to the token, we grab it.
                print("Gotcha!") 
                turn(40, 1.5)
                R.release()
                drive(-45,0.5)
                turn(-40,1.5)  
                if silver_token_counter == 0:
                    start = time.time()
                silver_token_counter += 1
                if silver_token_counter == 9:
                    end = time.time()
                    print("loop time: ")
                    print(end - start)
                    exit() 
