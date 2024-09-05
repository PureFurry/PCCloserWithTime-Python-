import os
import time

# Select Time Type
print("Select Time Type:")
print("1. Minutes")
print("2. Hours")
print("3. Seconds")

timeType = int(input("Choise (1, 2 or 3): "))

# Get time from user based on time type
if timeType == 1:
    shutdownTime = int(input("After how many minutes should it be closed? ")) * 60  # Convert Minutes
elif timeType == 2:
    shutdownTime = int(input("After how many hours should it be closed? ")) * 3600  # Convert Hours
elif timeType == 3:
    shutdownTime = int(input("After how many seconds should it be closed? "))
else:
    print("Wrong Choise.")
    exit()

# Wait for the specified time
print(f"Computer after {shutdownTime} shoutdown")
time.sleep(shutdownTime)

# Bilgisayarı kapat
os.system("shutdown /s /t 1")  # For Windows

# If you are using Linux or Mac, you can use the following line:
# os.system("sudo shutdown -h now")
