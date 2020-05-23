#! /usr/bin/python3
import getopt
import sys

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'x:y:')  # passing args


def main():  # operate with args
    with open(args[0], 'r', newline='') as infile:
        money = parse(infile)
        print(money)


def parse(infile):
    subscriber = "192.168.250.59"
    bytes = 0
    file_content = infile.read().split('\n')
    del file_content[-5:]  # removing last descriptive lines
    for index, row in enumerate(file_content):
        if index == 0:  # skip first description line
            continue
        row = row.split()
        """
        file structure:
        row[0] is date as year-month-day
        row[1] is time as hours:mins:secs.msecs
        row[2] is Event
        row[3] is XEvent
        row[4] is protocol
        row[5] is source ip addr
        row[6] is ->
        row[7] is destination ip addr
        row[8] is xip addr
        row[9] is ->
        row[10] is xip addr
        row[11] is bytes
        row[12] is 0 OR M if Mbytes in 11
        row[13] is 0 if 12 is M
        """
        if subscriber in row[5]:
            if row[12] == "M":
                bytes += float(row[11]) * 1024 * 1024
            else:
                bytes += float(row[11])
        if subscriber in row[7]:
            if row[12] == "M":
                bytes += float(row[11]) * 1024 * 1024
            else:
                bytes += float(row[11])
    return tariffing(bytes)


def tariffing(bytes):  # module to import
    if bytes < 500*1024*1024:
        if bytes > 500*1024:
            retval = 500*0.5 + (bytes-500*1024) / 1024
        else:
            retval = bytes / 1024 * 0.5
    else:
        retval = 500*0.5 + (bytes-500*1024*1024) / 1024 / 1024
    return int(retval)


if __name__ == '__main__':  # will not execute whole program if only tariffing is imported
    main()
