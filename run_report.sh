#!/bin/bash -
#===============================================================================
#
#          FILE: run_report.sh
#
#         USAGE: ./run_report.sh
#
#   DESCRIPTION:
#
#        AUTHOR: Dr. Hugo Valle (), hugovalle1@weber.edu
#  ORGANIZATION: WSU
#       CREATED: 04/14/2017 12:57:54 PM
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error


help()
{
    echo "Usage "
}

if [[ $1 == "--help" ]]
then
    help
fi

while getopts ":f:t:e:u:p:" opt
do
    case $opt in
        f) begDate=$OPTARG
            ;;
        t) endDate=$OPTARG
            ;;
        e)
            email=$OPTARG
            ;;
        u)
            user=$OPTARG
            ;;
        p)
            passwd=$OPTARG
            ;;
        /?)
            help
            ;;
    esac
done

if [[ -z $begDate || -z $endDate || -z $email || -z $user || -z $passwd ]]
then
    echo "Require all parameters to continue"
    echo "BegDate: $begDate"
    echo "EndDate: $endDate"
    echo "Email: $email"
    echo "User: $user"
    if [[ -z $passwd ]]
    then
        echo "Password is null"
    fi
fi

# Dates are verified in report.py module

python3 create_report.py $begDate $endDate >> temp.txt

fileName="NEEDNAME"
file="NEEDFILE"
ftpDest="137.190.19.104"

if [[ $? == 0 ]]
then
    `zip -v $fileName $file`

    `ftp -in $ftpDest << EOF
    quote USER $user
    quote PASS $passwd
    put $file
    bye
    EOF`

    echo "Successfully created a transaction report from $begDate to $endDate" | mail -s "Successfully transfer file $ftpDest" $email
fi

if [[ $? == 1 ]]
then
    echo "Error in create_report.py"
    echo "Bad input parameters $begDate to $endDate" | mail -s "The create program exit with code 1" $email

    exit 1
fi

if [[ $? == 2 ]]
then
    echo "No transactions available from $begDate to $endDate" | mail -s "The create_report program exit with code 2" $email

    exit 1
fi

exit 0

