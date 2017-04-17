# cs3030_py5

run_report.sh 
Accepts a user name, password, start date, end date and email. 
Checks all inputs are there and passes in the start date and end date into create_report.py
Checks the exit state of create_report.py and on success ftp's the file and emails the user.
Else will email the user based on the error from create_report.py

create_report.py
Accepts a start date and end date. Queries the DB based on those dates.
Formats the string as appropriate.
Sends data to run_report to be zipped and ftp'd.
