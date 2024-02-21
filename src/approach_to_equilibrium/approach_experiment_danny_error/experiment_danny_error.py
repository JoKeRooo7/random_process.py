import csv
import pandas as pd
import numpy as np

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from approach_to_equilibrium import Box, BoxApp, create_box

def calculate_save_data(file_name, num_experiments=100000, stop_after_corresponding=3):
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
            my_box_8 = create_box(8, stop_after_corresponding)
            my_box_16 = create_box(16, stop_after_corresponding)
            my_box_64 = create_box(64, stop_after_corresponding)
            my_box_400 = create_box(400, stop_after_corresponding)
            my_box_800 = create_box(800, stop_after_corresponding)
            my_box_3600 = create_box(3600, stop_after_corresponding)

            writer.writerow([
                len(my_box_8.history_left_particles),
                len(my_box_16.history_left_particles),
                len(my_box_64.history_left_particles),
                len(my_box_400.history_left_particles),
                len(my_box_800.history_left_particles),
                len(my_box_3600.history_left_particles),
            ])

# если данные нормально распределены
# def calculate_uncertainty(data):
#     std_deviation = data.std()  # Стандартное отклонение
#     std_error = std_deviation / np.sqrt(len(data))  # Стандартная ошибка среднего
#     confidence_interval = 1.96 * std_error  # Доверительный интервал (95%)
#     return data.mean(), std_deviation, std_error, confidence_interval


# def calculate_error_in_data(input_file_name, output_file_name):
#     df = pd.read_csv(input_file_name)

#     results = []
#     for column in df.columns:
#         mean_value, std_deviation, std_error, confidence_interval = calculate_uncertainty(df[column])
#         results.append([column, mean_value,  std_deviation, std_error , confidence_interval])

#     result_df = pd.DataFrame(results, columns=['particles', 'mean_value', 'Std Deviation', 'Std Error', 'Confidence Interval'])
#     result_df.to_csv(output_file_name, index=False)

def calculate_bootstrap_error(data, statistic, iterations=1000, confidence_level=0.95):
    boot_statistics = np.zeros(iterations)
    for i in range(iterations):
        boot_sample = np.random.choice(data, size=len(data), replace=True)
        boot_statistics[i] = statistic(boot_sample)
    alpha = (1 - confidence_level) / 2
    # перцентиль - значение которое не превышает с заданной вероятностью
    lower_bound = np.percentile(boot_statistics, 100 * alpha)
    upper_bound = np.percentile(boot_statistics, 100 * (1 - alpha))
    return lower_bound, upper_bound

def calculate_error_in_data(input_file_name, output_file_name):
    df = pd.read_csv(input_file_name)

    results = []
    for column in df.columns:
        data = df[column].values
        lower_bound, upper_bound = calculate_bootstrap_error(data, np.mean)
        std_deviation = np.std(data)
        std_error = std_deviation / np.sqrt(len(data))
        results.append([column, np.mean(data), std_deviation, std_error, lower_bound, upper_bound])

    result_df = pd.DataFrame(results, columns=['particles', 'mean_value', 'Std Deviation', 'Std Error', 'Lower CI', 'Upper CI'])
    result_df.to_csv(output_file_name, index=False)
