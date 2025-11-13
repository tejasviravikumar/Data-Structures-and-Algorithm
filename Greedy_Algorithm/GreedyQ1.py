def minFlips(bulbs : list[int]):
    cost = 0
    for bulb in bulbs:

        # Here we use cost to determine if the flip is even or odd cause after two flips the other parts retain to the original state same for odd flips
        if cost % 2 == 0: 
            bulb = bulb       # remains same 
        else:
            bulb = not bulb   # Flip the switch 

         # here we check if the bulb is ON / OFF 
        if bulb % 2 == 1:
            continue          # ON so skip it   

        else:
            cost += 1         #OFF so update the cost cause we changed the bulb state in the previous if-else block

    return cost

def main():
    l1 = [1,0,1]
    print(minFlips(l1))


if __name__ == "__main__":
    main()