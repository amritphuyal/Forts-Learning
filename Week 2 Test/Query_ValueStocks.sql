with last_year as (select 
                    company ,fiscal_year,fiscal_year%100 as y1  -- obtain last 2 digit of fiscal year
                    from dividend
                    order by company
),   
 next2_year as (select 
                    distinct on (company) company ,fiscal_year,fiscal_year,fiscal_year%100 as y1,
                    lead(y1 ) over (order by company) as  y2,
                    lead(y1,2) over (order by company) as  y3,
                    lead(y1,3) over (order by company) as  y4
                    from last_year
 )

select array( -- Convert to array 
select  company || '  ' from next2_year   -- || concanate string  and  ' ' to match with required output. {"CZBIL ","GBIME "} , one space after each company name
where ((y3 - y2) = 1 and (y2-y1) = 1 ) or ((y4-y3=1 and (y3-y2)=1) ) -- select only company that distribute dividend for  next 2 consecutive years
) as valuestocks;  -- output as valuestocks
