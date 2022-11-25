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

### Step One: Create an Astra Database
