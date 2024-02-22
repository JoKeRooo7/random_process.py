import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from script_1 import create_box as create_box_one
from script_2 import create_box as create_box_two
from script_errors import create_dataset, calculate_error_data


FOLDER = "../../../datasets/approach_to_equilibrium/"


def calc_step_err(folder, step_file_input):
    error_output = folder + "RES_ERR_" + step_file_input
    calculate_error_data(folder + step_file_input, error_output)


def calculate_script_one_stable_eq_dataset(folder, num_experiments, stop_after_corresponding):
    step_file_input = f"ST_STEP_script_1_{num_experiments}_{stop_after_corresponding}.csv"
    time_file_input = f"ST_script_1_{num_experiments}_{stop_after_corresponding}.csv"

    create_dataset(create_box_one, folder + step_file_input, folder+time_file_input, num_experiments, stop_after_corresponding)
    calc_step_err(folder, step_file_input)


def caclulate_script_two_sstable_eq_dataset(folder, num_experiments, stop_after_corresponding)
    step_file_input = f"ST_STEP_script_2_{num_experiments}_{stop_after_corresponding}.csv"
    time_file_input = f"ST_script_2_{num_experiments}_{stop_after_corresponding}.csv"

    create_dataset(create_box_one, folder + step_file_input, folder+time_file_input, num_experiments, stop_after_corresponding)
    calc_step_err(folder, step_file_input)
    

if __name__ == "__main__":
    calculate_script_one_stable_eq_dataset(FOLDER, 1000, 10)
    calculate_script_one_stable_eq_dataset(FOLDER, 1000, 15)
    calculate_script_one_stable_eq_dataset(FOLDER, 10000, 10)
    calculate_script_one_stable_eq_dataset(FOLDER, 10000, 15)
    calculate_script_one_stable_eq_dataset(FOLDER, 100000, 10)
    calculate_script_one_stable_eq_dataset(FOLDER, 100000, 15)
    calculate_script_two_stable_eq_dataset(FOLDER, 1000, 10)
    calculate_script_two_stable_eq_dataset(FOLDER, 1000, 15)
    calculate_script_two_stable_eq_dataset(FOLDER, 10000, 10)
    calculate_script_two_stable_eq_dataset(FOLDER, 10000, 15)
    calculate_script_two_stable_eq_dataset(FOLDER, 100000, 10)
    calculate_script_two_stable_eq_dataset(FOLDER, 100000, 15)
    
