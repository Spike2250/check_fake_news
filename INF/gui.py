import PySimpleGUI as sg


def create_layout():
    # что будет внутри окна
    layout = [
        [sg.Button(
            'Создать модель',
            enable_events=True,
            key='-CREATE MODEL-',
            font='Roboto 14'
        ),
        sg.Text(
            '',
            key='-MODEL INFO-',
            font='Roboto 12'
        )],
        [sg.Multiline(
            '',
            size=(550, 350),
            key='-TEXT-',
            finalize=True,
            font='Roboto 10'
        )],
        [sg.Button(
            'Проверить новость',
            enable_events=True,
            key='-CHECK NEWS-',
            font='Roboto 14'
        )],
        [sg.Text(
            '',
            key='-RESULT-',
            font='Roboto 12'
        )],

    ]
    return layout


def main():
    # рисуем окно
    window = sg.Window(
        'Проверка новостей',
        create_layout(),
        size=(600, 800)
    )
    # запускаем основной бесконечный цикл
    while True:
        # получаем события, произошедшие в окне
        event, values = window.read()
        # если нажали на крестик
        if event in (sg.WIN_CLOSED, 'Exit'):
            # выходим из цикла
            break
    # закрываем окно и освобождаем используемые ресурсы
    window.close()


if __name__ == '__main__':
    main()
