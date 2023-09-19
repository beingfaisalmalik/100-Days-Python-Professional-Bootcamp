with open('Day-26/file1.txt') as f:
    content1 = f.readlines()
print(content1[:-1])

with open('Day-26/file2.txt') as f:
    content2 = [line[:-1] for line in f]
print(content2)   

results = [c1number for c1number in content1 for c2number in content2 if c1number == c2number]
for i in range(len(results)-1):
    if results[i] == results[i-1]:
        results.remove(results[i])
print(results)