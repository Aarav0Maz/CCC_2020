def Epidemiology(P1, N1, R1):
    day = 0 
    totalInfected = N1
    while totalInfected <= P1:
        N1 = N1 * R1 
        totalInfected += N1
        day += 1
    return day


def main():
    P = int(input().strip())
    N = int(input().strip())
    R = int(input().strip())
    most_ill_day = Epidemiology(P, N, R)
    print(f"the day with the most ill people is day {most_ill_day}")


if __name__ == "__main__":
    main()