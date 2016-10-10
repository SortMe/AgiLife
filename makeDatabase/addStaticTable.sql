-- Create static events in database

CREATE TABLE staticEvent (
myKey Int,
event VARCHAR(100),
required Boolean,
timeStart DATETIME, -- form looks like: 2016-10-25 08:20:00
timeEnd DATETIME
);


