-- Create a table to store dynamic events, varchar allows for a variable amount
CREATE TABLE dynamicEvent (
myKey Int,
eventKey Int,      -- Key associated with the userTable event
event VARCHAR(100),
weight Double,    -- assigned by them
timePreference Int, -- time of day preference
timeStart DATETIME,  -- Output looks like: 2016-10-25 08:20:00
timeEnd DATETIME, -- Optional, either enter length of event or completion date
eventLength Double -- Optional, they can either enter length of event or time it takes to complete
);
-- start time, end time, period of time, total day preffered time of day 

