import RPi.GPIO as GPIO
import time
import socket

# GPIO pin configuration
DIR = 19      # Direction pin
STEP = 26     # Step pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Stepper motor parameters
delay = 0.01
steps = 100

# Setup UDP socket for receiving FicTrac data
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0)

def run_motor(direction):
    GPIO.output(DIR, GPIO.HIGH if direction == "forward" else GPIO.LOW)
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

try:
    print("Waiting for FicTrac ball motion data...")
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            line = data.decode('utf-8')
            if line.startswith("#"):
                continue  # Skip header lines

            parts = line.strip().split()
            if len(parts) < 5:
                continue

            angle = float(parts[4])  # Adjust index based on FicTrac's output format

            if angle > 1.0:
                print("Ball moving forward -> Motor rotates forward")
                run_motor("forward")
            elif angle < -1.0:
                print("Ball moving backward -> Motor rotates backward")
                run_motor("backward")
            else:
                print("Ball static or minor movement -> No motor action")

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("Terminating program...")

finally:
    GPIO.cleanup()
    sock.close()
