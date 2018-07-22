select Name
from Candidate
where id = (select CandidateId
            from (select CandidateId, count(*) as CandidateVote from Vote group by CandidateId) p 
            order by CandidateVote desc limit 1)
