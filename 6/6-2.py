import time

time_ = 35937366
dist = 212206012011044

def get_distance_travelled(time_holding, race_time):
    return time_holding * (race_time - time_holding)


def get_winning_times(record_time, distance):
    winning_times = []
    for t in range(1, record_time):
        if get_distance_travelled(t, record_time) >= distance:
            winning_times.append(t)
    return winning_times


def main():
    start = time.perf_counter()
    print(len(get_winning_times(time_, dist)))
    end = time.perf_counter()
    print(f"ran in {end - start} seconds")

main()