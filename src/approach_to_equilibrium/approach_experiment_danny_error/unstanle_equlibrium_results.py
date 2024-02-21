from experiment_danny_error import *


def main()
    file_input_unst_eqi_data = "../../../datasets/unstable_equilibrium_data_1.csv"
    file_otput_unst_eqi_data = "../../../datasets/error_unstaible_equlibriun_data_1.csv"
    file_input_unst_eqi_data_2 = "../../../datasets/unstable_equilibrium_data_2.csv"
    file_otput_unst_eqi_data_2 = "../../../datasets/error_unstaible_equlibriun_data_2.csv"
    calculate_save_data(file_name=file_input_unst_eqi_data, num_experiments=1000, stop_after_corresponding=1)
    calculate_error_in_data(file_input_unst_eqi_data, file_otput_unst_eqi_data)
    calculate_save_data(file_name=file_input_unst_eqi_data, num_experiments=100000, stop_after_corresponding=1)
    calculate_error_in_data(file_input_unst_eqi_data_2, file_otput_unst_eqi_data_2)


if __name__ == "__main__":
    main()
