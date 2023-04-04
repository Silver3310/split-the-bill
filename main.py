members = [
    'АлексейЕ',
    'АлексейТ',
    'Бауыржан',
    'Илья',
    'Вадим',
    'Рустам',
    'Виктор',
    'Сергей',
]
indexed_members = {str(i + 1): members[i] for i in range(0, len(members))}
print(
    f"У нас есть {len(members)} участников:",
    '\n'.join([f"{index} - {member}" for index, member in indexed_members.items()]),
    sep='\n'
)
chosen_member_indexes = list(
    input("Введите номера тех участников, для которых хотите подсчитать счёт (слитно без знаков разделения): ")
)
all_member_indexes = list(indexed_members.keys())
for index in all_member_indexes:
    if index not in chosen_member_indexes:
        del indexed_members[index]
print(
    f"Имеем {len(chosen_member_indexes)} участников для расчёта:",
    '\n'.join([f"{index} - {member}" for index, member in indexed_members.items()]),
    sep='\n'
)
all_debts_per_member = {}
total_paid_sum_per_member = {}
for index, member in indexed_members.items():
    all_debts_per_member[index] = {str(index): 0 for index in indexed_members.keys()}
    total_paid_sum_per_member[index] = 0
    print(f"==============={member}===============")
    receipt_number = 1
    have_receipts = True if input(f"Есть ли счета у участника {member}? (y/n)\n") == 'y' else False
    while have_receipts:
        print(f"Счёт #{receipt_number}")
        member_sum = int(input(f"Сколько потратил {member}: "))
        total_paid_sum_per_member[index] += member_sum
        affected_members = list(input(f"Между какими номерами участников разделить данный счёт ({indexed_members}): "))
        sum_each_member_owes = round(member_sum / len(affected_members), 1)
        for debtor in all_debts_per_member[index].keys():
            if debtor in affected_members:
                all_debts_per_member[index][debtor] += sum_each_member_owes
        print(
            f"На данный момент имеем следующее распределение:",
            ', '.join([f"{debtor} - {sum_to_pay}" for debtor, sum_to_pay in all_debts_per_member[index].items()]),
            sep='\n'
        )
        print(f"Всего {member} заплатил {total_paid_sum_per_member[index]}")
        have_receipts = True if input(f"Есть ли ещё счета у участника {member}? (y/n)\n") == 'y' else False
        receipt_number += 1
print("Итого имеем")
members_that_receive = {}
members_that_send = {}
for index, member in indexed_members.items():
    print(f"==============={member}===============")
    print(f"{member} уже заплатил {total_paid_sum_per_member[index]}")
    sum_to_pay = 0
    for member_index, debtors_sums in all_debts_per_member.items():
        sum_to_pay += debtors_sums[index]
    print(f"Всего участник {member} должен {round(sum_to_pay, 1)}")
    diff = round(total_paid_sum_per_member[index] - sum_to_pay, 1)
    print(f"Получаем разницу {diff}")
    if diff > 0:
        members_that_receive[index] = abs(diff)
        print(f"Итого участнику {member} должны {abs(diff)}")
    elif diff < 0:
        members_that_send[index] = abs(diff)
        print(f"Итого участник {member} должен {abs(diff)}")
print("----------АЛГОРИТМ РАСЧЁТА-----------")
for index in members_that_receive.keys():
    for debtor_index in members_that_send.keys():
        if members_that_send[debtor_index] > members_that_receive[index]:
            debtor_sum = members_that_receive[index]
        else:
            debtor_sum = members_that_send[debtor_index]
        if debtor_sum != 0:
            print(f"{indexed_members[debtor_index]} перечисляет {debtor_sum} участнику {indexed_members[index]}")
        members_that_send[debtor_index] = round(members_that_send[debtor_index] - debtor_sum, 1)
        members_that_receive[index] = round(members_that_receive[index] - debtor_sum, 1)
        if members_that_receive[index] <= 1:
            continue
