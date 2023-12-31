import datetime

about_st = '''https://t.me/st_shoom_krd 
\nЧто у нас есть:
\nЦиклорама размером  6 м на 4 м\nГримерка на 3 места\nСветовое оборудование - 3 импульсных и 4 постоянных источника, лед лампа, закатная лампа, цветные фильтры\n8 бумажных цветных фонов, 4 виниловых, супер фон НЕБО.\nДым машина \nПроектор  \nГардероб
\nСемейные, свадебные съемки\nЛав стори. Детские фотосессии.\nКонтент-съемка. Предметная и для маркетплейсов.
\nЕсть абонементы на съёмки! \n5 ч - 5000 р\n10 ч - 9000 р\n15 ч - 12000 р
\nКупи абонемент, это выгодно!
\nВыберите 1 из следующих услуг:

Студия - 1300/час
Только циклорама - 1100/час
Гримерка - 300/час
Студия + гримерка - 1600/час
Фотограф - 5000/час
Абонемент(на выбор)
'''


contacts = '''
Если есть какие-то дополнительные вопросы, свяжитесь с директором фотостудии ШУМ - https://t.me/kurbanova_marina
'''

optional_services = '''
\nВыберите дополнительную услугу:
\nДым - 500р.\nПроектор - 500p.\nДискошар - 200p.\nЛатексный фон - 200p.\nГардероб - 500p.
'''

text_season = '''
Выберите абонемент:
\n5 часов - 5000р.\n10 часов - 9000р.\n15 часов - 12000р.
'''

payment_text = '''Оплата по номеру телефона 8 918 567 17 47 Марина Александровна сбербанк или тинькофф.\nПосле оплаты отправьте пожалуйста чек для подтверждения - https://t.me/kurbanova_marina и нажмите кнопку - Подтвердить для окончательного оформления услуги.'''

calendar_text = f'''
Календарь записи на {datetime.date.today().month}-й текущий месяц и на следущий {datetime.date.today().month + 1}-й месяц.\nВыберите день, на который планируется съемка.
'''

calendar_text_time = '''
Выберите время съемки.
'''

booking_time_text = '''Введите время на которое вы хотите съемку.\nВводите время в формате - 12:00 - 13:00, 12:30-13:00, 12.00-13.00.\n\n
'''

get_user_full_name = '''
Для подтверждения бронирования введите Фамилию, имя и отчество(по желанию).
'''

get_user_phone_number = '''
И номер телефона для связи с вами, в случае изменений в работе студии.
'''

min_studio_booking_time = 'Минимальное время для записи 30 минут.'
min_booking_time = 'Минимальное время для записи 1 час.'

photograph_info = '''Марина Курбанова.
Фотограф @kurbanova.ph, диплом фотошколы Пикча. Своя фотостудия Шум https://t.me/st_shoom_krd, ставшей постоянной съёмочной площадкой для многих модельных агенств Краснодара. 
Официальный партнер премии года "Я покупаю", "Fashion Show", циркового шоу Гии Эрадзе.
Дипломированный Педагог дополнительного образования по направлениям фотография и мобильная фотография
 
Ссылка на портфолио - https://kurbanova.wfolio.pro/'''

photograph_booking = 'Аренда фотографа происходит только в личных сообщениях. Контакт фотографа - https://t.me/kurbanova_marina'

text_after_payment = """
Убедительная просьба ко всем участникам съёмки, любую обувь заклеить (подошву и каблук) скотчем.
Даже новую и чистую. И при желании взять для себя сменную.
В студии есть тапочки. Но не все желают ими пользоваться.
Можно ходить и без обуви тоже).
Спасибо за понимание)
"""

photos_path = [
        './tg/content/about_st_photo/photo_2023-05-05_22-46-05.jpg',
        './tg/content/about_st_photo/photo_2023-05-08_21-22-51.jpg',
        './tg/content/about_st_photo/photo_2023-05-05_22-46-11.jpg',
        './tg/content/about_st_photo/photo_2023-05-05_22-46-14.jpg'
    ]

video_path = [
        './tg/content/about_st_photo/video_1.mp4',
        './tg/content/about_st_photo/video_2.mp4',
]

price_dict = {
        'Студия': 1300,
        'Студия 30м': 700,
        'Только циклорама': 1100,
        'Только циклорама 30м': 700,
        'Гримерка': 300,
        'Студия и гримерка': 1600,
        'Фотограф': 5000,
        '5 часов': 5000,
        '10 часов': 9000,
        '15 часов': 12000,
        'Дым': 500,
        'Проектор': 500,
        'Диско-шар': 200,
        'Латексный фон': 200,
        'Гардероб': 500
}
