import pandas as pd
import matplotlib.pyplot as plt


def create_histogram(file_name, output):

    data = pd.read_csv(file_name)

    # Создаем общий график с 6 подграфиками
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    # Проходимся по каждой колонке и строим гистограмму на соответствующем подграфике
    for i, column in enumerate(data.columns):
        ax = axs[i // 3, i % 3]  # Получаем нужный подграфик
        ax.hist(data[column], bins=100, alpha=0.5)
        ax.set_xlabel('Количество шагов')
        ax.set_ylabel('Частота')
        ax.set_title(f'Гистограмма количества шагов для {column}')

    # Добавляем расстояние между графиками
    plt.tight_layout()

    plt.savefig(output)


if __name__ == "__main__":
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_1_data_1000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_1000_1.png")
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_1_data_100000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_100000_1.png")
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_2_data_1000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_1000_1.png")
    create_histogram("../../../datasets/approach_to_equilibrium/UN-script_2_data_100000_1.csv",
                     "../../../image/approach_to_equilibrium/HIST-UN-script_1_data_100000_1.png")
    
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_1000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_100000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_100000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_1000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_100000_10.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_100000_10.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_1000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_15.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_1_data_100000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_100000_15.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_1000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_1000_15.png")
    create_histogram("../../../datasets/approach_to_equilibrium/ST-script_2_data_100000_15.csv",
                     "../../../image/approach_to_equilibrium/HIST-ST-script_1_data_100000_15.png")


