SELECT MIN(ABS(P1.x-P2.x)) as shortest
FROM point P1 JOIN point P2 ON P1.x != P2.x
