from xlrd import open_workbook
from pandas import DataFrame

file_name = "input.xlsx"


def convert_xlsx_to_dataframe(file):
    """grabs data from excel file and return dataframe with two columns (hands, hands_realize)"""

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
    return DataFrame(data)


def realize_report(x, y, dataframe):
    """makes report in format avg realize and range"""

    hands_x_y = dataframe[(dataframe.hands_realize > x) & (dataframe.hands_realize < y)]
    if len(hands_x_y.hands_realize) != 0:
        avg_realize = sum(hands_x_y.hands_realize) / len(hands_x_y.hands_realize)
        cards = ""
        for card in hands_x_y.hands:
            cards = cards + card + ","
        report = "avg: " + str(avg_realize) + " range: " + cards
        return report


def output(dataframe, pace):
    """Iterate through all data and save final report to txt file"""

    output_file_name = "output.txt"
    steps = range(0, max(dataframe.hands_realize), pace)
    with open(output_file_name, 'w') as outfile:
        for step in steps:
            outfile.write(str(realize_report(step, step + pace, dataframe)) + "\n")


df = convert_xlsx_to_dataframe(file_name)
output(df, 10)
