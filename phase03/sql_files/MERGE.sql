-- Mering JSON documents

-- Using JSON_MERGE_PRESERVE()

select JSON_MERGE_PRESERVE(json_col1 ,'[1, 2]'),

JSON_MERGE_PRESERVE('[1, 2]', json_col1),

JSON_MERGE_PRESERVE(json_col1 ,'{"keymerge":"valuemerge"}'),

JSON_MERGE_PRESERVE('{"keymerge":"valuemerge"}',json_col1),

-- Using JSON_MERGE_PRESERVE()

JSON_MERGE_PATCH(json_col1 ,'[1, 2]'),

JSON_MERGE_PATCH('[1, 2]', json_col1),

JSON_MERGE_PATCH(json_col1 ,'{"keymerge":"valuemerge"}'),

JSON_MERGE_PATCH('{"keymerge":"valuemerge"}',json_col1)

 from J_table;

