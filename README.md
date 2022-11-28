# DataDay

<a href="https://gitpod.io/#https://github.com/rickdat/DataDay-Producer">
  <img
    src="https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod"
    alt="Launch on Gitpod"
  />
</a>

## Summary
This Workshop POCs a Log Management and Threat Detection Platform on Astra DB and Astra Streaming. This small application collects logs fm multiple servers, performs analytics on them and  generates alerts based on malware signatures that match an Indicator of compromise. 

## The application has the following components:

**A logs shipper:** collects logs from multiple servers using their “syslog” file and sends them to Astra Streaming.

**A Pulsar Topic:** receives the logs from multiple sources, applies transformations and inserts into a database.

**Astra DB:** a low latency, distributed and fault-tolerant datastore for real-time reads and writes.

**Data Analyzer:** a simple correlation engine created in Python using Pandas.

## Deployment Steps
Please follow the steps in order.

### Step One: Create an Astra Database and Streaming tenant
**Create an Astra Database**
- Visit https://astra.datastax.com/ and create an account.
- Click on "Databases" and then "Create Database". For this POC, your database should be on "Google Cloud" and the "us-central1" region. Your keyspace should be called "logs"
- Once database is created, copy the "token" value. Then click on "Go to database"
- Click on the "Connect tab" of your database and copy and save your database is "ASTRA_DB_ID", below the "Configure your environment" step. (Step 3)
- Click on the "CQL Console" tab and create the tables in the "1_db_objects" file.

**Create a streaming tenant**
- From the left hand menu, click on "Streaming" and then click "Create Stream"
- Create your tenant on "Google Cloud" and the "us-central1" region.
- Click on the "Namespace and Topics" tab. Create a new namespace called "events-namespace" and add a persistent Topic named "events-topic" to the namespace.
- Click on "Sinks" and then "Create Sink" named "events-sink". Select the "events-namespace" and Sink type "Astra DB". Under "Connect Topics" select your "events-topic"
- Under "Sink-Specific Configuration" select your Astra Database, enter the token Astra DB token you saved in a previous step. Select the "logs" keyspace and type "events" as your table name. If the configuration was applies correctly, the mapping should generate automatically.
- Generate a streaming tenant token by clicking on "Settings" and then "Create token" and save it for the next steps.

### Step Two: Generate data
- Open this Github repo on GitPod and open the "2_logs_shipper.py" file.
- Replace the "service_url" and "token" values by your streaming tenant values. You can get your "service_url" from the "Connect" tab of your streaming tenant. It appears after "Broker Service URL".

