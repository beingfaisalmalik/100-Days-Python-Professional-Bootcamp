#try Can Have Multiple errors here
a = {"Faisal":1}
try:
    print(a["A"])
except Exception as e:
    print(e)
else:
    print("Success")
finally:
    print("Done")