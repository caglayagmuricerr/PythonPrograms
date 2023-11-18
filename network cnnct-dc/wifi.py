import subprocess
import requests
import keyboard

def check_internet_access():
    """Checks if internet access is available."""
    try:
        # Try to connect to a website.
        requests.get("https://google.com")
        return True
    except requests.exceptions.ConnectionError:
        return False

def disconnect_wifi():
    if not check_internet_access():
        print("You are already disconnected.")
        return
    else: 
        try:
            subprocess.run(["netsh", "wlan", "disconnect"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error disconnecting Wi-Fi: {str(e)}")

def connect_to_wifi():
    if check_internet_access():
        print("You are already connected.")
        return
    else:
        try:     
            subprocess.run(["netsh", "wlan", "connect", "ssid=TurkTelekom_ZTX6HF","name=TurkTelekom_ZTX6HF"])
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to Wi-Fi: {str(e)}")

keyboard.add_hotkey('ctrl+alt+c', connect_to_wifi)
keyboard.add_hotkey('ctrl+alt+d', disconnect_wifi)

def main():
    keyboard.wait()

if __name__ == "__main__":
    main()