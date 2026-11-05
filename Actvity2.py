total_chores = 4
completed = 0

chores = ["Make your bed", "Feed the pet",
          "Take out the trash", "Wash the dishes"]

while completed<total_chores: 
    print("Have you finished:", chores[completed], "?")
    answer = input("yes/no: ")
    if answer=="yes":
        print("Good job!")
        completed=completed+1
    else:
        print("Finish remaining chore then restart")
    print("Chores remaining:", total_chores - completed)

print("\nALL CHORES COMPLETE!")
print("Chores assigned:", total_chores)
print("Chores completed:", completed)
print("Chores remaining:", total_chores - completed)