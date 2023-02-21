create database IF NOT EXISTS JSON_Dtype;
use JSON_Dtype;

-- creating table J_table for JSON data type demo

create table J_table (json_col1 JSON, task varchar(100));

-- Insertion of JSON data type values into table (Direct Insertion) 

-- JSON object insertion
Insert into J_table(json_col1, task) values('{"key1":"value1","key2":"value2"}','Direct Insertion');
-- JSON array insertion
Insert into J_table(json_col1, task) values('[3,"string1"]','Direct Insertion');

-- Insertion of JSON data type values into table (Insertion using functions) 

Insert into J_table(json_col1, task) values(JSON_object("key3","value3","key4","value4"),'Insertion through json method');
Insert into J_table(json_col1, task) values(JSON_array("string2",3,'{"key5":"value5","key6":"value6"}'),'Insertion through json method');

-- Nested Insertion

-- JSON object in an array
Insert into J_table(json_col1, task) values('[{"key1":"value1", "key2":"value2"}, "string2", 3]','Nested type-1');
-- Array inside JSON object
Insert into J_table(json_col1, task) values('{"key1":["string3", 6], "key2":"value2"}','Nested type-2');

-- display final table

select * from J_table;