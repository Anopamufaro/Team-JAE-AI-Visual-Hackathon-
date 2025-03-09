import fiftyone as fo

# A name for the dataset
name = "EYEDATASET"

# The directory containing the dataset to import
dataset_dir = "C:\\Users\\Natha\\Documents\\Anopamufaro's Folder\\Hackathons\\AI Hackathon 2025\\Preprocessed images\\"

import pandas as pd

# Define the file path (update this with your actual file path)
file_path = "your_file.csv"  # Replace with your actual CSV file path

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

dataset = fo.Dataset()

samples = []
for index, row in df.iterrows():
    left_file = row['Left-Fundus']
    right_file = row['Right-Fundus']
    left_c = row['Left-Diagnostic Keywords']
    right_c = row['Right-Diagnostic Keywords']
    age = row['Patient Age']
    sex = row['Patient Sex']
    patient_id = row['ID']

    sample1 = fo.Sample(dataset_dir+left_file)
    sample2 = fo.Sample(dataset_dir+right_file)
    sample1["ground_truth"] = fo.Classification(label=left_c)
    sample2["ground_truth"] = fo.Classification(label=left_c)
    sample1["age"] = age
    sample2["age"] = age
    sample1["sex"] = sex
    sample2["sex"] = sex
    sample1["id"] = patient_id
    sample2["id"] = patient_id
    samples.append(sample1)
    samples.append(sample2)

dataset.add_samples(samples)

# Create a dataset from a directory of images
dataset = fo.Dataset.from_images_dir("/path/to/images")

# Create a dataset from a glob pattern of images
dataset = fo.Dataset.from_images_patt("/path/to/images/*.jpg")

session = fo.launch_app(dataset)