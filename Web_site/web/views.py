from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3, random, datetime


def Wlogin(request):
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                return False
        else:
            return True


def admin(request):
    wish = ""
    repor = ""
    forms = """<tr>
                <td>Hi, I'm your first cell.</td>
                <td>I'm your second cell.</td>
                <td>I'm your third cell.</td>
                <td>I'm your fourth cell.</td>
                <td>Hi, I'm your first cell.</td>
                <td>I'm your second cell.</td>
                <td>I'm your third cell.</td>
                <td>I'm your fourth cell.</td>
            </tr>"""
    pets = ""
    users = ""

    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        bass = cursor.fetchall()
        for bas in bass:
            users += f"""<tr>
                                <td>{bas[0]}</td>
                                <td>{bas[1]}</td>
                                <td>{bas[2]}</td>
                                <td>{bas[4]}</td>
                                <td>{bas[5]}</td>
                                <td>{bas[6]}</td>
                                <td>{bas[7]}</td>
                            </tr>"""

        cursor.execute('SELECT * FROM Pets')
        bass = cursor.fetchall()
        for bas in bass:
            pets += f"""<tr>
                                            <td>{bas[0]}</td>
                                            <td>{bas[1]}</td>
                                            <td>{bas[2]}</td>
                                            <td>{bas[4]}</td>
                                        </tr>"""

        cursor.execute('SELECT * FROM Report')
        bass = cursor.fetchall()
        for bas in bass:
            repor += f"""<tr>
                                            <td>{bas[0]}</td>
                                            <td>{bas[1]}</td>
                                            <td>{bas[2]}</td>
                                            <td>{bas[3]}</td>
                                        </tr>"""

        cursor.execute('SELECT * FROM Donats')
        bass = cursor.fetchall()
        for bas in bass:
            wish += f"""<tr>
                                                        <td>{bas[0]}</td>
                                                        <td>{bas[1]}</td>
                                                        <td>{bas[2]}</td>
                                                        <td>{bas[3]}</td>
                                                    </tr>"""

        cursor.execute('SELECT * FROM Applications')
        bass = cursor.fetchall()
        for bas in bass:
            forms += f"""<tr>
                                            <td>{bas[0]}</td>
                                            <td>{bas[1]}</td>
                                            <td>{bas[2]}</td>
                                            <td>{bas[3]}</td>
                                            <td>{bas[4]}</td>
                                            <td>{bas[5]}</td>
                                            <td>{bas[6]}</td>
                                            <td>{bas[7]}</td>
                                        </tr>"""

    with open(r"web/templates/call.html", "w", encoding="utf-8") as form:
        form.write(f"""<div class="main">
    <div>        
        <h2>Пожертвования</h2>
        <table>
            <tr>
                <td>ID пользователя</td>
                <td>ID питомца</td>
                <td>Данная сумма</td>
                <td>Описание</td>
            </tr>{wish}
        </table>
    </div>
    <div>
        <h2>Объявления о находке</h2>
        <table>
            <tr>
                <td>ID объявления</td>
                <td>ID пользователя</td>
                <td>Описание</td>
                <td>Место</td>
            </tr>{repor}
        </table>
    </div>
    <div>
        <h2>Заявки</h2>
        <table>
            <tr>
                <td>ID пользвателя</td>
                <td>ID питомца</td>
                <td>Возраст</td>
                <td>ФИО</td>
                <td>Статус</td>
                <td>Место жительства</td>
                <td>Место работы</td>
                <td>Увлечения</td>
            </tr>{forms}
        </table>
    </div>
</div>
<div class="main">
    <div>        
        <h2>Пользователи</h2>
        <table>
            <tr>
                <td>ID </td>
                <td>Логин</td>
                <td>Пароль</td>
                <td>Почта</td>
                <td>Номер телефона</td>
                <td>Описание</td>
                <td>Навыки</td>
            </tr>{users}
        </table>
    </div>
    <div>
        <h2>Питомцы</h2>
        <table>
            <tr>
                <td>ID</td>
                <td>Имя</td>
                <td>Порода</td>
                <td>Собраная сумма</td>
            </tr>{pets}
        </table>
    </div>
</div>""")
    return render(request, "Admin.html")


def about(request):
    return render(request, "About.html")



def index(request):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    return render(request, "Index.html", context={"UserName": Uname})


def info(request, title="", text=""):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    return render(request, "Info.html", context={"Tit": title, "Txt": text, "UserName": Uname})


