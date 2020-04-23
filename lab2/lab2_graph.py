#! /usr/bin/python3
import matplotlib.pyplot as plt
import datetime
import getopt
import sys

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'x:y:')  # passing args


def main():
    with open(args[0], 'r', newline='') as infile:
        file_content = infile.read().split('\n')
        del file_content[-5:]  # removing last descriptive lines
        first_row = file_content[1].split()
        first_datetime = datetime.datetime.strptime(first_row[0]+" "+first_row[1], "%Y-%m-%d %H:%M:%S.%f")
        for last_row in file_content:
            pass
        last_row = last_row.split()
        last_datetime = datetime.datetime.strptime(last_row[0]+" "+last_row[1], "%Y-%m-%d %H:%M:%S.%f")
        # first_datetime and last_datetime are class datetime.datetime
        deltatime = (last_datetime-first_datetime).total_seconds()
        count = datetime.timedelta(seconds=deltatime/50)
        bytes = 0
        x_time = []
        y_bytes = []
        for index, row in enumerate(file_content):
            if index == 0:  # first description line
                continue
            row = row.split()
            row_datetime = datetime.datetime.strptime(row[0]+" "+row[1], "%Y-%m-%d %H:%M:%S.%f")
            if row_datetime < count+first_datetime:
                if row[12] == "M":
                    bytes += float(row[11]) * 1024 * 1024
                else:
                    bytes += float(row[11])
            else:
                x_time.append(count.total_seconds())
                count += datetime.timedelta(seconds=deltatime/50)
                y_bytes.append(bytes)
                bytes = 0
                if row_datetime < count + first_datetime:
                    if row[12] == "M":
                        bytes += float(row[11]) * 1024 * 1024
                    else:
                        bytes += float(row[11])
        x_time.append(count.total_seconds())
        y_bytes.append(bytes)
        plt.xlabel("Time in seconds")
        plt.ylabel("Bytes")
        plt.title("Graph of data transition")
        plt.plot(x_time, y_bytes)
        plt.savefig("Graph.png")


if __name__ == '__main__':  # will not execute whole program if imported
    main()
