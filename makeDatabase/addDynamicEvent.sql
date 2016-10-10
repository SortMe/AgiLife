-- Create a dynamic event
INSERT INTO dynamicEvent (myKey, event, weight)
VALUES (input_key >=@current_key,input_event >=@current_event,input_weight >=@current_weight);



/* script:get_customer_record.sql */

-- SELECT c_id, c_first_name,c_last_name, c_address,
-- ……
-- ,last_modified_date
-- FROM customer
-- WHERE last_modified_date >=@start_date AND last_modified_date <= @end_date; @start_date AND @end_date

