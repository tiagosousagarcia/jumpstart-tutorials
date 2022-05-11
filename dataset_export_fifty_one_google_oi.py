import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("open-images-v6", split="validation", max_samples=500, shuffle=True, label_types="classifications")

export_dir = "dataset/"
label_field = "positive_labels"  # for example

# Export the dataset
dataset.export(
    export_dir=export_dir,
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    label_field=label_field
)