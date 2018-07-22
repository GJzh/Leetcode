SELECT Customers
FROM ( SELECT Customers.Name as Customers, Orders.Id as OrderID
      FROM Customers LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
) ORDEREDCustomers
WHERE OrderID IS NULL
