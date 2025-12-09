import os
import subprocess

CMD1=r'curl --cookie-jar - -s -o /dev/null -L "http://gstudent.gitam.edu/Login/?id=1KfzbrzcraVzS3aqK3oGsw=="'
CMD1_OUT=subprocess.check_output(CMD1, shell=True).decode()
ASPNET_ID=CMD1_OUT.strip().split()[-1]

CMD2=f'curl -s --cookie "ASP.NET_SessionId={ASPNET_ID}" https://gstudent.gitam.edu/Home/Gettimetable'
TT_PAGE=subprocess.check_output(CMD2, shell=True).decode()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(TT_PAGE)
