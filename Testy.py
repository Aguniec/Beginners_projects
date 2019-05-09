import datetime

def get_data(filename):

    data_tuples = list()

    with open("sample_data.csv", "r") as f:
        for line in f:
            data_tuples.append(line.strip().split(","))

    format_string = "%Y-%m-%d %H:%M:%S"


    data_tuples = [(datetime.datetime.strptime(x[0],format_string).hour, float(x[1])) for x in data_tuples]

    return (data_tuples)


bucket = dict()
for item in get_data("sample_data.csv"):
    if item[0] in bucket:
        bucket[item[0]][0] += 1
        bucket[item[0][1]] += item[1]




