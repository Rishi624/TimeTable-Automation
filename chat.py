import subprocess

# Step 1: get session ID
cmd = r'curl --cookie-jar - -s -o /dev/null -L "http://gstudent.gitam.edu/Login/?id=1KfzbrzcraVzS3aqK3oGsw=="'
output = subprocess.check_output(cmd, shell=True).decode()

# Extract the ASP.NET session ID from the cookie-jar output
# The cookie jar format ends with the actual cookie value in the last column
ASPNET_ID = output.strip().split()[-1]

print("Session:", ASPNET_ID)

# Step 2: fetch timetable using the extracted cookie
cmd2 = f'curl -s --cookie "ASP.NET_SessionId={ASPNET_ID}" https://gstudent.gitam.edu/Home/Gettimetable'
TimeTable_Page = subprocess.check_output(cmd2, shell=True).decode()

print(TimeTable_Page)

