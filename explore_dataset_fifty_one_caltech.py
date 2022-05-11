import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("caltech101", max_samples=500, shuffle=True)

session = fo.launch_app(dataset)

session.wait()