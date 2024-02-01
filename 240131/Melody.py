import RPi.GPIO as GPIO
import time

# GPIO warning disable
GPIO.setwarnings(False)

# Buzzer pin setup using BCM numbering
BUZZER_PIN = 24  # BCM numbering for pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
buzzer_pwm = GPIO.PWM(BUZZER_PIN, 1000)  # PWM object creation, set frequency to 1000Hz

# Buzzer on function
def buzzerOn():
    buzzer_pwm.start(50)  # Set to 50% duty cycle

# Buzzer off function
def buzzerOff():
    buzzer_pwm.stop()

happy_birthday_melody = [
    (659, 0.5), (659, 0.5), (880, 1), (659, 0.5),
    (659, 0.5), (987, 1), (659, 0.5), (784, 0.5),
    (587, 1), (659, 0.5), (659, 0.5), (880, 1),
    (659, 0.5), (659, 0.5), (987, 1), (659, 0.5),
    (784, 0.5), (587, 1), (659, 0.5), (659, 0.5),
    (1318, 1), (1046, 0.5), (987, 0.5), (880, 1.5)
]

melody = [
    (392, 0.5), (330, 0.5), (392, 0.5), (392, 0.5),
    (349, 0.5), (392, 0.5), (330, 0.5), (294, 0.5),
    (392, 1), (330, 0.5), (247, 0.5), (247, 0.5),
    (262, 0.5), (262, 0.5), (311, 1), (415, 0.5),
    (330, 0.5), (330, 0.5), (262, 0.5), (349, 0.5),
    (247, 0.5), (330, 0.5), (294, 0.5), (392, 1),
]

# Melody playing function
def playMelody(melody):
    for note, duration in melody:
        buzzer_pwm.ChangeFrequency(note)
        buzzerOn()
        time.sleep(duration)
        buzzerOff()
        time.sleep(0.1)  # 0.1-second delay between each note

# Main operation
try:
    playMelody(melody)

finally:
    GPIO.cleanup()
