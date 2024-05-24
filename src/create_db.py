from flask import Flask
from models import User, Doctor, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        doctor1 = Doctor(firstname='Павел', surname='Гуревичев', midlename='Алексеевич', rang='Главный ветеринарный врач', time='с 2001 года', rang2='Хирургия, Кардиология, Реаниматология, Анестезиология, Интенсивная терапия, Эндоскопия, УЗ – диагностика, Онкология, Стоматология.')
        doctor2 = Doctor(firstname='Мария', surname='Титова', midlename='Вадимовна', rang='Ветеринарный врач', time='с 2019 года', rang2='Нефрология, Гастроэнтерология, Эндокринология, Дерматология, Терапия, Лабораторная диагностика, Общая хирургия.')
        doctor3 = Doctor(firstname='Ксения', surname='Румянцева', midlename='Александровна', rang='Ветеринарный врач', time='с 2001 года', rang2='Терапия, Кардиология, Нефрология, УЗИ, ЭХО - диагностика, Дерматология, Интенсивная терапия.')
        doctor4 = Doctor(firstname='Павел', surname='Лунтовский', midlename='Михайлович', rang='Ветеринарный врач', time='с 2014 года', rang2='Стоматология, Терапия, Общая хирургия, Реаниматология, Анестезиология, Интенсивная терапия.')
        doctor5 = Doctor(firstname='Мария', surname='Дымкова', midlename='Сергеевна', rang='Ветеринарный врач', time='с 2015 года', rang2='Терапия, Нефрология, УЗИ - диагностика, Интенсивная терапия.')
        doctor6 = Doctor(firstname='Николай', surname='Герасимов', midlename='Александрович', rang='Ветеринарный врач', time='с 1998 года', rang2='Терапия, Общая хирургия, Реаниматология, Анестезиология, Интенсивная терапия, Стоматология.')
        doctor7 = Doctor(firstname='Екатерина', surname='Удалова', midlename='Сергеевна', rang='Ветеринарный врач', time='с 2014 года', rang2='Терапия, УЗИ-диагностика, Интенсивная терапия, Дерматология.')
        doctor8 = Doctor(firstname='Александровна', surname='Ефимова', midlename='Александровна', rang='Ветеринарный врач', time='с 2014 года', rang2='Терапия, Офтальмология, Интенсивная терапия.')
        

        db.session.add_all([doctor1,doctor2,doctor3,doctor4,doctor5,doctor6,doctor7,doctor8])
        db.session.commit()
    print('Создана база данных users')
