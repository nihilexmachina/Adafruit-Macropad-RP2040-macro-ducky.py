from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Ducky',                # Application name
    'macros' : [                     # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'HslfAtk',[Keycode.WINDOWS,'r',-Keycode.WINDOWS,0.5,'cmd.exe',Keycode.ENTER,-Keycode.ENTER,0.5,'certutil.exe -urlcache -split -f https://cutewallpaper.org/21/david-hasselhoff-puppies-wallpaper/Pin-on-Fitzness.jpg %userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\hasselhoff.jpg',Keycode.ENTER,-Keycode.ENTER,1.5,'reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d  "%userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\hasselhoff.jpg" /f',Keycode.ENTER,-Keycode.ENTER,0.5,'reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v WallPaperStyle /t REG_SZ /d  10 /f',Keycode.ENTER,-Keycode.ENTER,0.5,'reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Tilewallpaper /t REG_SZ /d  0 /f',Keycode.ENTER,-Keycode.ENTER,0.5,'FOR /L %i IN (1,1,150) DO (RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters)',Keycode.ENTER,-Keycode.ENTER,0.5,'exit',Keycode.ENTER,-Keycode.ENTER,0.5,Keycode.WINDOWS,'d',-Keycode.WINDOWS]),
        (0x000000, '',['']),
        (0x000000, '',['']),
        # 2nd row ----------
        (0x000000, '',['']),
        (0x000000, '',['']),
        (0x000000, '',['']),
        # 3rd row ----------
        (0x000000, '',['']),
        (0x000000, '',['']),  
        (0x000000, '',['']),        
        # 4th row ----------
        (0x000000, '',['']),
        (0x000000, '',['']),
        (0x000000, '',['']),
        # Encoder button ---
        (0x000000, '',[''])
    ]
}
