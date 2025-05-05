import time

def delay_print(text, delay=1):
    print(text)
    time.sleep(delay)

delay_print("Connecting to SCSP Hackathon...")
delay_print("Access granted")
delay_print("AI+ Expo Hackathon 2025")
delay_print("SCSP x AGI House")
delay_print("June 2-4 | Washington D.C.")
delay_print("Ready to build the future?")

# Ask if user has registered
response = input("Have you registered? (y/n): ").strip().lower()

if response == 'y':
    delay_print("Great! See you there")
else:
    delay_print("Register here: https://expo.scsp.ai/hackathon")

