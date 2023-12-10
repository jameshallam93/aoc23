
TIME_DIST_DICT = {
    35: 212,
    93: 2060,
    73: 1201,
    66: 1044
}

def get_distance_travelled(time_holding, race_time):
    return time_holding * (race_time - time_holding)

def get_winning_times(record_time, distance):
    winning_times = []
    for t in range(1, record_time):
        if get_distance_travelled(t, record_time) >= distance:
            winning_times.append(t)
    return winning_times

def main():
    distances = {}
    for t, d in TIME_DIST_DICT.items():
        distances[t] = get_winning_times(t, d)
    prod = 1
    for t, d in distances.items():
        prod *= len(d)
    print(prod)


main()