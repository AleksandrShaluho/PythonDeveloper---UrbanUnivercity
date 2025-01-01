def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i:j+1]

print(all_variants('abc'))
a = all_variants("abc")
for i in a:
    print(i)