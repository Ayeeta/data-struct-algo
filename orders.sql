select Customers.Name as 'customers' from Customers
where Customers.id not in (
    select customerid from orders
)