import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F

dataset = foz.load_zoo_dataset("caltech101", max_samples=1000, shuffle=True)

view = dataset.filter_labels("ground_truth", (F("label") == "Motorbikes") | 
                                            (F("label") == "airplanes") |
                                            (F("label") == "Faces") |
                                            (F("label") == "butterfly") |
                                            (F("label") == "sunflower"))

session = fo.launch_app(view)

session.wait()

# Motorbikes, airplanes, Faces, watch, Leopards, chandelier, butterfly, sunflower, kangaroo, laptop