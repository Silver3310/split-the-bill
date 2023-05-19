import re

from typing import List, Dict, TextIO, Tuple

MEMBERS = [
    'АлексейЕ',
    'АлексейТ',
    'Бауыржан',
    'Илья',
    'Вадим',
    'Рустам',
    'Виктор',
    'Сергей',
]


def show_input_data(input_text: TextIO, output_text: TextIO):
    """
    Показать исходные данные
    """
    print("----------ВХОДНЫЕ ДАННЫЕ----------", file=output_text)
    print(input_text.read(), file=output_file)
    input_file.seek(0)
    print("----------------------------------", file=output_text)
    print(file=output_text)


def parse_input_data(input_text: TextIO) -> Dict:
    """
    Показать исходные данные
    """
    data_dict: Dict = dict()
    current_member: str = "-"
    debtors_list: List = list()
    sum_paid: int = 0
    for input_line in input_text.readlines():
        input_line: str = input_line.replace(',', ' ').replace('\n', '')  # заменяем запытые на пробел
        input_line_list: List[str] = re.split(" ", input_line)  # делим по пробелу
        if len(input_line_list) == 1 and input_line_list[0]:  # если строка состоит из одного слова
            current_member = input_line_list[0]  # то помечаем его как текущего участника, для которого введётся счёт
            data_dict[current_member] = dict()  # создаем для него словарь ключ-значение
            continue
        if len(input_line_list) > 1:
            # делаем из превого элемета ключ, 1ый элемент - сумма
            sum_paid = int(input_line_list[0])
            if sum_paid not in data_dict[current_member]:
                # создаём список (для списка участников, полезно, когда у нас два 2 счета с одинаковой суммой, тогда
                # это будет выглядеть так - 350: [[АлексейЕ, Илья], [Сергей, Бауыржан]]. Это считается два счета по 350,
                # но с разными участниками в кажом
                data_dict[current_member][sum_paid]: List = list()
            debtors_list = list()
            for possible_debt_member in input_line_list[1:]:  # идём дальше по строке
                if possible_debt_member in MEMBERS:  # если находим там участников, заносим
                    debtors_list.append(possible_debt_member)
                # если достигли секции с комментариаем, пропускаем до следующей строки
                elif possible_debt_member == '#' or possible_debt_member.startswith('#'):
                    break
                elif possible_debt_member != "":
                    raise Exception("Провертье написание имён всех участников:", possible_debt_member)
        if sum_paid and debtors_list:
            # добавить для текущего участника информацию о том, сколько он заплатил и кто ему должен
            data_dict[current_member][sum_paid].append(debtors_list)
            debtors_list = list()
            sum_paid = 0
    return data_dict


def calculate_debts(members_data_dict: Dict, output_text: TextIO) -> Dict:
    """
    Посчитать долг для каждого участника
    """
    debts_dict: Dict = dict()
    # создаем словать с балансом для каждого участника
    for member in members_data_dict.keys():
        debts_dict[member] = dict()
        debts_dict[member]["+"] = 0  # начальный положительный баланс
        debts_dict[member]["-"] = 0  # начальный отрицательный баланс
    print(
        f"Имеем {len(members_data_dict.keys())} участников для расчёта:",
        ', '.join([f"{member}" for member in members_data_dict.keys()]),
        file=output_text
    )
    print(file=output_text)
    print("------РАСПРЕДЕЛЕНИЕ ДОЛГОВ--------", file=output_text)
    # начинаем рассматривать данные с записями счетов для каждого учасника
    for member, member_dict in members_data_dict.items():
        print(file=output_text)
        print(f"{member}:", file=output_text)
        receipt_index = 1
        # начинаем рассматривать сколько данный участник заплатил и кто ему должен
        for sum_paid, debtors_lists in member_dict.items():
            # на случай, если у нас два счёта с одинаковой суммой, то тут счет записнный как
            # 350: [[АлексейЕ, Илья], [Сергей, Бауыржан]] превратиться в 2 счёта:
            # 350:[АлексейЕ, Илья] и 350:[Сергей, Бауыржан], каждый из которых мы тут отдельно рассмотрим
            for debtors in debtors_lists:
                print(f"Счёт #{receipt_index}: {member} заплатил {sum_paid} за", ", ".join(debtors), file=output_text)
                # помечаем что участник заплатил такую-то сумму
                debts_dict[member]["+"] += sum_paid
                debt_sum = round(sum_paid / len(debtors), 2)  # разделим сумму между участниками
                # каждому должнику эту сумму помечаем в их отрицательном балансе
                for debtor in debtors:
                    debts_dict[debtor]["-"] += debt_sum
                print(f"Всего {member} заплатил {debts_dict[member]['+']}", file=output_text)
                print(
                    f"Всего долгов по участникам:",
                    ', '.join([f"{debtor} - {debts_dict[debtor]['-']}" for debtor in members_data_dict.keys()]),
                    file=output_text
                )
                print("------", file=output_text)
                receipt_index += 1

    return debts_dict


def summarize_debts(members_debts_dict: Dict, output_text: TextIO) -> Tuple[Dict, Dict]:
    """
    Суммировать долг для каждого участника и подвести итоговые суммы
    """
    members_that_send = dict()
    members_that_receive = dict()

    print("-----ПОДВОДИМ ИТОГОВЫЕ СУММЫ------", file=output_text)
    for member, balance in members_debts_dict.items():
        print(f"{member} уже заплатил {balance['+']} и должен {balance['-']}", file=output_text)
        diff = round(balance['+'] - balance['-'], 1)
        print(f"Получаем разницу {diff}", file=output_text)
        if diff > 0:
            members_that_receive[member] = abs(diff)
            print(f"Итого участнику {member} должны {abs(diff)}", file=output_text)
        elif diff < 0:
            members_that_send[member] = abs(diff)
            print(f"Итого участник {member} должен {abs(diff)}", file=output_text)
        print(file=output_text)

    return members_that_send, members_that_receive


def redistribute_debts(senders_dict: Dict, receivers_dict: Dict, output_text: TextIO,):
    """
    Перераспределить расчёт по долгам
    """
    print("--------АЛГОРИТМ РАСЧЁТА----------", file=output_text)
    for receiver in receivers_dict.keys():
        for sender in senders_dict.keys():
            # если сумма отправителя больше чем сумма получателя
            if senders_dict[sender] > receivers_dict[receiver]:
                # то берем наименьшее (сумму получателя)
                debtor_sum = receivers_dict[receiver]
            else:
                # то берем наименьшее (сумму отправителя)
                debtor_sum = senders_dict[sender]
            if debtor_sum != 0:
                print(f"{sender} перечисляет {debtor_sum} участнику {receiver}", file=output_text)
            # вычитаем эту сумму из балансов участников
            senders_dict[sender] = round(senders_dict[sender] - debtor_sum, 1)
            receivers_dict[receiver] = round(receivers_dict[receiver] - debtor_sum, 1)
            # на случай копеек всяких
            if receivers_dict[receiver] <= 1:
                continue


with open("input.txt", mode="r", encoding="utf8") as input_file, \
        open("report.txt", mode="w", encoding="utf8") as output_file:
    show_input_data(input_file, output_file)
    input_data_dict: Dict = parse_input_data(input_file)
    calculated_debts_dict: Dict = calculate_debts(members_data_dict=input_data_dict, output_text=output_file)
    senders, receivers = summarize_debts(members_debts_dict=calculated_debts_dict, output_text=output_file)
    redistribute_debts(senders_dict=senders, receivers_dict=receivers, output_text=output_file)
