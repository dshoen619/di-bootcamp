-- create table drug_list(
-- dragRegNum varchar(65000),
-- dragHebName varchar(65000),
-- bitulDate varchar(65000),
-- isCytotoxic varchar(65000),
-- isVeterinary varchar(65000),
-- applicationType varchar(65000),
-- isPrescription varchar(65000),
-- iscanceled varchar(65000),
-- dragEnName varchar(65000),
-- usageFormHeb varchar(65000),
-- usageFormEng varchar(65000),
-- dosageForm varchar(65000),
-- dosageFormEng varchar(65000),
-- dragIndication varchar(65000),
-- activeMetirals varchar(65000),
-- dosage varchar(65000)
-- );


-- COPY drug_list (dragRegNum,dragHebName,bitulDate,isCytotoxic,isVeterinary,applicationType,isPrescription,iscanceled,dragEnName,usageFormHeb,usageFormEng,dosageForm,dosageFormEng,dragIndication,activeMetirals,dosage)
-- FROM '/Users/davidshoen1/Downloads/h2_4.csv'
-- Delimiter ','
-- CSV Header;


select* from drug_list;
-- select * from drug_list 
-- where dragindication LIKE '%diar%';