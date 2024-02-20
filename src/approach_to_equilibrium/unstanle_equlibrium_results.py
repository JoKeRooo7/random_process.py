import csv
import pandas as pd
import numpy as np
from approach_to_equilibrium import Box, BoxApp, create_box

def calculate_save_data(file_name, num_experiments=100000):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            '8 particles', 
            '16 particles',
            '64 particles',
            '400 particles',
            '800 particles',
            '3600 particles'])

        for _ in range(num_experiments):
            my_box_8 = create_box(8, 1)
            my_box_16 = create_box(16, 1)
            my_box_64 = create_box(64, 1)
            my_box_400 = create_box(400, 1)
            my_box_800 = create_box(800, 1)
            my_box_3600 = create_box(3600, 1)

            writer.writerow([
                len(my_box_8.history_left_particles),
                len(my_box_16.history_left_particles),
                len(my_box_64.history_left_particles),
                len(my_box_400.history_left_particles),
                len(my_box_800.history_left_particles),
                len(my_box_3600.history_left_particles),
            ])

def calculate_uncertainty(data):
    std_deviation = data.std()  # Стандартное отклонение
    std_error = std_deviation / np.sqrt(len(data))  # Стандартная ошибка среднего
    confidence_interval = 1.96 * std_error  # Доверительный интервал (95%)
    return data.mean(), std_deviation, std_error, confidence_interval


def calculate_error_in_data(input_file_name, output_file_name):
    df = pd.read_csv(input_file_name)

    results = []
    for column in df.columns:
        mean_value, std_deviation, std_error, confidence_interval = calculate_uncertainty(df[column])
        results.append([column, mean_value,  std_deviation, std_error , confidence_interval])

    result_df = pd.DataFrame(results, columns=['particles', 'mean_value', 'Std Deviation', 'Std Error', 'Confidence Interval'])
    result_df.to_csv(output_file_name, index=False)

if __name__ == "__main__":
    file_input_unst_eqi_data = "../../datasets/unstable_equilibrium_data_2.csv"
    file_otput_unst_eqi_data = "../../datasets/error_unstaible_equlibriun_data_2.csv"
    # calculate_save_data(file_name=file_input_unst_eqi_data)
    # calculate_error_in_data(file_input_unst_eqi_data, file_otput_unst_eqi_data)

    