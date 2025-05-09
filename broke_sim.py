import time
import sys

broke = False
one_stroke = 0.0000000722
chillin = False
total_keystrokes = 0
total_earnings = 0 

print("Desperate Broke Job Simulator")
print("Press 'Y' to play")
start = input()
if start.lower() == "y":
    start_time = time.perf_counter()
    broke = True
else:
    print("k, i guess ur not broke")
    sys.exit()

while broke:
    user_input = input(f"Your goal is to get $1. Each keystroke you do is worth {one_stroke}. Start typing: ")
    keystroke_count = len(user_input)
    total_keystrokes += keystroke_count
    total_earnings += keystroke_count * one_stroke

    print(f"You typed {keystroke_count} characters. Total keystrokes: {total_keystrokes}. Total earnings: ${total_earnings:.10f}")

    if total_earnings >= 1.0:
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Congratulations. You've earned $1 in {total_time}. To leave this program, type 'exit'.")
        
        # Generate a unique signature for the session
        unique_signature = sum(ord(c) for c in f"{total_keystrokes}{total_earnings:.10f}{total_time}") % 1000000
        print(f"Your session signature is: {unique_signature}")
        chillin = True

while chillin:
    exit = input()
    if exit == "exit":
        sys.exit()
