# DataDay

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/rickdat/DataDay-Producer)

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
- Click on "Databases" and then "Create Database". For this POC, your database should be on "Google Cloud" and the "us-east-1" region. Your keyspace should be called "logs"
- Once database is created, download the "token" and database details, then click on "Go to database"
- Click on the "Connect tab" of your database and copy and save your database id "ASTRA_DB_ID", you can find it below the "Configure your environment" step. (Step 3)
- Click on the "CQL Console" tab and create the tables in the "1_db_objects" file in this repo.

**Create a streaming tenant**
- From the left hand menu, click on "Streaming" and then click "Create Stream" [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/rickdat/DataDay-Producer)
- Create your tenant on "Google Cloud" and the "us-east-1" region.
- Click on the "Namespace and Topics" tab. Create a new namespace called "events-namespace" and add a persistent Topic named "events-topic" to the namespace.
- Click on "Sinks" and then "Create Sink" named "events-sink". Select the "events-namespace" and Sink type "Astra DB". Under "Connect Topics" select your "events-topic"
- Under "Sink-Specific Configuration" select your Astra Database, enter the token Astra DB token you saved in a previous step. Select the "logs" keyspace and type "events" as your table name. If the configuration was applies correctly, the mapping should generate automatically.
- Generate a streaming tenant token by clicking on "Settings" and then "Create token" and save it for the next steps, then click create.

### Step Two: Collect and send log data
- Open this Github repo on GitPod and open the "2_logs_shipper.py" file.
- Replace the "service_url" and "token" values by your streaming tenant values. You can get your "service_url" from the "Connect" tab of your streaming tenant. It appears as "Broker Service URL" in the connect tab.
- Click on "Namespace and Topics" and copy the "Full Name" of your "events-topic". Paste it into your "2_logs_shipper" script in the "topic" value.
- Execute the "2_logs_shipper.py" file.

### Step Three: Analyze and visualize data.
- Create an account at Grafana and click on "Configuration" on the bottom left corner. Click on "Plugins", search for "Astra" and install the plugin.
- Go back to your Grafana dashboard and click on "Integrations and Connections". Look for the "Astra" datasource and click "Create a AstraDB data source".
- Go to your Astra Database, click the Connect tab, and copy the ClusterID and AstraDBRegion "ASTRA_DB_ID", "ASTRA_DB_REGION" then enter them in this format to create a URI. <ASTRA_DB_ID>-<ASTRA_DB_REGION>.apps.astra.datastax.com:443. Enter the Astra Database token copied before.
- Import the "Logs Dashboard" and "Events Dashboard". Observe the data in the logs dashboard.
- Open the "3_data_analyzer.py" script and enter your "ASTRA_DB_ID" and "ASTRA_DB_APPLICATION_TOKEN".
- Execute the "3_data_analyzer.py" script
- Observe the data in the "events" dashboard.

