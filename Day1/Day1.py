import matplotlib.pyplot as plt

x = [1 , 2 , 3 , 4 , 5]
y = [ i **2 for i in x]
plt.plot(x, y, marker = 'o')
plt.title("Matplotlib Test")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()