# Problem Statement: Write a Python program to create a Light class with three methods: turn_on() that switches the light on, turn_off() that switches it off, and status() that reports whether the light is currently on or off.

# Purpose: This exercise models a simple stateful object, where the object remembers and changes its own condition over time. It introduces the concept of state management within a class, a pattern found everywhere from UI components and IoT devices to game objects and workflow engines.

# Given Input: Create a Light object, call turn_on(), check status(), call turn_off(), and check status() again.

# Expected Output:

# Light is ON
# Current status: ON
# Light is OFF
# Current status: OFF

class Light:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
        print("Light is on")

    def turn_off(self):
        self.is_on = False
        print("Light is off")

    def status(self):
        if self.is_on:
            print("ON")
        else:
            print("OFF")

l1 = Light()
l1.turn_off()
l1.status()
l1.turn_on()
l1.status()