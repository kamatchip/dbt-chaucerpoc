{{ config(materialized='table') }}

select row_number() over (order by null ) as id, * from  (select  
        
        distinct 
        originalcurrency as currency ,
        settlementcurrency , 
        exchangerate,
        current_timestamp as created_at
 from {{ ref('src_business_units') }} )