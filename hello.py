from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time

# Smooth head nod motion
with ReachyMini() as mini:

    # Neutral position
    mini.goto_target(
        head=create_head_pose(),
        duration=1.0
    )

    time.sleep(0.2)

    # Nod downward smoothly
    mini.goto_target(
        head=create_head_pose(pitch=18, degrees=True),
        duration=0.45
    )

    # Return smoothly to neutral
    mini.goto_target(
        head=create_head_pose(pitch=0, degrees=True),
        duration=0.55
    )

    mini.goto_target(
        head=create_head_pose(z=15, mm=True),
        duration=1.0
    )

    time.sleep(1)


