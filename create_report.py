#!/usr/bin/env python3
import sys
import sqlite3
conn = sqlite3.connect('hw8SQLite.db')
c = conn.cursor()
# CS3030 Assignment
# Author: Trevor Orgill
# Description: Takes in a Date and formats it to date time


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

    current = 1
    end = []
    end.append("")
    eachamount = []
    eachamount.append("")
    for row in c.execute("SELECT t.trans_id, t.trans_date, t.card_num, tl.qty, tl.amt, p.prod_desc " +
                         "FROM trans t INNER JOIN trans_line tl " +
                         "ON t.trans_id = tl.trans_id " +
                         "INNER JOIN products p " +
                         "ON p.prod_num = tl.prod_num "
                         "WHERE t.trans_date > '" + formatDate(argv[1], "beg") +
                         "' AND t.trans_date < '" + formatDate(argv[2], "end") + "'"):
        if (row[0] != current):
            if (len(end[current][0]) < 45):
                end[current][0] = end[current][0] + '00000000          00000000          ' + str(eachamount[current]).replace('.','').zfill(6)
            elif (len(end[current][0]) < 63):
                end[current][0] = end[current][0] + '00000000          ' + str(eachamount[current]).replace('.','').zfill(6)
            current = current +1
        if (row[0] == current):
            if (len(end) == current):
                end.append([])
                eachamount.append(0)
                eachamount[current] = eachamount[current] + row[4]
                end[current].append(str(row[0]).zfill(5) + row[1][0] + row[1][1] + row[1][2] + row[1][3] + row[1][5] + row[1][6] +
                    row[1][8] + row[1][9] + row[1][11] + row[1][12] + row[1][14] + row[1][15] +
                    str(row[2])[8:] + str(row[3])[0].zfill(1) + str(row[3])[1].zfill(1) + str(row[4]).replace('.','').zfill(6) + str(row[5]).ljust(10))
            else:
                eachamount[current] = eachamount[current] + row[4]
                end[current][0] = end[current][0] + (str(row[3])[0] + str(row[3])[1]).replace('.','').zfill(2) + str(row[4]).replace('.','').zfill(6) + str(row[5]).ljust(10)
            if (len(end[current][0]) > 75):
                end[current][0] = end[current][0] + str(eachamount[current]).replace('.','').zfill(6)

    for i in end:
        if (i != ""):
            print(str(i).replace("'",'').replace('[','').replace(']',''))


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)

    exit(0)
