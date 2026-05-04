print("Vinuthna")

print("City is Virginia")
x = 5
print(type(x))
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)
product_name = "Mouse"
price = 400.99
stock = 50
is_active = True
print(type(product_name))
print(type(price))
print(type(stock))
print(type(is_active))
price = 120 

if price > 110:
    print("Price is greater than 110")
else:
    print("Price is 110 or less")

 
thislist = ["grapes", "mango", "cherry"]

print(thislist)   
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
cities = ["Delhi", "Mumbai", "Chennai"]

for city in cities:
    print(city)

 product = {
    "id": 102,
    "name": "Phone",
    "category": "Electronics",
    "price": 2000
}

print(product["price"])

def convert_to_upper(product_name):
    upper_name = product_name.upper()  
    return upper_name  
    result = convert_to_upper("vinnu")
    print(result)

id,name,city
1,Ravi,Hyderabad
2,Anvi,Chennai
3,Srinika,New York
import csv
with open("students.csv", "r") as file:
    
  reader = csv.DictReader(file)
  for row in reader:
  print(row)

 price_text = "avs" #bad value
  try:
    price = int(price_text)  
    print(price)
except:
    print("Invalid price value")

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


 Week 2
SELECT CustomerName, City FROM Customers;
SELECT * FROM Customers
WHERE Country = 'India';
SELECT * FROM Customers
WHERE age<30;
SELECT * FROM Products
ORDER BY Price ASC;
#customers:
id,name,age,city
1,Ravi,25,Hyderabad
2,Asha,30,Chennai
3,Imran,22,Bangalore
#orders:
order_id,customer_id,amount
101,1,500
102,2,700
103,1,300
SELECT * FROM customers;
SELECT *
FROM customers
WHERE city = 'Bangalore';
SELECT c.name, o.amount
FROM customers c
JOIN orders o
ON c.id = o.customer_id;
SELECT customer_id, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;
SELECT *
FROM customers
WHERE id IS NULL OR name IS NULL OR age IS NULL OR city IS NULL;
SELECT  c.name, COUNT(o.order_id) AS total_orders,
SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o
ON c.id = o.customer_id
GROUP BY c.name;

customers
customer_id | name  | city      | age | updated_at
1           | Ravi  | Hyderabad | 25  | 2024-01-10
2           | Asha  | Chennai   | 30  | 2024-01-12
3           | Imran | Hyderabad | 22  | 2024-01-11
1           | Ravi  | Hyderabad | 26  | 2024-02-01

orders
order_id | customer_id | order_date  | amount | status
101      | 1           | 2024-01-01  | 500    | completed
102      | 2           | 2024-02-01  | 700    | completed
103      | 1           | 2024-03-01  | 300    | returned
104      | 3           | 2024-03-05  | 250    | completed

Topic-1
WITH completed_orders AS (
    SELECT *
    FROM orders
    WHERE status = 'completed'
),
recent_completed_orders AS (
    SELECT *
    FROM completed_orders
    WHERE order_date > '2024-02-01'
)
SELECT *
FROM recent_completed_orders;

Topuic-2
SELECT customer_id, name, city, age,
    RANK() OVER (PARTITION BY city ORDER BY age DESC) AS age_rank
FROM customers;

SELECT order_id, customer_id, amount,
    RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS amount_rank
FROM orders;

Topic-3


