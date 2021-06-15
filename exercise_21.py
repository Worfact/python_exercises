import sys
import re
import math

robot_directions = sys.stdin.readlines()
robot_position = [0, 0]
x = 0

for str in robot_directions:
    
    robot_directions[x] = str.replace('\n', '')
    x += 1
    direction_value_list = re.findall(r'\d', str)
    direction_value = int(''.join(direction_value_list))
    
    if str.find('UP') == 0:
        robot_position[1] += direction_value 
    elif str.find('DOWN') == 0:
        robot_position[1] -= direction_value
    elif str.find('LEFT') == 0:
        robot_position[0] -= direction_value
    elif str.find('RIGHT') == 0:
        robot_position[0] += direction_value
    
distance = math.sqrt((robot_position[0]**2) + (robot_position[1]**2))
distance = round(distance)
    
print('The robot run through', distance, 'units.')
