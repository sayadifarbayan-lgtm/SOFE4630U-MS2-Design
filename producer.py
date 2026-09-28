import os
import glob
import csv
import json
from google.cloud import pubsub_v1

files = glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = files[0]

project_id = "sofe4630-ms2-bayan"
topic_id = "labelsData"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

with open("Labels.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["time"] = float(row["time"])
        row["temperature"] = float(row["temperature"])
        row["humidity"] = float(row["humidity"])
        row["pressure"] = float(row["pressure"])

        future = publisher.publish(topic_path, message)
        future.result()

        print(f"Published: {row}")

print("All records were published successfully.")
