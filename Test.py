indian = ["samosa", "daal", "naan"]
chinese = ["Egg roll", "Fried rice", "Dumplings"]
italian = ["Pizza", "Pasta", "Risotto"]

dish = input("Enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Base on limited source of my knowledge I have no information on which cuisine is", dish)