"""
Stock Car Race Elimination Problem
Problem Statement:
All competitors in a stock car race have completed their qualifying laps. Each lap, the driver with the current slowest "best" time (highest personal best time) is eliminated. If multiple drivers tie for the slowest time, they are all eliminated.

You are given a two-dimensional string array laps, where each subarray represents a lap, and each entry in the subarray is formatted as "DriverName LapTime" (e.g., "Harold 154"). Your task is to return the drivers in the order they were eliminated, ending with the last remaining driver(s). If multiple drivers are eliminated in the same lap, sort their names alphabetically.

Notes:

A driver’s "best time" is their fastest lap time across all completed laps.

Drivers are eliminated after each lap based on their current best time.

Examples
Example 1:
Input:

python
laps = [
    ["Harold 154", "Gina 155", "Juan 160"],
    ["Juan 152", "Gina 153", "Harold 160"],
    ["Harold 148", "Gina 150", "Juan 151"]
]
Output:
["Juan", "Harold", "Gina"]

Explanation:

Lap 1: Best times → Harold (154), Gina (155), Juan (160).
Juan (slowest) is eliminated.

Lap 2: Best times → Harold (154), Gina (153).
Harold (slowest) is eliminated.

Lap 3: Only Gina remains.

Example 2:
Input:

python
laps = [
    ["Gina 155", "Eddie 160", "Joy 161", "Harold 163"],
    ["Harold 151", "Gina 153", "Joy 160", "Eddie 160"],
    ["Harold 149", "Joy 150", "Gina 152", "Eddie 154"],
    ["Harold 148", "Gina 150", "Eddie 151", "Joy 155"]
]
Output:
["Harold", "Eddie", "Joy", "Gina"]

Explanation:

Lap 1: Harold (163) is eliminated.

Lap 2: Eddie and Joy tie (160) → both eliminated alphabetically: Eddie, Joy.

Lap 3: Gina remains.
"""

def stockCarRace(laps):
    drivers = {}

    eliminated_drivers = []

    for lap in laps:
        
        for driver in lap:
            name, time = driver.split()
            drivers[name] = int(time)

        ignore_eliminated_drivers = {key:value for key, value in drivers.items() if not key in eliminated_drivers}

        if ignore_eliminated_drivers:

            slowest_time = max(ignore_eliminated_drivers.values())

            slowest_drivers = sorted([k for k, v in ignore_eliminated_drivers.items() if v == slowest_time])

            eliminated_drivers.extend(slowest_drivers)

        else:
            break

    return eliminated_drivers