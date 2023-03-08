import csv
from pprint import pprint
from sqlalchemy.orm import sessionmaker, Session
from models.models import SportsObjects
from database.config import SessionLocal

FIELDS_NAMES = [
    'id:', 'Название:', 'Название (in english):', 'Активный:', 'Краткое описание:', 'Детальное описание:',
    'Краткое описание (in english):', 'Детальное описание (in english):', 'МО:', 'Субъект федерации:', 'Значимость:',
    'Населённый пункт:', 'Населённый пункт (in english):', 'Адрес:', 'Адрес (in english):', 'ОКТМО:',
    'ФЦП (федеральная целевая программа):', 'Действия с объектом:', 'Дата начала строительства / реконструкции:',
    'Дата завершения строительства / реконструкции:', 'Общий объём финансирования:',
    'Финансирование из федерального бюджета:', 'Финансирование из федерального бюджета (из них освоено):',
    'Финансирование из бюджета субъекта федерации:', 'Финансирование из бюджета субъекта федерации (из них освоено):',
    'Финансирование из бюджета муниципального образования:',
    'Финансирование из бюджета муниципального образования (из них освоено):',
    'Финансирование из внебюджетных источников:', 'Финансирование из внебюджетных источников (из них освоено):',
    'Ключевой или нет?:', 'Курирующий орган:', 'Курирующий орган (in english):', 'Адрес курирующего органа:',
    'Адрес курирующего органа (in english):', 'Телефон курирующего органа:', 'Контактный телефон объекта:',
    'Режим работы Пн.-Пт.:', 'Режим работы Сб.:', 'Режим работы Вс.:', 'Площадь:', 'E-mail:', 'URL сайта:',
    'Внесён в реестр?:', 'Тип спортивного комплекса:', 'Какие соревнования проводятся?:', 'Виды спорта:',
    'Яндекс координата объекта X:', 'Яндекс координата объекта Y:', 'Маштаб Яндекс-карты:',
    'Яндекс координата центра X:', 'Яндекс координата центра Y:', 'Мини координата X:', 'Мини координата Y:',
    'Генеральный план:', 'Дополнительные планы:', 'Фото:', 'URL фото галереи объекта:', 'Видео:', 'Панорамы:',
    'Web-трансляции:', 'Прочие материалы:'
]


def to_db(path: str ,db: Session):

    with open(path, encoding='Windows-1251') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDS_NAMES, delimiter=';')

        next(reader)
        for i, row in enumerate(reader):
            new_object = SportsObjects(name=row['Название:'],
                                       is_active=True if row['Активный:'] == 'Y' else False,
                                       description=row['Детальное описание:'],
                                       short_description=row['Краткое описание:'],
                                       m_o=row['МО:'],
                                       subject=row['Субъект федерации:'],
                                       locality=row['Населённый пункт:'],
                                       address=row['Адрес:'],
                                       oktmo=row['ОКТМО:'],
                                       fcp=row['ФЦП (федеральная целевая программа):'],
                                       action_on_object=row['Действия с объектом:'],
                                       date_start_action=row['Дата начала строительства / реконструкции:'],
                                       date_end_action=row['Дата завершения строительства / реконструкции:'],
                                       total_funding=float(row['Общий объём финансирования:']) if row['Общий объём финансирования:'] else 0 ,
                                       federal_financing=float(row['Финансирование из федерального бюджета:'] if row['Финансирование из федерального бюджета:'] else 0),
                                       financing_from_subject=float(row['Финансирование из бюджета субъекта федерации:']) if row['Финансирование из бюджета субъекта федерации:'] else 0,
                                       financing_from_municipality=float(row['Финансирование из бюджета муниципального образования:']) if row['Финансирование из бюджета муниципального образования:'] else 0,
                                       financing_from_extrabudgetary=float(row['Финансирование из внебюджетных источников:']) if row['Финансирование из внебюджетных источников:'] else 0,
                                       supervising_body=row['Курирующий орган:'] if row['Курирующий орган:'] else None,
                                       supervisor_phone=row['Телефон курирующего органа:'] if row['Телефон курирующего органа:'] else None,
                                       object_contact_phone=row['Контактный телефон объекта:'] if row['Контактный телефон объекта:'] else None,
                                       working_mode_mn_fr=row['Режим работы Пн.-Пт.:'] if row['Режим работы Пн.-Пт.:'] else None,
                                       working_mode_st=row['Режим работы Сб.:'] if row['Режим работы Сб.:'] else None,
                                       working_mode_sn=row['Режим работы Вс.:'] if row['Режим работы Вс.:'] else None,
                                       area=row['Площадь:'] if row['Площадь:'] else None,
                                       email=row['E-mail:'] if row['E-mail:'] else None,
                                       site_url=row['URL сайта:'] if row['URL сайта:'] else None,
                                       registry=True if row['Внесён в реестр?:'] else None,
                                       sport_type=row['Тип спортивного комплекса:'] if row['Тип спортивного комплекса:'] else None,
                                       type_of_competition=row['Какие соревнования проводятся?:'] if row['Какие соревнования проводятся?:'] else None,
                                       yandex_maps_x=float(row['Яндекс координата объекта X:']) if row['Яндекс координата объекта X:'] else None,
                                       yandex_maps_y=float(row['Яндекс координата объекта Y:']) if row['Яндекс координата объекта Y:'] else None,
                                       yandex_maps_scale=int(row['Маштаб Яндекс-карты:']) if row['Маштаб Яндекс-карты:'] else None,
                                       yandex_maps_x_center=float(row['Яндекс координата центра X:']) if row['Яндекс координата центра X:'] else None,
                                       yandex_maps_y_center=float(row['Яндекс координата центра Y:']) if row['Яндекс координата центра Y:'] else None,
                                       mini_coordinate_x=float(row['Мини координата X:']) if row['Мини координата X:'] else None,
                                       mini_coordinate_y=float(row['Мини координата Y:']) if row['Мини координата Y:'] else None)
            db.add(new_object)
            print(f'{i} Done')
            db.commit()

        db.close()
