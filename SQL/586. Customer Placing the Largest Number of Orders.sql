SELECT customer_number
FROM (SELECT customer_number, COUNT(*) as OrderCount 
      FROM orders
      GROUP BY customer_number 
      ORDER BY OrderCount DESC) P 
LIMIT 1
