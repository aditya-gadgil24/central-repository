"""This file and its code blocks purely illustrate the core fundamentals and concepts of 
python programming language"""



x = 5
print(x)
print(type(x))

squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)

# begin
record = 'steve, 70, founder'
name, age, title = record.split(",")
# end


x = [2, 9]
b = x
b.append(11)
print(b)
print(x)


a = b = []       # ⚠️ both refer to the *same list*
a.append(111)
print(b)         # [1]

x, y, z = 1, 11, 19
name, age = ['Bill', 68]

x = 5 + 6
print(x)



list_x = [9, 13, 19]
list_x[0] = 29
print(list_x)

print(hash('abc'))


# code block to illustrate hashable elements in python

d = {}
d["a"] = 1           # ✅ str is hashable
d[(1, 2)] = "tuple"  # ✅ tuple is hashable


# set elements
s = {1, "hello", (2, 3)}  # ✅
# end

# begin
t = 1
if t < 5:
    print('domestic terminal')
elif t > 5 and t < 20:
    print('international')
else:
    print('code sharing flights')

# end

# begin
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
# end



# begin
i = 10
while i < 999:
    print(i)
    i = i * 1.25
# end

# begin
for i in range(50):
    print(i)  

for char in "Sam":
    print(char)
# end


data = {'a': 1, 'b': 2}
for k, v in data.items():
    print(k, v)


x = 3
while x > 0:
    print(x)
    x -= 1
# end


# begin
# break — exits the loop
for x in range(60):
    if x == 50:
        break
    print(x)
# end

# begin
for b in range(100):
    if b % 2 != 0:
        continue
    print(b)

# list comprehension

sqr = [a*a for a in range(5)]
print(sqr)

# with condition
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)


unique_lengths = {len(word) for word in ["Sam", "Data", "Python", "Sam"]}
print(unique_lengths)
# Result: {4, 6, 3}


# if-else inline

labels = ['even' if x % 2 ==0 else 'odd' for x in range(15)]
print(labels)




