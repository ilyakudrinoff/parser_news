import datetime
import sys
import vk_api
import asyncio
import sqlite3

from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from PyQt5 import QtWidgets

from home import Ui_MainWindow
from ist import Ui_IstWindow
from ispoln import Ui_IspolnWindow
from api import Ui_AuthWindow


# pyuic5 myform.ui -o myform.py

# запись в файл
def write_file(cursor, ist, ispol, parser, my_file):
    for text in parser:
        text = text.replace("\n\n", "\n")
        my_file.write("==/СМИ\n01/" +
                      str(cursor.execute(f'select ist.ist from ist where url = \'{ist}\'').fetchone()).strip('[(\')],') +
                      "\n02/" + str(datetime.date.today()) +
                      "\n03/" + str(cursor.execute(f'select ist.reg from ist where url = \'{ist}\'').fetchone()).strip('[(\')],') +
                      "\n07/\n09/" + text[:text.find(".")] + "\n12/" + str(ispol) + "\n06/" + text + "\n" +
                      str(cursor.execute(f'select ist.link from ist where url = \'{ist}\'').fetchone()).strip('[(\')],') +
                      '\n\n')
    return my_file


# "2816958d49c900c83e952a4b1ab5192ce2a86d8d6fc6b695f83f37d4cf9dc767b41121008bc4316428a2b"
# парсинг ВК
def parser_vk(ist, parse_date, token):
    session = vk_api.VkApi(token=token,
                           scope="nohttps")
    posts = session.method("wall.get", {"owner_id": ist, "count": 20})
    posts_list = []
    for post in posts["items"]:
        if datetime.datetime.utcfromtimestamp(post["date"]).strftime("%Y-%m-%d") == parse_date:
            posts_list.append(post["text"])
    return posts_list


