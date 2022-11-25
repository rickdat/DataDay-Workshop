import requests
import pandas
import uuid

ASTRA_DB_ID="b2431031-f6c1-4cff-bdd7-47b4a4810061"
ASTRA_DB_REGION="us-central1"
ASTRA_DB_KEYSPACE="logs"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:XilDZTkQebsDuWaXRcZAUSok:217a4ba6f471118ef80b97a000fd0769463799c056c514dbd68b3645038505ae"
get_url = 'https://'+ASTRA_DB_ID+'-'+ASTRA_DB_REGION+'.apps.astra.datastax.com/api/rest/v1/keyspaces/logs/tables/events/rows/'
post_url = 'https://'+ASTRA_DB_ID+'-'+ASTRA_DB_REGION+'.apps.astra.datastax.com/api/rest/v1/keyspaces/logs/tables/metrics/rows/'

# get rows frm astra table and save result in a list
def get_rows():
    x = requests.get(get_url, headers={"X-Cassandra-Token": ASTRA_DB_APPLICATION_TOKEN, "Content-Type": "application/json", "Accept": "application/json", "Page-Size": "100"})
    x = x.json()
    x = x["rows"]
    return(x)

#convert to pandas dataframe
df = pandas.DataFrame(get_rows())

# count the amount of times the text "memory" appears in the dataframe
memory_count=df['data'].str.count('LAPTOP-5MFKVMMH').sum()
cpu_count=df['data'].str.count('cpu').sum()
priviledge_escalation_count=df['data'].str.count('sudo').sum()

# get the row that contains the text "262144"
malware_alert=df[df['data'].str.contains('262144')]

# add rows to astra table

jsontext = {"columns": [
        {
            "name": "id",
            "value": str(uuid.uuid4())
        },
        {
            "name": "memory",
            "value": str(memory_count)
        },
        {
            "name": "cpu",
            "value": str(cpu_count)
        },
        {
            "name": "priviledge_escalation",
            "value": str(priviledge_escalation_count)
        }
    ]}


x = requests.post(post_url, headers={"X-Cassandra-Token": ASTRA_DB_APPLICATION_TOKEN, "Content-Type": "application/json", "Accept": "application/json"}, json=jsontext)
x = x.json()
print(x)


