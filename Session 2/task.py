import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [120, 85, 150, 110, 95]

plt.bar(products, sales, color = ['red', 'lightgreen', 'orange', 'aqua', 'blue'])

plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()

max_val = np.max(sales)
a = sales.index(max_val)
print("The Top-Selling Product is", products[a])

total = np.sum(sales)
print("The Total Sales Amount is", total)
