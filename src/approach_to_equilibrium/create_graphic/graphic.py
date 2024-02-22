# import pandas as pd
# import matplotlib.pyplot as plt

# # Считываем данные из CSV файла
# data = pd.read_csv('../../../datasets/stable_equilibrium_data_1.csv')

# # Построение графика
# plt.figure(figsize=(10, 6))

# for column in data.columns:
#     plt.plot(data.index, data[column], label=f'{column} particles')

# plt.xlabel('Эксперименты')
# plt.ylabel('Количество шагов')
# plt.title('График количества шагов в зависимости от числа экспериментов и частиц')
# plt.legend()
# plt.grid(True)

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

def graphic(file_name, output):
    # Считываем данные из CSV файла
    data = pd.read_csv(filename)

    # Построение графиков
    fig, axs = plt.subplots(3, 1, figsize=(10, 18))

    columns_groups = [data.columns[:2], data.columns[2:4], data.columns[4:6], data.columns[6:]]

    for i, columns in enumerate(columns_groups[:3]):  # Изменено на columns_groups[:3]
        for column in columns:
            axs[i].plot(data.index, data[column], label=f'{column} particles')
        axs[i].set_xlabel('Эксперименты')
        axs[i].set_ylabel('Количество шагов')
        axs[i].set_title(f'График количества шагов для 1000 экспериментов')
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout()
    plt.savefig(output)


if __name__ == "__main__":
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_1_data_1000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_1000_1.png")
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_2_data_1000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_1000_1.png")
    
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_1000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_1000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_1000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_15.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_1000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_15.png")


