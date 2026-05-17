tsalin = int(input("tsalin: "))

if tsalin < 500000:
    bonus = 0.1
elif tsalin <= 1000000:
    bonus = 0.05
else:
    bonus = 0.02

net = (tsalin + tsalin * bonus) * 0.9
print(f"niit mongo: {net:,.0f} togrog ")