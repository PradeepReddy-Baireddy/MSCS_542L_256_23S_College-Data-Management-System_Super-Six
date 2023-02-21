-- Other functions

-- Appending integer element into index 2 of an array
select json_col1,JSON_ARRAY_APPEND(json_col1 ,'$[1]',1) from J_table;

-- Insering integer element into index 2 of an array
select JSON_ARRAY_INSERT(json_col1 ,'$[0]',1) from J_table;

-- JSON column objects storage size calculation
select json_col1, JSON_STORAGE_SIZE(json_col1) from J_table;

-- JSON column element Type
select json_col1, JSON_TYPE(json_col1) from J_table;

-- JSON column element length (gives length of array or number of key-value pairs in JSON object)
select json_col1, JSON_LENGTH(json_col1) from J_table;

-- confirming validity of json objects before inserting (returns 1 if valid 0 if not)
select JSON_VALID('string'), JSON_VALID('"string1"');

 