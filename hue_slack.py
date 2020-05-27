import re
import time
import json
import psutil

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from slackclient import SlackClient
#from slack import WebClient

#Slack Workspace = DiveHQ
#slack_client = WebClient("xoxb-63457761984-1147150098451-Lqw4MfwpKOt3M8qkKVmwTFKO")
slack_client = SlackClient("xoxb-63457761984-1147150098451-Lqw4MfwpKOt3M8qkKVmwTFKO")




# Fetch your Bot's User ID
user_list = slack_client.api_call("users.list")
for user in user_list.get('members'):
    if user.get('name') == "thorbot":
        slack_user_id = user.get('id')
        break


# Start connection
if slack_client.rtm_connect():
    print ("Thorbot now online!")

    while True:
        for message in slack_client.rtm_read():
            if 'text' in message and message['text'].startswith("<@%s>" % slack_user_id):

                print ("Message received: %s" % json.dumps(message, indent=2))

                message_text = message['text'].\
                    split("<@%s>" % slack_user_id)[1].\
                    strip()

                if re.match(r'.*(cpu).*', message_text, re.IGNORECASE):
                    cpu_pct = psutil.cpu_percent(interval=1, percpu=False)

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My CPU is at %s%%." % cpu_pct,
                        as_user=True)

                if re.match(r'.*(memory|ram).*', message_text, re.IGNORECASE):
                    mem = psutil.virtual_memory()
                    mem_pct = mem.percent

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My RAM is at %s%%." % mem_pct,
                        as_user=True)

        time.sleep(1)
