"""Practicing!"""

pets: list[str] = ["Louie", "Bo", "Bear"]

for item in pets:
    print(f"Good boy, { item }!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0,len(names)):
    elem: str = names[idx]
    print(f"{ idx }: {elem}")