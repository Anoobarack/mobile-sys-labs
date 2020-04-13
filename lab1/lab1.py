import getopt
import sys
import csv

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'x:y:')  # passing args


def main():  # operate with args
    with open(args[0], 'r', newline='') as infile:
        money = parse(infile)
        print(money)


def parse(infile):
    subscriber = '915642913'
    in_minutes = 0
    out_minutes = 0
    sms = 0
    spamreader = csv.reader(infile, delimiter = ',')
    for index, row in enumerate(spamreader):
        if index == 0:  # timestamp, msisdn_origin, ...
            continue
        if row[1] == subscriber:
            in_minutes += float(row[3])
            sms += float(row[4])
        if row[2] == subscriber:
            out_minutes += float(row[3])
    return tariffing(in_minutes, out_minutes, sms)


def tariffing(in_minutes, out_minutes, sms):
    in_value = 1
    out_value = 1
    if sms < 5:
        sms_money = 0
    elif sms < 10:
        sms_money = (sms - 5) * 1
    else:
        sms_money = 5 * 1 + (sms - 10) * 2
    in_money = in_minutes * in_value
    out_money = out_minutes * out_value
    return sms_money + in_money + out_money

if __name__ == '__main__':
    main()
