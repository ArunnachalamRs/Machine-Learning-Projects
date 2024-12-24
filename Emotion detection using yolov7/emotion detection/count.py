from roboflow import Roboflow
import supervision as sv

rf = Roboflow(api_key="riMiboxeLKguBWpBlc7J")
project = rf.workspace().project("emotion-detection-project-ooyeo")
model = project.version(1).model

result = model.predict("c.jpg", confidence=20, overlap=20).json()

detections = sv.Detections.from_roboflow(result)

print(len(detections))

# filter by class
detections = detections[detections.class_id == 0]
print(len(detections))