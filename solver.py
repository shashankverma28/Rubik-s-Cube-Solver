# import kociemba

# f=open('input2.txt','r')
# s=f.read() 
# f.close() 
# print(s)
# solution=kociemba.solve(s)
# print(solution)
# f=open('output.txt','w')
# f.write(solution)
# f.close() 

import kociemba

# Read the input2.txt file
with open('input2.txt', 'r') as file:
    s = file.read().strip()

# Debug: Print the read cube string
print(f"Cube string: {s}")

try:
    # Solve the cube
    solution = kociemba.solve(s)
    print(solution)

    # Write the solution to output.txt
    with open('output.txt', 'w') as file:
        file.write(solution)
except ValueError as e:
    print(f"Error: {e}")

