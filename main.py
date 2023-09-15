from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = {}
    now = date.today()
    week = now.strftime('%A')

    # Присвоємо перемінні до дат
    d= timedelta(days=1)
    if week=="Monday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now,now +d,now +d*2,now +d*3,now +d*4,now +d*5,now +d*6)
    elif week=="Tuesday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d*6,now,now +d,now +d*2,now +d*3,now +d*4,now +d*5)
    elif week=="Wednesday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d*5,now+d*6,now,now +d,now +d*2,now +d*3,now +d*4)
    elif week=="Thursday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d*4,now+d*5,now+d*6,now,now +d,now +d*2,now +d*3)
    elif week=="Friday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d*3,now+d*4,now+d*5,now+d*6,now,now +d,now +d*2)
    elif week=="Saturday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d*2,now+d*3,now+d*4,now+d*5,now+d*6,now +d)
    elif week=="Sunday":
        (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(now+d,now+d*2,now+d*3,now+d*4,now+d*5,now+d*6,now)
    (Mo,Tu,We,Th,Fr)=([],[],[],[],[])
    (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)=(str(Monday).split("-"),str(Tuesday).split("-"),str(Wednesday).split("-"),str(Thursday).split("-"),str(Friday).split("-"),str(Saturday).split("-"),str(Sunday).split("-"))

    for slov in users:
        for key, value in slov.items():
            if key=="birthday":
                ta =str(value).split("-")
                if Monday[1]==ta[1] and Monday[2]==ta[2]:
                    Mo.append(slov["name"])
                    result["Monday"]= Mo
                if Tuesday[1]==ta[1] and Tuesday[2]==ta[2]:
                    Tu.append(slov["name"])
                    result["Tuesday"]=Tu
                if Wednesday[1]==ta[1] and Wednesday[2]==ta[2]:
                    We.append(slov["name"])
                    result["Wednesday"]=We
                if Thursday[1]==ta[1] and Thursday[2]==ta[2]:
                    Th.append(slov["name"])
                    result["Thursday"]=Th
                if Friday[1]==ta[1] and Friday[2]==ta[2]:
                    Fr.append(slov["name"])
                    result["Friday"]=Fr
                if Saturday[1]==ta[1] and Saturday[2]==ta[2]:
                    Mo.append(slov["name"])
                    result["Monday"]=Mo
                if Sunday[1]==ta[1] and Sunday[2]==ta[2]:
                    Mo.append(slov["name"])
                    result["Monday"]=Mo
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")