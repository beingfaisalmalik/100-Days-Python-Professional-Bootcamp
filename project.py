
with open(file="Day-24/Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    temp = [line[:-1] for line in f]
with open(file="Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as f:
    content = f.read()


content = content.replace("Angela","Faisal")
for i  in range(0,len(temp)-1):
    if "[name]" in content:
        
        content = content.replace("[name]", temp[i])
    else:
        content = content.replace(f"{temp[i-1]}", temp[i])
    with open(file=f"Day-24/Mail Merge Project Start/Output/ReadyToSend/{temp[i]}.txt", mode="w") as f:
        f.write(content)
        