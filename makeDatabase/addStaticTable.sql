-- Create static events in database

CREATE TABLE IF NOT EXSISTS 'staticEvent' (
'myKey' Int,
'eventKey' Int, --Key associated with the userTable event
'event' VARCHAR(100),
-- required Boolean, --possible future implementation
'timeStart' DATETIME, -- form looks like: 2016-10-25 08:20:00
'timeEnd' DATETIME, 
'eventLength' Double -- Optional, either enter event length or time
);


