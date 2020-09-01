def wifi_check():
    import subprocess
    import time
    import sys

    from mypackages.config import Config

    results = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
    results = results.decode("utf8")
    results = results.replace("\r", "")
    results = results.replace("\n", "")
    results = results.split(" ")

    if Config.wifi_ssid_1 or Config.wifi_ssid_2 in results:
        print("connected to known network!")
        time.sleep(2)
    else:
        sys.exit("Non known network!")
        time.sleep(3)


if __name__ == "__main__":
    wifi_check()
else:
    print("module 'Wifi-Check' is imported")
