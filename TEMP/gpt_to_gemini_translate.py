gpt=[]
new=[]
for i in range(len(gpt)):
    new.append({
        "parts": [
        {
            "text": gpt[i]["content"]
        }
        ],
        "role": gpt[i]["role"].replace("assistant","model")
    })


