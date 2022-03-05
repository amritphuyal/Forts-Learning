-- -- import from dat.csv file into dividend table
-- Copy  dividend(company,fiscal_year)
-- From 'E:\Forts Learning\Week 2 Test\data.csv'
-- delimiter ','
-- csv header;

-- ----------------OR ---------------------



-- insert data manually
insert into dividend(company,fiscal_year)
values('AHPC',20702071),
('AHPC',20712072),
('AHPC',20732074),
('AHPC',20762077),
('CZBIL',20692070),
('CZBIL',20702071),
('CZBIL',20712072),
('CZBIL',20732074),
('GBIME',20692070),
('GBIME',20702071),
('GBIME',20712072),
('GBIME',20732074);

select * from dividend; -- show data

