import os
import csv


def parse_file(file_path):
    """
    Parse the content of a single file and extract relevant data.

    Args:
        file_path (str): Path to the file to be parsed.

    Returns:
        dict: Extracted data from the file.
    """
    extracted_data = {}
    per_level_time = []
    per_level_hypotheses = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        extracted_data['name'] = file_path.split("\\")[-1].replace(".mhs", "")
        parts = extracted_data['name'].split(".")
        extracted_data['name'] = parts[-2] + "." + parts[-1]
        for line in lines:
            if line.startswith(';;; Matrix size:'):
                mxn_string = line.strip().split(':')[1]
                mxn_string.replace(" ", "")
                mxn_parts = mxn_string.split("x")
                extracted_data['|N|'] = (int(mxn_parts[0]))
                extracted_data['|M|'] = (int(mxn_parts[1]))
                extracted_data['matrix_size'] = extracted_data['|N|'] * extracted_data['|M|']
            elif line.startswith(';;; |M\'|:'):
                line = line.strip().split(': ')[1]
                line = line.replace(" ", "")
                extracted_data['|M1|'] = int(line)
            elif line.startswith(';;; Maximum spatial occupation:'):
                line = line.strip().split(': ')[1]
                line = line.replace(" ", "").replace("KB", "")
                extracted_data['memory_occupation'] = int(line)
            elif line.startswith(';;; Execution time:'):
                line = line.strip().split(': ')[1]
                line = line.replace(" ", "").replace("ms", "")
                extracted_data['execution_time'] = float(line)
            elif line.startswith(';;; Number of explored Hypotheses:'):
                line = line.strip().split(': ')[1]
                line = line.replace(" ", "")
                extracted_data['num_explored_hypotheses'] = int(line)
            elif line.startswith(';;; Number of generated Hypotheses per level:'):
                line = line.strip().split(': ')[1]
                parts = line.split("||")
                for part in parts:
                    part = part.split("->")[1].replace(" ", "")
                    per_level_hypotheses.append(int(part))
                extracted_data['per_level_hypotheses'] = per_level_hypotheses
            elif line.startswith(';;; Time taken at each level:'):
                line = line.strip().split(': ')[1]
                parts = line.split("||")
                for part in parts:
                    part = part.split("->")[1].replace(" ", "").replace("ms", "")
                    per_level_time.append(float(part))
                extracted_data['per_level_time'] = per_level_time
            elif line.startswith(';;; Solutions found:'):
                line = line.strip().split('||')[0].split(':')[1]
                line = line.replace(" ", "")
                extracted_data['num_solutions'] = int(line)

    return extracted_data


def extract_data_from_files(file_list):
    """
    Extract data from a list of files.

    Args:
        file_list (list): List of file paths to be parsed.

    Returns:
        list: List of dictionaries containing extracted data.
    """
    all_data = []
    for file_path in file_list:
        if os.path.getsize(file_path) != 0:
            data = parse_file(file_path)
            data['hypotheses_per_second'] = data['num_explored_hypotheses'] / data['execution_time']
            all_data.append(data)

    return all_data


def write_to_csv(data, output_file):
    """
    Write extracted data to a CSV file.

    Args:
        data (list): List of dictionaries containing extracted data.
        output_file (str): Path to the output CSV file.
    """
    if not data:
        return

    # Get the headers from the first dictionary
    headers = data[0].keys()

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def get_files_from_directory(directory):
    """
    Get all files from the specified directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        list: List of file paths.
    """
    return [os.path.join(directory, file) for file in os.listdir(directory) if
            os.path.isfile(os.path.join(directory, file))]


def main():
    # Directory containing the result files (modify this with your actual directory)
    result_dir = 'permutations'

    # Get list of all files in the result directory
    file_list = get_files_from_directory(result_dir)

    # Extract data from files
    extracted_data = extract_data_from_files(file_list)

    # Output CSV file path (modify this to your desired output file path)
    output_file = 'output_perms.csv'

    # Write extracted data to CSV
    write_to_csv(extracted_data, output_file)
    print(f'Data has been written to {output_file}')


if __name__ == '__main__':
    main()
