# This export works, need to filter by top labels

# Training this dataset with Teachable Machine works fine, but I'm not too
# happy with the categories.

# Art media dataset works fine, but might need some prunning -- lots of pictures
#Same for WikiArt

import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F

dataset = foz.load_zoo_dataset("caltech101", max_samples=1000, shuffle=True)

export_dir = "caltech101_dataset/"
label_field = "ground_truth"  # for example

view = dataset.filter_labels("ground_truth", (F("label") == "Motorbikes") | 
                                            (F("label") == "airplanes") |
                                            (F("label") == "Faces") |
                                            (F("label") == "butterfly") |
                                            (F("label") == "sunflower"))

# view = dataset.filter_labels("ground_truth", (F("label") == "Motorbikes") | 
#                                             (F("label") == "airplanes") |
#                                             (F("label") == "Faces") |
#                                             (F("label") == "watch") |
#                                             (F("label") == "Leopards") |
#                                             (F("label") == "chandelier") |
#                                             (F("label") == "butterfly") |
#                                             (F("label") == "sunflower") |
#                                             (F("label") == "kangaroo") |
#                                             (F("label") == "laptop") |
#                                             (F("label") == "BACKGROUND_Google"))

# Export the dataset
view.export(
    export_dir=export_dir,
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    label_field=label_field
)