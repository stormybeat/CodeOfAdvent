allRucksackInput = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


allrucksacksList = allRucksackInput.split("\n")
print()
for rucksackContent in allrucksacksList:
    stringLen = len(rucksackContent)
    firstCompartment = slice(0, stringLen//2)
    secondCompartment = slice(stringLen//2, stringLen)
    print(rucksackContent[firstCompartment], rucksackContent[secondCompartment])