SELECT x, y, z, (CASE WHEN x+y>z AND ABS(x-y)<z THEN 'Yes'
                      ELSE 'No' END) as triangle
FROM triangle
