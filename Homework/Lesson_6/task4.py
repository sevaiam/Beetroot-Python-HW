def main():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_dic_1 = dict(enumerate(week, start=1))
    week_dic_2 = {week[x]: x + 1 for x in range(len(week))}


if __name__ == "__main__":
    main()
