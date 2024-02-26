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
    FOLDER_DATASETS = "../../../datasets/approach_to_equilibrium/"
    OUTPUT_FOLDER = "../../../images/approach_to_equilibrium/"
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_1_1000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_1_1000_1.png")
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_1_10000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_1_10000_1.png")
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_1_100000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_1_100000_1.png")
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_2_1000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_2_1000_1.png")
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_2_10000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_2_10000_1.png")
    create_histogram(FOLDER_DATASETS + "UNST_STEP_script_2_100000_1.csv", OUTPUT_FOLDER + "UNST_STEP_script_2_100000_1.png")
    
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_1000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_1_1000_10.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_10000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_1_10000_10.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_100000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_1_100000_10.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_1000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_2_1000_10.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_10000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_2_10000_10.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_100000_10.csv", OUTPUT_FOLDER + "ST_STEP_script_2_100000_10.png")

    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_1000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_1_1000_15.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_10000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_1_10000_15.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_1_100000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_1_100000_15.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_1000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_2_1000_15.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_10000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_2_10000_15.png")
    create_histogram(FOLDER_DATASETS + "ST_STEP_script_2_100000_15.csv", OUTPUT_FOLDER + "ST_STEP_script_2_100000_15.png")
