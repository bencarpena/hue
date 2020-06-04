import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import datetime as dt

log_name = "hue_log_" + (str(dt.datetime.now()).replace(":", ".")).replace(" ", "_") + ".txt"


import http.client
import mimetypes




#>>>>>>> Hue Parameters >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
conn = http.client.HTTPSConnection("192.168.0.10")
payload = "{\"on\":false, \"bri\":254}"
headers = {
  'Content-Type': 'text/plain'
}
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#Create log file
#=======================================================
def create_log_file(logdata):
  f = open("./hue_log/" + log_name, "a")
  f.write("\n")
  f.write(logdata)
  f.close()


#Office Lights
#=======================================================
create_log_file("###Office Lights")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/9/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)
#print(data.decode("utf-8"))


#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/8/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)



#Dining Light
#=======================================================
create_log_file("###Dining Light")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/2/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)


#Kitchen Light
#=======================================================
create_log_file("###Kitchen Light")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/1/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)


#Chandelier Lights
#=======================================================
create_log_file("###Chandelier Lights")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/3/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)

#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/4/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)

#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/6/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)


#First Floor Hallway Light
#=======================================================
create_log_file("###1F Hallway Light")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/5/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)


#Second Floor Hallway Lights
#=======================================================
create_log_file("###2F Hallway Lights")
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/7/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)
#===Execute
conn.request("PUT", "/api/bpdiHvLoYj7sGYMjUhjvPMAIOnv9M7tSCtbzmBRp/lights/10/state", payload, headers)
res = conn.getresponse()

#===Enter log
data = res.read()
data = data.decode("utf-8")
create_log_file(data)


