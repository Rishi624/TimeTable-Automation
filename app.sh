curl --cookie-jar - -s -o /dev/null -L "http://gstudent.gitam.edu/Login/?id=1KfzbrzcraVzS3aqK3oGsw==" | awk '/ASP.NET_SessionId/ {print $NF}'
