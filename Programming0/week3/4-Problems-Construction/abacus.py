#Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 

def print_abacus(n):

    line = "|00000*****   |"
    text = ['|', '0', '0', '0', '0', '0', '*', '*',
            '*', '*', '*', ' ', ' ', ' ', '|']

    if n == 0:
        while n <= 9:
            print(line)
            n = n + 1

    else:
        line = ""
        prints = []

        while n > 0:
            text.insert(11 - n % 10, ' ')
            text.insert(12 - n % 10, ' ')
            text.insert(13 - n % 10, ' ')
            text.pop(-2)
            text.pop(-2)
            text.pop(-2)
            for e in text:
                line = line + e
            prints.append(line)
            text = ['|', '0', '0', '0', '0', '0', '*', '*',
                    '*', '*', '*', ' ', ' ', ' ', '|']
            line = ""
            n = (n - n % 10) // 10

        line = "|00000*****   |"       
        countPrints = len(prints)
        while countPrints < 10:
            prints.append(line)
            countPrints += 1

        prints.reverse()

        for e in prints:
            print (e)

def main():
    n = input("Enter n: ")
    n = int(n)

    print ("Abacus showing 0:")
    print_abacus(n)


if __name__ == "__main__":
    main()           


