#_____ИМПОРТЫ_____
import requests #Запросы на сервер
from datetime import datetime # Узнать сколько времени
from time import sleep #Сон


token = "dc54d704dc54d704dc54d7049adc256519ddc54dc54d704839a84cacf70b105fbdf9838"
myid = "433849874"

#Основной метод
def get_data(method, parameters, token = token):
    url = 'https://api.vk.com/method/'+ method +'?'+ parameters +'&v=5.52'+'&access_token=' + str(token)
    response = requests.get(url)
    return(response.json())

#Проверка id
def check_id(id_person):
    id_person = str(id_person).split("/")
    if len(id_person) > 2:
        id_person = id_person[3]
    else:
        id_person = id_person[0]
    #Превращаем id во внутренний id
    id_person = ((get_data(method = "users.get", parameters = "user_ids=" + str(id_person), token = token))["response"])[0]
    id_person = id_person["id"]
    
    return id_person


#Имя Фамилия id
def get_NamePerson(id_person):
    id_person = check_id(id_person)
    # Имя и фамилия
    name = ((get_data(method = "users.get", parameters = "user_ids=" + str(id_person), token = token))["response"])[0]
    firstname = name["first_name"] #Имя
    lastname = name["last_name"] #Фамимлия
    idp = name["id"]
    #Возврат значения
    return [firstname, lastname, idp]


#Фото профиля
def get_PhotoPerson(id_person):
    id_person = check_id(id_person)
    # Фото профиля
    photo = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=photo_max", token = token))["response"])[0]
    photo = photo["photo_max"]
    #Возврат значения
    return photo

print(get_PhotoPerson("https://vk.com/id.mlfv"))

#Cодержимое "О себе"
def get_AboutPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    about = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=about", token = token))["response"])[0]
    about = about["about"]
    #Проверка 
    if about == "":
        about = "Не заполнено"
    #Возврат значения
    return about
    


#Школа пользователя
def get_SchoolPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    schools = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=schools", token = token))["response"])[0]
    schools = schools["schools"]
    #Проверка 
    if schools == []:
        schools = "Не заполнено"
    #Возврат значения
    return schools


#Пол пользователя
def get_SexPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    sex = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=sex", token = token))["response"])[0]
    sex = sex["sex"]
    #Проверка 
    if sex == 1:
        sex = "Женский"
    elif sex == 2:
        sex = "Мужской"
    elif sex == 0:
        sex = "Не заполнено"
    #Возврат значения
    return sex


#Статус пользователя
def get_StatusPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    status = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=status", token = token))["response"])[0]
    status = status["status"]
    #Проверка 
    if status == "":
        status = "Не заполнено"
    #Возврат значения
    return status
        

#День рождения пользователя
def get_BirthdayPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    birthday = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=bdate", token = token))["response"])[0]
    birthday = birthday["bdate"]
    #Проверка
    if birthday== "":
        birthday = "Не заполнено"
    #Возврат значения
    return birthday


#Телефон пользователя
def get_PhonePerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    phone = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=contacts", token = token))["response"])[0]
    phone_1 = phone["mobile_phone"]
    phone_2 = phone["home_phone"]
    #Проверка
    if phone_1 == "" and phone_2 == "":
        phone = "Не заполнено"
    else:
        phone = [phone_1, phone_2]
    #Возврат значения
    return phone

print(get_PhonePerson("https://vk.com/id611672214"))

#Интересы пользователя
def get_InterestsPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    interests = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=interests", token = token))["response"])[0]
    interests = interests["interests"]
    #Проверка 
    if interests == "":
        interests = "Не заполнено"
    #Возврат значения
    return interests


#Фильмы пользователя
def get_MoviesPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    movies = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=movies", token = token))["response"])[0]
    movies = movies["movies"]
    #Проверка 
    if movies == "":
        movies = "Не заполнено"
    #Возврат значения
    return movies


