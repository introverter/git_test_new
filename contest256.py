def ref_schedule(windows, user, times):
    if times.count(1) > 2 or times.count(windows) > 2:
        return 'x'
    for time in range(user):
        if times.count(times[time]) > 3:
            return 'x'
    return 1

def main():
    results = []
    amount_of_sets = int(input())

    for _ in range(amount_of_sets):
        data_line = input().split()
        windows = int(data_line[0])
        users = int(data_line[1])
        times = [int(i) for i in input().split()]
        results.append(ref_schedule(windows, users, times))

    for result in results:
        print(result)

if __name__ == '__main__':
    main()