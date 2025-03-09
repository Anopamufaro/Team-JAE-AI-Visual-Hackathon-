import fiftyone as fo

# A name for the dataset
name = "EYEDATASET"

# The directory containing the dataset to import
dataset_dir = "C:\\Users\\Natha\\Documents\\Anopamufaro's Folder\\Hackathons\\AI Hackathon 2025\\Preprocessed images\\"

# LOAD IN CSV FILE INTO PANDAS

# ITERATE THROUGH CSV

dataset = fo.Dataset()

samples = []
for row in csv.iterrows():
    left_file
    right_file
    left_c
    right_c
    age
    sex
    patient_id

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

datgaset.add_samples(samples)



# Create a dataset from a directory of images
dataset = fo.Dataset.from_images_dir("/path/to/images")

# Create a dataset from a glob pattern of images
dataset = fo.Dataset.from_images_patt("/path/to/images/*.jpg")

session = fo.launch_app(dataset)