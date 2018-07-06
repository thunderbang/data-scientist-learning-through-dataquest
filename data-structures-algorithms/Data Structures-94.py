## 3. Exercise: Dynamic Arrays ##

# Retrieving an item in an array by index
retrieval_by_index = ""

# Searching for a value in an unordered array
search = ""

# Deleting an item from an array, and filling the gap
#     by shifting all later items back by one
deletion = ""

# Inserting an item into the array, and shifting forward
#     every item that comes after it
insertion = ""
retrieval_by_index = "constant"
search = "linear"
deletion = "linear"
insertion = "linear"

## 4. Exercise: Practice Inserting Into an Array ##

players = ["Reggie Jackson"]
print(players)
players.insert(1, "C.J. Watson")
print(players)
players.insert(0, "Jeff Adrien")
print(players)
players.remove("Reggie Jackson")
print(players)
players.insert(0, "Quincy Acy")
players.insert(2, "Evan Turner")

## 6. 2D Array Implementation ##

red_pieces = 0
black_pieces = 0

# Find how many red and black pieces there are
for row in checker_board:
    for piece in row:
        if piece == "red":
            red_pieces += 1
        elif piece == "black":
            black_pieces += 1

## 9. Dictionary Access ##

# Population of Rio de Janeiro
rio_population = city_populations["Rio de Janeiro"]
boston_population = city_populations["Boston"]
paris_population = city_populations["Paris"]
city_populations["Beijing"] += 1
city_populations["Boston"] -= 1