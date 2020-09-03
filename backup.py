from mypackages.filedownload import start_backup
from mypackages.filemanagement import move_files
from mypackages.wifi_check import wifi_check

# Func checks the current Wifi
wifi_check()

# Func runs Selenium and beginns to download the desired files
start_backup()

# Func moves files to a certain folder
move_files()

# End of script
print("done!!!")
