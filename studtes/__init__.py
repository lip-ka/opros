from otree.api import *




class C(BaseConstants):
    NAME_IN_URL = 'studtes'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MULT1 = ['Чтобы оформить пенсию по достижении пенсионного возраста', 'Чтобы устроиться на работу', 'Чтобы пользоваться госуслугами через интернет']
    MULT2 = ['Ее обязан предоставить работодатель', 'На госусугах через интернет', 'Только по письменному заявлению в Социальном фонде России']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #Социально-демографические показатели

    age = models.IntegerField(label="2. Сколько Вам полных лет?", min = 17, max=30)
    gender = models.StringField(label="1. Укажите Ваш пол",
        choices=['женский', 'мужской'],
        widget=widgets.RadioSelect
    )
    q = models.StringField(label="3. В каком городе вы провели большую часть детства?")

    educ_par = models.StringField(label="4. Какой наивысший уровень образования имеют Ваши родители?",
                                choices=['Оба родителя с высшим образованием',
                                         'Один родитель с высшим, другой — нет',
                                         'Оба родителя со средним профессиональным',
                                         'Один родитель со средним профессиональным, другой — нет',
                                         'Оба родителя со средним общим образованием',
                                         'Не знаю / Затрудняюсь ответить'],
                                widget=widgets.RadioSelect
                                )

    q4 = models.StringField(label="5. Какое утверждение наиболее точно описывает финансовое положение Вашей семьи?",
                                choices=['Денег не хватает, чтобы выжить',
                                         'Денег хватает только на еду, покупка одежды требует сбережений',
                                         'Денег хватает на еду и одежду, но покупка бытовой техники требует сбережений',
                                         'Денег хватает на еду, одежду, бытовую технику, но позволить себе квартиру, дачу мы не можем',
                                         'Мы можем позволить себе крупные расходы при первой необходимости'],
                                widget=widgets.RadioSelect
                                )
    # блок 2
    q9 = models.StringField(label= '6. Как Вы относитесь к изменениям в своей жизни?',
                            choices= ["Я их принимаю и адаптируюсь",
                                      "Я предпочитаю стабильность, но могу адаптироваться",
                                      "Я испытываю трудности с изменениями",
                                      "Я испытываю трудности с изменениями"],
                            widget=widgets.RadioSelect)


    q12 = models.StringField(
        label="7. Согласны ли Вы, что увеличить доход практически невозможно?",
        choices=["Да", "Нет"],
        widget=widgets.RadioSelect)

    q14 = models.StringField(
        label="8.Согласны ли Вы с тем что, основная причина низкого дохода – лень?",
        choices=['Да', 'Нет'],
        widget=widgets.RadioSelect
    )

    # --- Шкалы 1-10 ---
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()


    #Финансовая грамотность (3)
    q19 = models.StringField(
        label="19. Представьте, что Вы положили 100 000 рублей на банковский вклад на 2 года под 10% годовых. По условиям договора капитализация процентов отсутствует. Как Вы думаете, сколько денег принесет вклад за второй год: больше, чем в первый год, столько же или меньше?",
        choices=['Больше',
                 'Столько же',
                 'Меньше',
                 'Не знаю'],
        widget=widgets.RadioSelect
    )
    q20 = models.StringField(
        label="20. Какой из годовых депозитов выгоднее для сбережения денег? ",
        choices=['9.5% в конце срока',
                 '9.5% с ежеквартальной капитализацией',
                 '9.5% с ежемесячной капитализацией',
                 'Все одинаковы'
        ],
        widget=widgets.RadioSelect
    )
    q21 = models.StringField(
        label="21. Как Вы считаете, верно ли утверждение, что обычно покупка акций одной компании обеспечивает большую надежность вложения, чем покупка доли в паевом инвестиционном фонде? ",
        choices=['Да',
            'Нет',
            'Не знаю, что такое паевый инвестиционный фонд'
        ],
        widget=widgets.RadioSelect
    )
    q22 = models.StringField(
        label="22. Еврооблигации — это:",
        choices=[
            (1, 'Облигации в евро'),
            (2, 'Облигации, выпущенные европейскими государствами или компаниями'),
            (3, 'Облигации, выпущенные в иностранной для эмитента валюте'),
            (4, 'Не знаю')
        ],
        widget=widgets.RadioSelect
    )
    q23 = models.StringField(
        label="23. Какая ставка рефинансирования в настоящий момент? ",
        choices=['8-10%',
                 '11-13%',
                 '14-16%',
                 '17-21%',
                 'Свыше 22%',
                 'Не слежу',
                 'Не знаю, что это'
        ],
        widget=widgets.RadioSelect
    )
    q24 = models.StringField(
        label="24. Сколько составляла ставка рефинансирования в декабре 2023 года? ",
        choices=['8-10%',
                 '11-13%',
                 '14-16%',
                 '17-21%',
                 'Свыше 22%',
                 'Не слежу',
                 'Не знаю, что это'
                 ],
        widget=widgets.RadioSelect
    )

    q25 = models.StringField(
        label="25. Знаете ли вы, что такое ИИС?",
        choices=['Да', 'Нет'],
        widget=widgets.RadioSelect
    )
    q26 = models.StringField(
        label="26. Имеете ли вы опыт инвестирования в финансовые инструменты (например, акции, облигации), фонды (ПИФы, ETF), банковские вклады или другие виды вложений?",
        choices=['Да', 'Нет'],
        widget=widgets.RadioSelect
    )

    q27 = models.IntegerField()

    # Пенсионная осведомленность (4)


    q29 = models.StringField(
        label="28. Когда человек может выйти на пенсию?",
        choices=['Человек вправе самостоятельно решать, когда ему начать получать страховую пенсию',
                 'Женщины – с 60 лет, мужчины – с 65 лет',
                 'Женщины – с 60 лет, мужчины – с 65 лет, если соблюдены условия по стажу и пенсионным коэффициентам'],
        widget=widgets.RadioSelect
    )

    q30 = models.StringField(
        label="29. Какой минимальный рабочий стаж требуется для получения страховой пенсии?",
        choices=['1 год', '11 лет', '15 лет', '25 лет'],
        widget=widgets.RadioSelect
    )
    q31 = models.StringField(
        label="30. Что такое страховые взносы?",
        choices=['Средства, которые обязательно перечисляет работодатель за своего работника или самозанятые граждане сами за себя в Социальный фонд России',
                 'Выплаты, совершаемые на усмотрение гражданина в добровольном порядке и по специальному договору с Социальном фондом России'],
        widget=widgets.RadioSelect
    )
    q32 = models.StringField(
        label="31. Какой процент от страховых взносов идет на пенсионные отчисления?",
        choices=['0,1', '0,13', '0,22'],
        widget=widgets.RadioSelect
    )

    q48 = models.StringField(
        label="32. Как Вам кажется, кто должен заботиться о том, чтобы у человека было достаточно средств для поддержания достойного уровня жизни на пенсии: скорее государство или скорее сам человек?",
        choices=['Только государство', 'В большей степени государство'
            , 'В большей степени сам человек', 'Только человек'],
        widget=widgets.RadioSelect
    )

    q50 = models.StringField(
        label="33. Как часто Вы думаете о своем выходе на пенсию?",
        choices=['Много', 'Иногда', 'Немного', 'Совсем не думаю'],
        widget=widgets.RadioSelect
    )

    q51 = models.StringField(
        label="34. Если бы Вы могли выбирать, в каком возрасте Вы бы хотели выйти на пенсию?",
        choices=['30-40 лет',
                 '40-50 лет',
                 '50-60 лет',
                 '60-70 лет',
                 'После 70 лет'],
        widget=widgets.RadioSelect
    )

    q70 = models.StringField(
        label="35. Задумывались ли Вы из чего будет формироваться Ваша пенсия?",
        choices=['Да', 'Нет'],
        widget=widgets.RadioSelect
    )

    #Блок восприятие отдаленности дня выхода на пенсию (5)
    q38 = models.IntegerField()
    q39 = models.IntegerField()
    q40 = models.IntegerField()
    q41 = models.IntegerField()
    q42 = models.IntegerField()
    q43 = models.IntegerField()
    q44 = models.IntegerField()
    q45 = models.IntegerField()
    q46 = models.IntegerField()
    q47 = models.IntegerField()

    q55_1 = models.StringField(
        choices= ['Ц', 'Г'],
        label="Выберите букву",
        blank=False
    )

    q55_2 = models.StringField(
        choices=['Г', 'Ц'],
        label="Выберите букву",
        blank=False
    )