def ext(request):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                cursor.execute(f'UPDATE Users SET agent = " " WHERE id = {user[0]};')

        connection.commit()
    return redirect(f'/')

def pet(request, num=0):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]

    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        pits=[]
        for pit in pets:
            pits.append(pit)

        connection.commit()
    return render(request, "Pets.html",
                  context={"NumPet": pits[num][0], "Name": pits[num][1], "KRTKO": pits[num][3], "PetInd": num, "What": pits[num][2], "UserName": Uname})


def Pnext(request, num):
    if Wlogin(request): return redirect('/')
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        pits=[]
        for pit in pets:
            pits.append(pit)

        connection.commit()
    if num + 1 >= len(pits):
        num1 = 0
    else:
        num1 = num + 1
    return redirect(f'/pet/{num1}/')


def Pback(request, num):
    if Wlogin(request): return redirect('/')
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        pits=[]
        for pit in pets:
            pits.append(pit)

        connection.commit()
    if num - 1 < 0:
        num1 = len(pits) - 1
    else:
        num1 = num - 1
    return redirect(f'/pet/{num1}/')


def Pwish(request, num):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        name=""
        for pit in pets:
            if pit[0] == num:
                sum = float(pit[4])
                name = pit[1]

        connection.commit()
    Sum = request.POST.get("Sum", None)
    Cell = request.POST.get("Text", None)
    user_agent = request.META["HTTP_USER_AGENT"]
    if Sum != None and Sum != "":
        Sum = float(Sum)
        with sqlite3.connect(r'web\static\database\db.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM Users')
            users = cursor.fetchall()

            for user in users:
                if user[3] == user_agent:
                    ID_u = user[0]
            cursor.execute('INSERT INTO Donats (id_user, id_pet, sum, wish) VALUES (?, ?, ?, ?)', (ID_u, num, Sum, Cell))
            cursor.execute(f"UPDATE Pets SET sum = {Sum+sum} WHERE id = {num};")
            connection.commit()
        return redirect(f'/info/Спасибо за пожертвование/ /')
    return render(request, "Wish.html", context={"NumPet": num, "Name": f"Пожертвование - {name}", "UserName": Uname})


def Pforum(request, num):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    Mess = request.POST.get("Mess", None)
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                ID_u = user[0]
                Uname = user[1]
        for pit in pets:
            if pit[0] == num:
                name = pit[1]
                data = eval(pit[5])
        if Mess != None and Mess != "":
            date = datetime.datetime.now()
            date = f"{date.day}.{date.month}.{date.year} {date.hour}:{date.minute}"
            data.append([date, ID_u, Mess])
            cursor.execute(f'UPDATE Pets SET forum = "{data}" WHERE id = {num};')
        for user in users:
            for i in range(len(data)):
                if data[i][1] == user[0]:
                    data[i][1] = user[1]
        oni = ""
        ty = ""
        for i in data:
            if i[1] == Uname:
                oni += "        \n<br>"
                ty += f"        \n<p>{i[0]} - {i[1]} - {i[2]}</p>"
            else:
                oni += f"       \n<p>{i[0]} - {i[1]} - {i[2]}</p>"
                ty += f"        \n<br>"
        with open(r"web/templates/call.html","w",encoding="utf-8") as form:
            form.write(f"""<div class="main">
    <div>{ty}
    </div>
    <div>{oni}
    </div>
</div>""")
    return render(request, "Forum.html", context={"NumPet": num, "Name": f"Обсуждение - {name}", "Data": "gh\n\nhj", "UserName": Uname})


