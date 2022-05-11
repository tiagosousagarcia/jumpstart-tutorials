import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("open-images-v6", \
    split="validation", max_samples=500, shuffle=True, label_types=["classifications"])

print(dataset.list_view_stages())
view = dataset.limit_labels("positive_labels", 1)

session = fo.launch_app(view)

session.wait()