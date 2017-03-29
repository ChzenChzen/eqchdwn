import pandas as pd

file_name = "input.csv"


def error_message():
    print("First line in input.csv must looks like 'Hand, EV, Equity, Equity Realization, Matchups'")
    print("input.csv must contain only header and data of one player, please check your input.csv")


def slice_data_to_report(from_eq, to_eq, dataframe_name):
    """makes report in format avg realize and range"""

    sorted_dataframe = dataframe_name.sort_values(by=["EqR"],
                                                  ascending=True)  # Sorts dataframe by equity
    # make new dataframe with values between 'from_eq' and 'to_eq' variables.
    sorted_sliced_dataframe = sorted_dataframe[
        (sorted_dataframe["EqR"] > from_eq) & (sorted_dataframe["EqR"] < to_eq)]
    if not sorted_sliced_dataframe.empty:
        # calculate average value of Equity Realization in this slice
        avg_eq_realization = sorted_sliced_dataframe["EqR"].mean()
        cards_range = ""
        for card in sorted_sliced_dataframe["Hand"]:  # do range of cards from slice
            cards_range += card + ","
        # print report
        print("Values between {0!s} and {1!s}. Avg eq: {2:.2f} Range: {3!s}".format(from_eq, to_eq, avg_eq_realization,
                                                                                    cards_range[:-1]))


def output(dataframe_name, pace):
    """Iterates through all data and save final report to txt file"""
    biggest_eq_realization = int(max(dataframe_name["EqR"]))
    steps = range(0, biggest_eq_realization, pace)
    for step in steps:
        slice_data_to_report(step, step + pace, dataframe_name)


def loop():
    """Dialog for enter value of pace"""
    while True:
        try:
            pace = int(input("Enter pace of equity or any string for exit: "))
        except ValueError:
            break

        df = pd.read_csv(file_name, usecols=["Hand", " Equity Realization"])
        df.rename(columns={" Equity Realization": "EqR"}, inplace=True)
        output(df, pace)


try:
    loop()
except ValueError:
    error_message()
