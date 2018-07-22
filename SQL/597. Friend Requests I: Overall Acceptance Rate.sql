select
round(
    ifnull(
    (select count(*) from (select distinct requester_id, accepter_id from request_accepted) A)
    /
    (select count(*) from (select distinct sender_id, send_to_id from friend_request) B),
    0)
, 2) as accept_rate;
