from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = {}
    now = date.today()
    week = now.strftime('%A')

    # Присвоємо перемінні до дат
    d_1= timedelta(days=1)
    d_2= timedelta(days=2)
    d_3= timedelta(days=3)
    d_4= timedelta(days=4)
    d_5= timedelta(days=5)
    d_6= timedelta(days=6)
    if week=="Monday":
        Monday=(now)
        Tuesday=(now +d_1)
        Wednesday=(now +d_2)
        Thursday=(now +d_3)
        Friday=(now +d_4)
        Saturday=(now +d_5)
        Sunday=(now +d_6)
    elif week=="Tuesday":
        Monday=(now+d_6)
        Tuesday=(now)
        Wednesday=(now +d_1)
        Thursday=(now +d_2)
        Friday=(now +d_3)
        Saturday=(now +d_4)
        Sunday=(now +d_5)
    elif week=="Wednesday":
        Monday=(now+d_5)
        Tuesday=(now+d_6)
        Wednesday=(now)
        Thursday=(now +d_1)
        Friday=(now +d_2)
        Saturday=(now +d_3)
        Sunday=(now +d_4)
    elif week=="Thursday":
        Monday=(now+d_4)
        Tuesday=(now+d_5)
        Wednesday=(now+d_6)
        Thursday=(now)
        Friday=(now +d_1)
        Saturday=(now +d_2)
        Sunday=(now +d_3)
    elif week=="Friday":
        Monday=(now+d_3)
        Tuesday=(now+d_4)
        Wednesday=(now+d_5)
        Thursday=(now+d_6)
        Friday=(now)
        Saturday=(now +d_1)
        Sunday=(now +d_2)
    elif week=="Saturday":
        Monday=(now+d_2)
        Tuesday=(now+d_3)
        Wednesday=(now+d_4)
        Thursday=(now+d_5)
        Friday=(now+d_6)
        Saturday=(now)
        Sunday=(now +d_1)
    elif week=="Sunday":
        Monday=(now+d_1)
        Tuesday=(now+d_2)
        Wednesday=(now+d_3)
        Thursday=(now+d_4)
        Friday=(now+d_5)
        Saturday=(now+d_6)
        Sunday=(now)
    (Mo,Tu,We,Th,Fr)=([],[],[],[],[])
    Monday=str(Monday).split("-")
    Tuesday=str(Tuesday).split("-")
    Wednesday=str(Wednesday).split("-")
    Thursday=str(Thursday).split("-")
    Friday=str(Friday).split("-")
    Saturday=str(Saturday).split("-")
    Sunday=str(Sunday).split("-")

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