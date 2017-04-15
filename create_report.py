#!/usr/bin/env python3
import sys
#CS3030 Assignment
#Author: Trevor Orgill
#Description: Takes in a Date and formats it to date time


def formatDate(date, time):
    """
    Takes in date (YYYYMMDD) and formats it to Date-Time (YYYY-MM-DD hh:mm)
    Pass in the date and the time (beg or end)
    """
    if (len(date) != 8):
        print("Invalid date length")
        exit(1)
    if (time == "beg"):
        return (date[:4]+"-"+date[4:6]+"-"+date[6:8]+" 00:00")
    elif (time == "end"):
        return (date[:4]+"-"+date[4:6]+"-"+date[6:8]+" 23:59")
    else:
        print("Invalid Time Parameter (beg or end)")
        exit(1)


def usage():
    """
    Usage Function
    """
    print("Takes in 2 dates (YYYYMMDD) and displays them in Date-Time Format (YYYY-MM-DD hh:mm)")
    exit(1)


def main(argv):
    """
    Main Function
    """
    if (argv[1] == "--help"):
        usage()
    if (len(argv) != 3):
        print("Invalid number of arguments")
        usage()
    if (len(argv[1]) != 8):
        print("Invalid date length")
        usage()
    if (len(argv[2]) != 8):
        print("Invalid date length")
        usage()
    print(formatDate(argv[1], "beg"))
    print(formatDate(argv[2], "end"))


if __name__ == "__main__":
    main(sys.argv)

    exit(0)
