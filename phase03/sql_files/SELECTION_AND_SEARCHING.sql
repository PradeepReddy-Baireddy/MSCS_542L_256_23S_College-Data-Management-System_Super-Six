-- Search and Selection JSON documents using functions

select json_col1,

-- JSON_EXTRACT() FUNCTION FOR SEARCH
-- searching for values with key as 'key1' 
JSON_EXTRACT(json_col1,'$.key1'),
-- searching for values in an array with key as 'key1' and index of object is 0
JSON_EXTRACT(json_col1,'$[0].key1'),

-- JSON_INSERT()​ function
-- inser new object with key 'keynew' and value 'newval'
JSON_INSERT(json_col1,'$.keynew', "newval"),

-- JSON_SET()​ function
-- set object with key 'key1' as 'val3'
JSON_SET(json_col1,'$.key1', "val3"),

-- JSON_REMOVE()​ function
-- remove value of first json object of array
JSON_REMOVE(json_col1,'$[0]'),

-- JSON_REPLACE()​ function
-- replace value of object with key as key1 with val3
JSON_REPLACE(json_col1,'$.key1', "val3")


from J_table;