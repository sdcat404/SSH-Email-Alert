# SSH-Email-Alert
This is a python program that runs in the background on linux servers such as Raspberry Pi, It looks for SSH connections in the auth.log file and then sends an automatic email to you alerting you that someone has SSH'd or attempted but failed to SSH into your server


# Setup Your Gmail With An App Password
For this to work, we need to setup an App Password on your Gmail account.

1: Go to https://myaccount.google.com/
2: Select Security.
3: Under 'Signing in to Google', select 2-Step Verification.
4: At the bottom of the page, select App passwords.
5: Enter a name that helps you remember where you’ll use the app password.
6: Select Generate.
7: To enter the app password, follow the instructions on your screen. The app password is the 16-character code that is generated on your device.
8: Select Done.

If you follow the above steps correctly, then you should now have an App Password! 
Good job!

# But, SDcat404. This doesn't work on my machine!
After testing this out, it wont work on all distros, and yes this includes macOS (sorry not sorry) 
On most linux systems the SSH logs are kept in "/var/log/auth.log" but on macOS its kept in "/var/log/system.log"
So have a play around on line '9' and see what works for you.