#Музыка пользователя
def get_MusicPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    music = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=music", token = token))["response"])[0]
    music = music["music"]
    #Проверка 
    if music == "":
        music = "Не заполнено"
    #Возврат значения
    return music


#Онлайн пользователя
def get_OnlinePerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    online = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=online", token = token))["response"])[0]
    online = online["online"]
    #Проверка 
    if online == 1:
        online = "Онлайн"
    elif online == 0:
        online == "Оффлайн"
    #Возврат значения
    return online


#Получение групп пользователя
def get_GroupPerson(id_person):
    id_person = check_id(id_person)
    group = ((get_data(method = "groups.get", parameters = "user_id=" + str(id_person) + "&" "count=1000" + "&" , token = token))["response"])["items"]
    return group



#Курение пользователя
def get_SmokingPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    personal = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=personal", token = token))["response"])[0]
    personal = personal["personal"]
    #Проверка 
    smoking = personal["smoking"]
    #Статус алкоголя
    if smoking == 1:
        smoking = "Резко негативное"
    elif smoking == 2:
        smoking = "Негативное"
    elif smoking == 3:
        smoking = "Компромиссное"
    elif smoking == 4:
        smoking = "Нейтральное"
    elif smoking == 5:
        smoking = "Положительное"
    elif smoking == 0:
        smoking = "Не заполнено"
    #Возврат значения
    return smoking


#Алкоголь пользователя
def get_AlcoholPerson(id_person):
    id_person = check_id(id_person)
    #Получение статуса
    personal = ((get_data(method = "users.get", parameters = "user_id=" + str(id_person) + "&fields=personal", token = token))["response"])[0]
    personal = personal["personal"]
    #Проверка 
    alcohol = personal["alcohol"]
    #Статус алкоголя
    if alcohol == 1:
        alcohol = "Резко негативное"
    elif alcohol == 2:
        alcohol = "Негативное"
    elif alcohol == 3:
        alcohol = "Компромиссное"
    elif alcohol == 4:
        alcohol = "Нейтральное"
    elif alcohol == 5:
        alcohol = "Положительное"
    elif alcohol == 0:
        alcohol = "Не заполнено"
    #Возврат значения
    return alcohol
    

#Посмотреть плохие группы у человека
def get_PersonBadGroup(id_person):
    id_person = check_id(id_person)
    #Сборка групп пользователя и плохих групп
    group = get_GroupPerson(id_person = id_person)
    badgroup = open("BadGroup.txt", 'r')
    badgroup = badgroup.read()
    badgroup = badgroup.split(',')
    #Поиск одннаковых значений
    result = []
    for i in group:
        for g in badgroup:
            if str(i) == str(g):
                result.append(i)
    #Возврат значения
    return result


#Колличесвто записей поьзователя
def get_CountWallPerson(id_person):
    id_person = check_id(id_person)
    wall = ((get_data(method = "wall.get", parameters = "owner_id=" + str(id_person) + "&", token = token))["response"])["count"]
    return wall


#Получение стены пользователя(100 штук)
def get_WallPerson(id_person):
    id_person = check_id(id_person)
    count = get_CountWallPerson(id_person)
    #Cбор всей стены
    wall = ((get_data(method = "wall.get", parameters = "owner_id=" + str(id_person) + "&count=100" +"&" , token = token))["response"])["items"]
    #Возврат значений
    return wall


#Получение всех текстов стены
def get_WallTextPerson(id_person):
    id_person = check_id(id_person)
    wall = get_WallPerson(id_person)
    wall_text = []
    for i in wall:
        i = i["text"]
        wall_text.append(i)
    return wall_text


#Получение данных о группе
def get_GroupInfo(id_group):
    #СОН ДЛЯ НОРМАЛЬНОЙ ЗАПИСИ
    sleep(1)
    #Сбор данных
    group = ((get_data(method = "groups.getById", parameters = "group_id=" + str(id_group) + "&", token = token))["response"])[0]
    return group


#Получение имени группы
def get_GroupName(id_group):
    group = get_GroupInfo(id_group)
    name = group["name"]
    return name


