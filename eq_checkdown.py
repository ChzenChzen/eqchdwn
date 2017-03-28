from xlrd import open_workbook
import pandas as pd

file_name = "input.xlsx"


def convert_xlsx_to_dataframe(file):
    hands_realize_list = []
    hands_list = []
    data = {}

    book = open_workbook(file)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        if row != '':
            hand = sheet.cell_value(row, colx=0)
            if isinstance(hand, float):
                hand = round(hand)
            hand_realize_value = float(sheet.cell_value(row, colx=3))
            hands_list.append(str(hand))
            hands_realize_list.append(round(hand_realize_value))
            data['hands'] = hands_list
            data['hands_realize'] = hands_realize_list
    return pd.DataFrame(data)


def realize_report(x, y, dataframe):
    hands_x_y = dataframe[(dataframe.hands_realize > x) & (dataframe.hands_realize < y)]
    avg_realize = sum(hands_x_y.hands_realize) / len(hands_x_y.hands_realize)
    cards = ""
    for card in hands_x_y.hands:
        cards = cards + card + ","
    report = "avg: " + str(avg_realize) + " range: " + cards
    return report

df = convert_xlsx_to_dataframe(file_name)

print(df)
steps = range(0, len(df.hands) - 1)
print(steps)

for step in steps:
    print()

# print(realize_report(0, 10, df))

# with open("output.txt", 'w') as f_obj:
#     f_obj.write(cards_ranges)
