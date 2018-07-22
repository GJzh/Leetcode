select dept_name, ifnull(student_number, 0) as student_number
from department left join (select dept_id, count(*) as student_number from student group by dept_id) p using (dept_id)
order by student_number desc, dept_name 
