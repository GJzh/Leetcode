from (select question_id, count(*) as answer_count from survey_log where action = 'answer' group by question_id) t1
     right join
     (select question_id, count(*) as action_count from survey_log group by question_id) t using (question_id)
     left join
     (select question_id, count(*) as show_count from survey_log where action = 'show' group by question_id) t2 using (question_id)
order by (answer_count)/(show_count) desc
limit 1
