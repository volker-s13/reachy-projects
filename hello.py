from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time

#while True:
#        taste = input("Press w: ")
#        if taste == "w":
#            break

with ReachyMini() as mini:  
 
    mini.goto_target(head=create_head_pose(), duration=0.5) # Neutral position  
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(z=15, mm=True), duration=0.5) # Move head forward
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(pitch=18, degrees=True), duration=0.5) # Nod downward smoothly
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(), duration=0.5) # Neutral position  
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(z=15, mm=True), duration=0.5) # Move head forward
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(), duration=0.5) # Neutral position 
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(roll=20, degrees=True), duration=0.55) # Tilt head to the right
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(), duration=0.5) # Neutral position 
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(roll=-20, degrees=True), duration=0.55) # Tilt head to the left
    time.sleep(0.5)

    mini.goto_target(head=create_head_pose(), duration=0.5) # Neutral position 
    time.sleep(0.5)

    print("Wiggling antennas...")
    mini.goto_target(antennas=[0.5, -0.5], duration=0.5)
    mini.goto_target(antennas=[-0.5, 0.5], duration=0.5)
    mini.goto_target(antennas=[0, 0], duration=0.5)

    
    time.sleep(1)  # Wait for the sound to finish playing   



    


