info={
    "id1":{"name": "nihitha", "subject": "maths"},
        "id2":{"name": "nihanth", "subject": "science"},
            "id3":{"name": "jump", "subject": "computer"},
        "id4":{"name": "sing", "subject": "gk"},
        "id1":{"name": "nihitha", "subject": "maths"}
}

r={}
for k,v in info.items():
    if v not in r.values():
        r[k]=v

    print(r)