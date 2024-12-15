# THIS IS FOR TESTING FUNCTIONS !
from enum import Enum
import math

def ease_in_expo_deq_hard(acc: float, star: float):
    exponent = 100 - 12 * star
    if exponent < 5:
        exponent = 5
    return 0 if acc == 0 else math.pow(2, exponent * acc - exponent)

def calculate_rp(acc: float, star: float):
    return round(
        math.pow(
            (star * ease_in_expo_deq_hard(acc, star) * 100) / 2, 2
            ) / 1000, 2
        )

class Speed(Enum):
    SpeedMinusMinusMinus = 1 / 1.35
    SpeedMinusMinus = 1 / 1.25
    SpeedMinus = 1 / 1.15
    Normal = 1
    SpeedPlus = 1.15
    SpeedPlusPlus = 1.25
    SpeedPlusPlusPlus = 1.35
    SpeedPlusPlusPlusPlus = 1.45

# azer's happy new bpm top play
speed: Speed = Speed.SpeedPlusPlusPlusPlus
accuracy = 95.09
star = 9.79

print(calculate_rp(accuracy / 100, star * speed.value))

# prints 358.46