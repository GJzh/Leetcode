SELECT FirstName, LastName, City, State
FROM Person LEFT JOIN Address USING(PersonId)
