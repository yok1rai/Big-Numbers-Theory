import random

dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
entry_counter = 0
previous_probs = None


while True:
    try:
        entry = int(input("What is your range of attempts? (0 to quit) "))
        if entry < 1000000 and entry != 0:
            entry_counter += 1
            for i in range(entry):
                dice = random.randint(1,6)
                dices[dice] += 1
            
            current_probs = []
            for dice in dices:
                prob = dices[dice] / entry
                current_probs.append(prob)
                print(f"The chances of {dice} is:\n {prob}")
            
            if previous_probs is not None:
                avg_diff = sum(abs(current_probs[i] - previous_probs[i]) for i in range(6)) / 6
                print(f"Avg. Difference is {avg_diff:.4f}")
            
            previous_probs = current_probs
            dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        elif entry == 0:
            print("Good night...")
            break
        else:
            print("Too big number to proccess")
            continue
    except ValueError:
        print("Please enter a valid input")
