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
        file_content.pop(0)  # removing first description line
        # ordered_tmp = sorted(tmp_dict.items(), key=lambda x: x[0])
        tmp_list = [line.split() for line in file_content]
        file_content = sorted(tmp_list, key=lambda x: datetime.datetime.strptime(x[0]+" "+x[1], "%Y-%m-%d %H:%M:%S.%f"))
        first_row = file_content[0]
        first_datetime = datetime.datetime.strptime(first_row[0]+" "+first_row[1], "%Y-%m-%d %H:%M:%S.%f")
        for last_row in file_content:
            pass
        last_datetime = datetime.datetime.strptime(last_row[0]+" "+last_row[1], "%Y-%m-%d %H:%M:%S.%f")
        # first_datetime and last_datetime are class datetime.datetime
        deltatime = (last_datetime-first_datetime).total_seconds()
        count = datetime.timedelta(minutes=5)
        bytes = 0
        x_time = []  # seconds since first datetime
        y_bytes = []  # traffic intensity during timedelta
        for row in file_content:
            row_datetime = datetime.datetime.strptime(row[0]+" "+row[1], "%Y-%m-%d %H:%M:%S.%f")
            if row_datetime < count+first_datetime:
                if row[12] == "M":
                    bytes += float(row[11]) * 1024 * 1024
                else:
                    bytes += float(row[11])
            else:
                x_time.append(count.total_seconds()/60)
                count += datetime.timedelta(minutes=5)
                y_bytes.append(bytes/1024)
                bytes = 0
                if row[12] == "M":
                    bytes += float(row[11]) * 1024 * 1024
                else:
                    bytes += float(row[11])
        x_time.append(count.total_seconds()/60)
        y_bytes.append(bytes/1024)
        plt.xlabel("Time from beginning in minutes")
        plt.ylabel("Traffic (Kb)")
        plt.title("Data transition per every 5 minutes")
        plt.plot(x_time, y_bytes)  # build graph
        plt.savefig("Graph.png")


if __name__ == '__main__':  # will not execute whole program if imported
    main()
