N = int(input())
promise = [
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop'
]
result = 'No'
for i in range(N):
    s = input()
    if not s in promise:
        result = 'Yes'
print(result)