def set_payoffs(group):
    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)



#  PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age',  'q','educ_par', 'q4']

class Page2(Page):
    form_model = 'player'
    form_fields = ['q9', 'q12', 'q14', 'q15', 'q16', 'q17', 'q18']


class Page3(Page):
    form_model = "player"
    form_fields = ['q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27']

class Page4(Page):
    form_model = "player"
    form_fields = ['q29', 'q30', 'q31', 'q32', 'q48',  'q50', 'q51', 'q70']


class Page5_1(Page):
    form_model = "player"
    form_fields = ['q38', 'q40', 'q41', 'q42', 'q43']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group % 2 == 0

    @staticmethod
    def vars_for_template(player):
        # Получаем возраст и пол из предыдущих ответов
        age = player.age
        gender = player.gender

        # Вычисляем X
        if gender == 'мужской':
            x = 65 - age
        else:
            x = 60 - age

        # Передаем X в шаблон
        return {'x': x}

class Page5_2(Page):
    form_model = "player"
    form_fields = ['q39', 'q44', 'q45', 'q46', 'q47']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group % 2 == 1

class Page6(Page):
    form_model = "player"
    form_fields = ['q55_1', 'q55_2']

    def error_message(self, values):
        # Проверка правильности ответов
        if values['q55_1'].upper() == values['q55_2'].upper():
            errors = "В 13 вопросе в верхней и нижней клетке значения не должны повторяться"
            return errors

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    MyPage,    # сначала сбор familyname
    Page2,     # затем другие страницы
    Page6,
    Page5_2,   # страницы с условиями
    Page5_1,
    Page3,
    Page4,
    Results
]