def Ptake(request, num):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pets')
        pets = cursor.fetchall()
        name=""
        for pit in pets:
            if pit[0] == num:
                name = pit[1]
    FIO = request.POST.get("Fio", None)
    Statys = request.POST.get("Statys", None)
    Home = request.POST.get("Home", None)
    Work = request.POST.get("Work", None)
    Dosyg = request.POST.get("Dosyg", None)
    Allegrik = request.POST.get("Allegrik", None)
    Years = request.POST.get("Years", None)
    user_agent = request.META["HTTP_USER_AGENT"]
    if (FIO != None and FIO != '') and (Statys != None and Statys != '') and (Home != None and Home != '') and (Work != None and Work != ''):
        with sqlite3.connect(r'web\static\database\db.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM Users')
            users = cursor.fetchall()

            for user in users:
                if user[3] == user_agent:
                    ID_u = user[0]

            cursor.execute('INSERT INTO Applications (id_user, id_pet, years, fio, statys, home, work, hobby, Allergic) '
                           'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (ID_u, num, Years, FIO, Statys, Home, Work, Dosyg, Allegrik))

            connection.commit()
        return redirect(f'/info/Заявка отправлена/ /')
    else:
        return render(request, "Take.html", context={"Name": name, "NumPet": num, "UserName": Uname})


def report(request):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
    return render(request, "Report.html", context={"UserName": Uname})


def RPpet(request):
    if Wlogin(request): return redirect('/')
    pet = request.POST.get("Pet", "None")
    place = request.POST.get("Place", "None")
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Report')
        users = cursor.fetchall()

        ids=[]
        for user in users:
            ids.append(user[0])
        ID = random.randint(10000, 99999)
        while ID == ids:
            ID = random.randint(10000, 99999)

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                ID_u = user[0]

        cursor.execute('INSERT INTO Report (id, usernum, pet, place) VALUES (?, ?, ?, ?)', (ID,ID_u,pet,place))

        connection.commit()
    return redirect('/main/')


def account(request):
    return render(request, "Account.html")


def login(request):
    Login = request.POST.get("WhatUser", None)
    Password = request.POST.get("KeyAccess", None)
    user_agent = request.META["HTTP_USER_AGENT"]
    if Login == "Admin" and Password == "123":
        return redirect(f'/admin/')
    if Login == None: return redirect('/')
    if Password == None: return redirect('/')

    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[1] == Login and user[2] == Password:
                cursor.execute(f"UPDATE Users SET agent = '{user_agent}' WHERE id = {user[0]};")
                break
        else:
            return redirect(f'/')
    connection.commit()
    return redirect(f'/main/')


def reg(request):
    return render(request, "Registration.html")


def Rlogin(request):
    print("--------------------------------------------------------------------")
    Login = request.POST.get("User", None)
    Password = request.POST.get("Key", None)
    Email = request.POST.get("Email", "no@email.post")
    Telephone = request.POST.get("Telephone", '+7 (000) 000 00-00')
    Like = request.POST.get("O_like", "None")
    Skill = request.POST.get("O_skills", "None")
    user_agent = request.META["HTTP_USER_AGENT"]

    if Login == None: return redirect('/')
    if Password == None: return redirect('/')

    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        ids = []
        for user in users:
            if user[1] == Login: return redirect('/')
            if user[2] == Password: return redirect('/')
            ids.append(user[0])
        ID = random.randint(10000, 99999)
        while ID == ids:
            ID = random.randint(10000, 99999)


        cursor.execute('INSERT INTO Users (id, login, password, agent, email, phone, like, skill) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (ID, Login, Password, user_agent, Email, Telephone, Like, Skill))
        connection.commit()
        return redirect('/main/')
    return redirect('/')


def new(request):
    if Wlogin(request): return redirect('/')
    Login = request.POST.get("User", None)
    Password = request.POST.get("Key", None)
    Email = request.POST.get("Email", "no@email.post")
    Telephone = request.POST.get("Telephone", '+7 (000) 000 00-00')
    Like = request.POST.get("O_like", "None")
    Skill = request.POST.get("O_skills", "None")
    user_agent = request.META["HTTP_USER_AGENT"]
    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                if Login != user[1]:
                    cursor.execute(f"UPDATE Users SET login = '{Login}' WHERE id = {user[0]};")
                if Password != user[2]:
                    cursor.execute(f"UPDATE Users SET password = '{Password}' WHERE id = {user[0]};")
                if Email != user[4]:
                    cursor.execute(f"UPDATE Users SET email = '{Email}' WHERE id = {user[0]};")
                if Telephone != user[5]:
                    cursor.execute(f"UPDATE Users SET phone = '{Telephone}' WHERE id = {user[0]};")
                if Like != user[6]:
                    cursor.execute(f"UPDATE Users SET like = '{Like}' WHERE id = {user[0]};")
                if Skill != user[7]:
                    cursor.execute(f"UPDATE Users SET skill = '{Skill}' WHERE id = {user[0]};")

        connection.commit()
    return redirect('/main/')


def acc(request):
    if Wlogin(request): return redirect('/')
    user_agent = request.META["HTTP_USER_AGENT"]

    with sqlite3.connect(r'web\static\database\db.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for user in users:
            if user[3] == user_agent:
                Uname = user[1]
                USER = user
    return render(request, "Cabinet.html",
                  context={"UserName": Uname, "Login": USER[1], "Password": USER[2], "Email": USER[4], "Telephone": USER[5], "Like": USER[6], "Skill": USER[7]})