# парсинг ТЛГ
async def parser_tlg(ist, parse_date, api_id, api_hash, phone):
    posts_list = []
    api_id = api_id  # 9526621
    api_hash = api_hash  # '3d14cc36425af92b52c7ecf6f3954a7e'
    phone_number = phone  # '89010179912'
    client = TelegramClient('session', api_id, api_hash)
    client = await client.start()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter code: '))
    channel = await client.get_entity(str(ist).strip('[(\')],'))
    posts = await client(GetHistoryRequest(peer=channel, limit=10,
                                               offset_date=datetime.datetime.strptime(parse_date, "%Y-%m-%d"),
                                               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    for post in posts.messages:
        posts_list.append(post.message)
    await client.disconnect()
    return posts_list


# обновление списков для удаления в окнах исполнители и источники
def combo_upd(query, self):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    base = cursor.execute(query).fetchall()
    self.ui.comboBox.clear()
    for i in range(len(base)):
        i = [base[i]]
        i = str(i).strip('[(\')],')
        self.ui.comboBox.addItem(i)


# главное окно
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(datetime.datetime.now().date())
        # self.ui.comboBox.currentTextChanged.connect(self.updateComboBox)
        self.ui.pushButton.clicked.connect(self.parser)
        # кнопка перехода на Источники
        self.ui.pushButton_2.clicked.connect(self.button_clicked2)
        # кнопка перехода на Исполнителей
        self.ui.pushButton_3.clicked.connect(self.button_clicked3)
        # кнопка перехода на АПИ
        self.ui.pushButton_4.clicked.connect(self.button_clicked4)
        # обновление исполнителей в комбобокс
        self.ui.comboBox.clear()
        self.ui.progressBar.setValue(0)
        combo_upd('select auth.name from auth', self)

    # функция перехода для работы с источниками
    def button_clicked2(self):
        self.ui = Ist()
        self.ui.show()
        self.close()

    # функция перехода для работы с исполнителями
    def button_clicked3(self):
        self.ui = Ispoln()
        self.ui.show()
        self.close()

    # функция перехода для работы с АПИ
    def button_clicked4(self):
        self.ui = Api()
        self.ui.show()
        self.close()

    # основная функция по работе парсера
    def parser(self):
        my_file = open(self.ui.lineEdit.text() + '.smi', 'a', encoding='cp1251', errors='replace', newline='')
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        ist_vk = cursor.execute('select ist.url from ist where soc = \'Вконтакте\'').fetchall()
        ist_tlg = cursor.execute('select ist.url from ist where soc = \'Телеграм\'').fetchall()
        token = ", ".join(cursor.execute('select api.token from api').fetchone())
        api_id = ", ".join(cursor.execute('select api.api_id from api').fetchone())
        api_hash = ", ".join(cursor.execute('select api.hash from api').fetchone())
        phone = ", ".join(cursor.execute('select api.phone from api').fetchone())
        self.ui.progressBar.setValue(30)
        self.ui.textBrowser.setText('Источники взяты из базы данных.')
        for ist in ist_tlg:
            ist = ", ".join(ist)
            loop = asyncio.get_event_loop()
            write_file(cursor, ist, self.ui.comboBox.currentText(),
                        loop.run_until_complete(parser_tlg(ist, self.ui.dateEdit.text(), api_id, api_hash, phone)), my_file)
        self.ui.progressBar.setValue(50)
        self.ui.textBrowser.append('Собраны все источники с telegram-каналов.')
        for ist in ist_vk:
            ist = ", ".join(ist)
            write_file(cursor, ist, self.ui.comboBox.currentText(), parser_vk(ist, self.ui.dateEdit.text(), token), my_file)
        self.ui.progressBar.setValue(70)
        self.ui.textBrowser.append('Собраны все источники с Вконтакте.')
        my_file.write('===')
        my_file.close()
        self.ui.progressBar.setValue(100)
        self.ui.textBrowser.append('Сбор СМИ выполнен успешно!')
        conn.close()


class Api(QtWidgets.QMainWindow):
    def __init__(self):  # вызываем окно, определяем переменные
        super(Api, self).__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)
        # кнопка для обновления API
        self.ui.pushButton.clicked.connect(self.upd_api)
        self.ui.pushButton_3.clicked.connect(self.back)

    def back(self):
        self.ui = Main()
        self.ui.show()
        self.close()

    def upd_api(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('update api set token=(?), phone=(?), api_id=(?), hash=(?)', (self.ui.lineEdit_2.text(), self.ui.lineEdit.text(),
                       self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(),))
        conn.commit()
        conn.close()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()


class Ist(QtWidgets.QMainWindow):
    def __init__(self):  # вызываем окно, определяем переменные
        super(Ist, self).__init__()
        self.ui = Ui_IstWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_ist)
        self.ui.pushButton_2.clicked.connect(self.del_ist)
        self.ui.pushButton_3.clicked.connect(self.back)
        combo_upd('select ist.link from ist', self)

    def back(self):
        self.ui = Main()
        self.ui.show()
        self.close()

    def add_ist(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('insert into ist values(?, ?, ?, ?, ?)', (self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                                 self.ui.lineEdit_3.text(),
                                                                 self.ui.comboBox.currentText(),
                                                                 self.ui.comboBox_2.currentText(),))
        conn.commit()
        conn.close()

    def del_ist(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('delete from ist where link = (?)', (self.ui.comboBox.currentText(),))
        conn.commit()
        conn.close()
        combo_upd('select ist.link from ist', self)


class Ispoln(QtWidgets.QMainWindow):
    def __init__(self):  # вызываем окно, определяем переменные
        super(Ispoln, self).__init__()
        self.ui = Ui_IspolnWindow()
        self.ui.setupUi(self)
        # кнопка для добавления исполнителя
        self.ui.pushButton.clicked.connect(self.add_ispoln)
        # кнопка для удаления исполнителя
        self.ui.pushButton_2.clicked.connect(self.del_ispoln)
        self.ui.pushButton_3.clicked.connect(self.back)
        combo_upd('select auth.name from auth', self)

    def back(self):
        self.ui = Main()
        self.ui.show()
        self.close()

    def add_ispoln(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('insert into auth values (?)', (self.ui.lineEdit.text(),))
        conn.commit()
        conn.close()
        self.ui.lineEdit.clear()
        combo_upd('select auth.name from auth', self)

    def del_ispoln(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('delete from auth where name = (?)', (self.ui.comboBox.currentText(),))
        conn.commit()
        conn.close()
        combo_upd('select auth.name from auth', self)


# Открытие первоначального окна
app = QtWidgets.QApplication([])
application = Main()
application.show()
sys.exit(app.exec())
