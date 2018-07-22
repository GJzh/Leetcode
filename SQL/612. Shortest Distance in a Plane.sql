select round(min(sqrt(power(p.x-q.x,2)+power(p.y-q.y,2))),2) as shortest
from point_2d p, point_2d q
where p.x != q.x or p.y != q.y
