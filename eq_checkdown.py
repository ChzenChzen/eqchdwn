import pandas as pd

file_name = "input.csv"


def error_message():
    print("First line in input.csv must looks like 'Hand, EV, Equity, Equity Realization, Matchups'")
    print("input.csv must contain only header and data of one player, please check your input.csv")


def slice_data_to_report(from_eq, to_eq, dataframe_name):
    """makes report in format avg realize and range"""
    sliced_dataframe = dataframe_name[from_eq:to_eq]  # make new dataframe with values of Equity Realization
    if not sliced_dataframe.empty:
        avg_eq_realization = sum(sliced_dataframe[" Equity Realization"]) / len(
            sliced_dataframe[" Equity Realization"])  # calculate average value of Equity Realization in this slice
        cards_range = ""
        for card in sliced_dataframe["Hand"]:  # do range of cards from slice
            cards_range = cards_range + card + ","
        print("Values between {0!s} and {1!s}. Avg eq: {2:.2f} Range: {3!s}".format(from_eq, to_eq, avg_eq_realization,
                                                                                    cards_range[:-1]))


def output(dataframe_name, pace):
    """Iterates through all data and save final report to txt file"""
    output_file_name = "output.txt"
    biggest_eq_realization = int(max(dataframe_name[" Equity Realization"]))
    steps = range(0, biggest_eq_realization, pace)
    with open(output_file_name, 'w') as outfile:
        for step in steps:
            outfile.write(str(slice_data_to_report(step, step + pace, dataframe_name)) + "\n")


def loop():
    """Dialog for enter value of pace"""
    while True:
        try:
            pace = int(input("Enter pace of equity or any string for exit: "))
        except ValueError:
            break

        df = pd.read_csv(file_name, usecols=["Hand", " Equity Realization"])
        output(df, pace)


try:
    loop()
except ValueError:
    error_message()