#Получение всех групп со стены
def get_WallGroupPerson(id_person):
    wall = get_WallPerson(id_person)
    wall_group = []
    for i in wall:
        for g in i:
            if g == "copy_history":
                group = (i["copy_history"])[0]
                group = int(group["owner_id"]) * -1
                info = get_GroupInfo(id_group = str(group))
                wall_group.append(info)
    return wall_group


#Плохие группы на стене
def get_WallBadGroupPerson(id_person):
    id_person = check_id(id_person)
    #Сбор стены
    wall = get_WallGroupPerson(id_person)
    id_group = []
    badgroup = []
    #Запись id
    for i in wall:
        id_group.append(i["id"])
    #Открытие плохих групп
    file = open("BadGroup.txt", "r")
    file = (file.read()).split(",")
    file.pop(len(file) - 1 )
    #Поиск похожестей
    for i in id_group:
        for g in file:
            if str(i) == str(g):
                badgroup.append(i)
    return badgroup

        
#Личные записи студента
def get_PrivateRecordPerson(id_person):
    id_person = check_id(id_person)
    wall = get_WallPerson(id_person)
    record = []
    for i in wall:
        from_id = i["from_id"]
        owner_id = i["owner_id"]
        print(owner_id)
        if str(from_id) == str(owner_id):
            record.append(i["id"])
    return record



def write_ClassBadGroup(clas, letter):
    #Сам файл
    filename = ""
    #Создание имени файла
    if clas == '1' :
        filename += "1"
    elif clas == "2":
        filename += "2"
    elif clas == "3":
        filename += "3"
    elif clas == "4":
        filename += "4"
    elif clas == "5":
        filename += "5"
    elif clas == "6":
        filename += "6"
    elif clas == "7":
        filename += "7"
    elif clas == "8":
        filename += "8"
    elif clas == "9":
        filename += "9"
    elif clas == "10":
        filename += "10"
    elif clas == "11":
        filename += "11"
    #Добавление буквы
    if letter == 'А':
        filename += "A"
    elif letter ==  'Б':
        filename += "B"
    elif letter ==  "В":
        filename += "V"
    elif letter ==  "Г":
        filename += "G"
    elif letter ==  "Д":
        filename += "D"
    elif letter ==  "Е":
        filename += "E"
    elif letter ==  "Ё":
        filename += "Y"
    elif letter ==  "Ж":
        filename += "J"
    elif letter ==  "З":
        filename += "Z"
    #Добавление расширения
    filename += ".txt"
    #Сам id
    ids = []
    #Открыть класс
    students = open(filename, "r")
    students = students.read()
    students = students.split(",")
    students.pop(len(students) - 1 )
    #Создать файл с плохими студентами
    bs = open("BadStudents_" + str(filename), "w+")
    #Поиск групп в подписках
    for i in students:
        bad = get_PersonBadGroup(id_person = str(i))
        if len(bad) >= 1:
            name = get_NamePerson(id_person = i)
            bs.write(str(name[0]) + " " + str(name[1]) + " " + str(name[2]) + " ")
            bs.write(str(bad))
            bs.write("\n")
    #Поиск групп на стене
    for i in students:
        wall = get_WallBadGroupPerson(id_person = str(i))
        if len(wall) >= 1:
            name = get_NamePerson(id_person = str(i))
            bs.write(str(name[0]) + " " + str(name[1]) + " " + str(name[2]) + " ")
            bs.write(str(bad))
            bs.write("\n")



#Записать группу
def write_BadGroup(adress):
    adress = adress.split("/")
    adress = adress[3]
    #Группа
    group = get_GroupInfo(id_group = adress)
    #Запись группы
    file = open('BadGroup.txt', 'a')
    file.write(str(group["id"]))
    file.write(",")



