import time
import subprocess
import webbrowser
import threading

# Function to start the HTTP server
def start_server():
    # Start the HTTP server
    subprocess.run(["python3", "-m", "http.server", "8000"])

# Function to open the web browser to the localhost
def open_browser():
    time.sleep(1)  # Give the server a second to start
    webbrowser.open_new('http://localhost:8000/')

# Static audio file name
audio_filename = "test1.wav"

# Start the server in a new thread
threading.Thread(target=start_server, daemon=True).start()

# Open the web browser
open_browser()

while True:
    # Step 1: Record audio and save it as a file
    subprocess.run(["python3", "record.py"])
    
    # Step 2: Identify the song
    identification_result = subprocess.run(
        ["python3", "identify.py", audio_filename],
        capture_output=True,
        text=True
    )
    print(identification_result.stdout)  # prints a statement if correct song has been identified or error.
    
    # Add a delay before the next iteration if needed
    time.sleep(15)  # The loop will wait for 15 seconds before the next recording
