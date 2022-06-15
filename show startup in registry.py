import winreg

Registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
RawKey = winreg.OpenKey(Registry, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
try:
    counter = 0
    while True:
        name, value, type = winreg.EnumValue(RawKey, counter)
        print(f'Value: {name}\nPath: {value}\n')
        counter += 1
except WindowsError:
    print()

print("==============================================================")

Registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
RawKey = winreg.OpenKey(Registry, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
try:
    counter = 0
    while 1:
        name, value, type = winreg.EnumValue(RawKey, counter)
        print(f'Value: {name}\nPath: {value}\n')
        counter += 1
except WindowsError:
    print()

print("==============================================================")

Registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
RawKey = winreg.OpenKey(Registry, "SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run")
try:
    counter = 0
    while True:
        name, value, type = winreg.EnumValue(RawKey, counter)
        print(f'Value: {name}\nPath: {value}\n')
        counter += 1
except WindowsError:
    print()