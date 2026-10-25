import time
from AADFramework.ArduinoComponents import ServoMotor, DigitalInput, DigitalOutput, ControlBoard, InputMonitor

controller = ControlBoard('COM5')

redLED = controller.buildDigitalOutput(12, 'redLED')
greenLED = controller.buildDigitalOutput(11, 'greenLED')
buzzer = controller.buildDigitalOutput(10, 'Buzzer')
button_reset = controller.buildDigitalInput(7, 'Reset Button')
irSensor = controller.buildDigitalInput(4, 'irSensor')
motor = controller.buildServoMotor(2, 'motor')

motor.homePos = 0
motor.minAngle = 0
motor.maxAngle = 180

monitor = controller.buildInputMonitor()

controller.start()
monitor.start()
print("Quality Control Machine operational.")

while True:
    if irSensor.getCountValue() >= 1:
        motor.turnTo(90, 20)
        buzzer.turnOn()
        redLED.turnOn()
        greenLED.turnOff()
        print("***** DEFECT DETECTED *****")
        print("Please remove defect from slider!")
        print("Press reset button to reset.")

    elif button_reset.getCountValue() >= 1:
        buzzer.turnOff()
        redLED.turnOff()
        motor.turnTo(0, 20)
        print("***** DEFECT REMOVED *****")
        print("Quality Control Machine operational.")
        continue

    else:
        greenLED.turnOn()

controller.shutdown()


