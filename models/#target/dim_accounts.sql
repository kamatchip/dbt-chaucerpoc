{{ config(materialized='table') }}

SELECT row_number() over (order by YEAROFACCOUNT) as id, *  FROM (select  DISTINCT 
ACCOUNTNO,
ACCOUNTTYPE ,
YEAROFACCOUNT ,
CURRENT_TIMESTAMP as CREATED_AT
from {{ ref('src_business_units') }} )