#Записать ученика
def write_Student(adress, clas, letter):
    filename = ""
    #Поиск id
    if len(adress) >= 10:
        adress = adress.split("/")
        adress = adress[3]
    #Создание имени файла
    if clas == '1' :
        filename += "1"
    elif clas == "2":
        filename += "2"
    elif clas == "3":
        filename += "3"
    elif clas == "4":
        filename += "4"
    elif clas == "5":
        filename += "5"
    elif clas == "6":
        filename += "6"
    elif clas == "7":
        filename += "7"
    elif clas == "8":
        filename += "8"
    elif clas == "9":
        filename += "9"
    elif clas == "10":
        filename += "10"
    elif clas == "11":
        filename += "11"
    #Добавление буквы
    if letter == 'А':
        filename += "A"
    elif letter ==  'Б':
        filename += "B"
    elif letter ==  "В":
        filename += "V"
    elif letter ==  "Г":
        filename += "G"
    elif letter ==  "Д":
        filename += "D"
    elif letter ==  "Е":
        filename += "E"
    elif letter ==  "Ё":
        filename += "Y"
    elif letter ==  "Ж":
        filename += "J"
    elif letter ==  "З":
        filename += "Z"
    #Добавление расширения
    filename += ".txt"
    # Имя
    name = get_NamePerson(id_person = adress)
    #Создание файла
    file = open(filename, "a")
    #Добавление фамилии
    file.write(str(name[2]) + ",")


#Посмотреть учеников определенного класса
def show_Student(clas, letter):
    #Создание имени файла
    if clas == "1":
        filename = "1"
    elif clas == "2":
        filename = "2"
    elif clas == "3":
        filename = "3"
    elif clas == "4":
        filename = "4"
    elif clas == "5":
        filename = "5"
    elif clas == "6":
        filename = "6"
    elif clas == "7":
        filename = "7"
    elif clas == "8":
        filename = "8"
    elif clas == "9":
        filename = "9"
    elif clas == "10":
        filename = "10"
    elif clas == "11":
        filename = "11"
    #Добавление буквы
    if letter == "А":
        filename += "A"
    elif letter ==  "Б":
        filename += "B"
    elif letter ==  "В":
        filename += "V"
    elif letter ==  "Г":
        filename += "G"
    elif letter ==  "Д":
        filename += "D"
    elif letter ==  "Е":
        filename += "E"
    elif letter ==  "Ё":
        filename += "Y"
    elif letter ==  "Ж":
        filename += "J"
    elif letter ==  "З":
        filename += "Z"
    #Добавление расширения
    filename += ".txt"
    #Создание файла
    file = open(filename, "r")
    file = file.read()
    #Разделение
    students = file.split(", ")
    return students


#Показать плохих студентов
def show_BadStudent(clas, letter):
    #Сам файл
    filename = ""
    #Создание имени файла
    if clas == '1' :
        filename += "1"
    elif clas == "2":
        filename += "2"
    elif clas == "3":
        filename += "3"
    elif clas == "4":
        filename += "4"
    elif clas == "5":
        filename += "5"
    elif clas == "6":
        filename += "6"
    elif clas == "7":
        filename += "7"
    elif clas == "8":
        filename += "8"
    elif clas == "9":
        filename += "9"
    elif clas == "10":
        filename += "10"
    elif clas == "11":
        filename += "11"
    #Добавление буквы
    if letter == 'А':
        filename += "A"
    elif letter ==  'Б':
        filename += "B"
    elif letter ==  "В":
        filename += "V"
    elif letter ==  "Г":
        filename += "G"
    elif letter ==  "Д":
        filename += "D"
    elif letter ==  "Е":
        filename += "E"
    elif letter ==  "Ё":
        filename += "Y"
    elif letter ==  "Ж":
        filename += "J"
    elif letter ==  "З":
        filename += "Z"
    #Добавление расширения
    filename += ".txt"
    file = open("BadStudents_" + str(filename), "r")
    file = file.read()
    return file


#Посмотреть плохие группы
def show_BadGroup():
    file = open("BadGroup.txt", "r")
    file = file.read()
    group = file.split(",") 
    return group
