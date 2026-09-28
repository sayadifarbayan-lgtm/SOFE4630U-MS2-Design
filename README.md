# SOFE4630U Milestone 2 - Design

## Overview

This project extends the producer-consumer system developed in Milestone 1 by adding a persistent storage stage between the producer and the consumer.

The architecture is:

Labels.csv
→ producer.py
→ Google Cloud Pub/Sub
→ Application Integration
→ MySQL Connector
→ MySQL Database
→ consumer.py

## Producer

The `producer.py` script reads records from `Labels.csv`, converts the numeric fields to numeric JSON values, and publishes each record to the Google Cloud Pub/Sub topic:

`labelsData`

The published fields are:

- time
- profileName
- temperature
- humidity
- pressure

Missing numeric values are converted to `null`.

## Storage Stage

A Google Cloud Application Integration workflow receives messages from the `labelsData` Pub/Sub topic.

The workflow contains:

- Cloud Pub/Sub Trigger
- Data Mapping
- MySQL Connector

The connector stores each incoming record in the `LabelsData` table in the `Readings` MySQL database.

## Consumer

The `consumer.py` script connects directly to the MySQL database and reads the latest 10 stored records from the `LabelsData` table.

This means the consumer no longer receives messages directly from Pub/Sub. Instead, the data is first stored persistently in MySQL and then retrieved by the consumer.

## MySQL Table

```sql
CREATE TABLE LabelsData (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    time DOUBLE,
    profileName VARCHAR(100),
    temperature DOUBLE,
    humidity DOUBLE,
    pressure DOUBLE
);