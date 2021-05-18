#딕셔너리

pairs = {'잔나비': '싫어', '이소라': '좋아'}

print(pairs)

pairs['김단비'] = '좋아'

print(pairs)

del pairs['잔나비']

print(pairs)

print(pairs.get('김단비'))
