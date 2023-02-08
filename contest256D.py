'''
В соревновании по бегу приняли участие n спортсменов: i-й из них пробежал дистанцию за ti

секунд. Жюри хочет назначить места участникам по следующим правилам:

    места пронумерованы от 1

и далее (лучшее место — первое);
если у двух спортсменов результаты одинаковые или отличаются на одну секунду, то они делят место (в этом случае считаем, что они делят лучшее из поделенных мест);
участники делят место только в результате применения предыдущего правила (возможно, несколько раз);
если k
участников делят место p, то места следующих за ними участников нумеруются начиная с k+p. 
'''

def grade_runners(amount, times):
    sorted_results = {}
    sorted_times = sorted(times)
    last_time = 1
    sorted_results[sorted_times[0]] = 0

    for count in range(1, amount):
        if sorted_times[count] in sorted_results:
            last_time += 1
            continue
        elif sorted_times[count] > (sorted_times[count-1] + 1):
            sorted_results[sorted_times[count]] = count
            last_time = 1
        else:
            sorted_results[sorted_times[count]] = count - last_time
            last_time += 1

    return [sorted_results[i]+1 for i in times]

def main():
    set_of_results = []
    amount_of_sets = int(input())

    for _ in range(amount_of_sets):
        amount_of_runners = int(input())
        runners_results = [int(i) for i in input().split(' ')]
        set_of_results.append(grade_runners(amount_of_runners, runners_results))

    for results in set_of_results:
        print(*results)


if __name__ == '__main__':
    main()