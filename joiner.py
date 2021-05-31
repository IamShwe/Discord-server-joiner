import requests

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discord.gg/zta3AZHs" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")
