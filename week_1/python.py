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

SELECT order_id, customer, amount,
    ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num,
    RANK() OVER (ORDER BY amount DESC) AS rank_num,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
FROM orders;

Topic - 4

SELECT order_id, customer, amount, order_date,
    LAG(amount) OVER (PARTITION BY customer ORDER BY order_date) AS prev_amount
FROM orders;

SELECT order_id, customer, order_date,
    LEAD(order_date) OVER (PARTITION BY customer ORDER BY order_date) AS next_order_date
FROM orders;

Topic - 5

SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);

SELECT DISTINCT c.name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

Topic-6
row to keep - We should Keep the latest record.
Logic - First grouping duplicate records
              sort by latest date
              We shouldkeep only the newest record

Topic-7
1#SELECT customer_id, amount
FROM orders;

2#SELECT customer_id, amount
FROM orders
WHERE order_date >= '2024-02-01';

3- Filtering completed orders before aggregation gives correct results by excluding invalid records and also improves queryperformance by reducing the number of rows processed during aggregation

Topic-8
1 - Imagine we have a 1000-page book with no index.
If we want to find where joins are explained we need to flip page by page until wefind it.
Now we have the same book with an index.
“Joins → page 245”
We no need tosearch the whole book anymore we can directly jump to page 245.
2 - best column to index is the date column. Because we are always filter based on time.



Week - 4
Task-1
*Identify at Least Five Entities - Customer, Restaurant, Order, Driver, Payment
*For each entity, three possible attributes 
Customer - Customer name, phone number, Customer_id
Restaurant - Restaurant name, location, restaurant_id
Order - Order_id, order_date, order_amount
Driver - Driver name, driver_id, phone number
Payment - Payment_id, payment_amount, payment_date
*Explain how Customer, Restaurant, Order, and Driver are related - In a food delivery app, Customer, Restaurant, and Driver are connected through the Orders table. A customer places orders, restaurants prepare those orders, and drivers deliver them. Most relationships are one-to-many because one customer, restaurant, or driver can be associated with multiple orders
*Convert one business sentence into a rough table design
A company wants to track customer purchases
| customer_id | customer_name | city   |
| 1           | Ravi          | Dallas |

| order_id | customer_id | amount |
| 101      | 1           | 500    |
The business wants to track purchases, so we need Customer & Order tables
The orders table stores customer_id to show customer placed the order.
Task-2
*Identify entities and attributes for a banking app
Entity: Customer
Attributes:
customer_id
customer_name
phone_number

Entity: Account
Attributes:
account_number
account_type
balance

Entity: Transaction
Attributes:
transaction_id
transaction_amount
transaction_date

*Separate attributes that belong to Customer and Account.
Customer
customer_name
email
phone_number
address

Account
account_number
balance
account_type
accout created_date

*Given a messy list of fields, group them under correct entities
Fields:
customer_name, account_balance, transaction_date, email, account_type
Customer
customer_name
email
Account
account_balance
account_type
Transaction
transaction_date

*Explain why order_amount belongs to Order and not Customer
order_amount changes for every order. A customer can place many orders with different amounts. If we store order_amount inside Customer, we would lose proper transaction-level detail.
So order_amount belongs to the Order table because it describes the order, not the customer.



