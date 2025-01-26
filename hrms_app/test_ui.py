# filepath: /c:/Users/DeeAnn/Desktop/HRMSPROJECT/test_ui.py
from colorama import init, Fore, Style
from tqdm import tqdm
import time

# Configurable sleep duration
sleep_duration = 0.05  # Adjust this value as needed

# Initialize colorama
init()

# Display a colored message
print(Fore.GREEN + "This is a test message." + Style.RESET_ALL)

# Display a progress bar using tqdm
for i in tqdm(range(100)):
    time.sleep(sleep_duration)