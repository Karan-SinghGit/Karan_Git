set SERVEROUTPUT ON;
declare 
number1 number(10);
number2 number(10);

BEGIN
number1:=10;
number2:=10;
dbms_output.put_line('sum of two number is ' ||(number1+number2) );
end;


-- SECOND WAY TO DECLARE THE VARIABLE
declare 
number1 number(10):=10;
number2 number(10):=5;

BEGIN


dbms_output.put_line('sum of two number is ' ||(number1+number2) );
end;


----if variable is DECIMAL TYPE
declare 
number1 number(10,2):=10.2;
number2 number(10,2):=5.4; 
total number (10,2);
BEGIN
total:=number1+number2;
dbms_output.put_line('sum of two number is ' ||total );
end;


-----------------------------
---if we want to take the value from the user then we nee to use & saymbol

declare 
number1 number(10,2):=&number1;
number2 number(10,4):=&number2;
total number (10,2);
BEGIN
total:=number1+number2;
dbms_output.put_line('sum of two number is ' ||total );
end;

-----
--if want to display entry of user in output also then 
declare 
number1 number(10,2):=&number1;
number2 number(10,4):=&number2;
total number (10,2);
BEGIN
total:=number1+number2;
dbms_output.put_line('sum of' ||number1 || 'and' ||number2|| 'is ' ||total );
end; 



----------- global and local variable ----value assigned inside the begin and end block will replace the value of variable from declare block


declare 
number1 number(10,2):=10.2;
number2 number(10,4):=5.4;
total number (10,2);
BEGIN

number1:=10;
number2 :=5;
total:=number1+number2;
dbms_output.put_line('sum of two number is ' ||total );
end

--output is 15 not 15.6



---------------------------
--when we want to not change value of particular variable then we use constant also adding null with zero always  give null value
declare 
number1 constant number(10,2):=10.2;
number2 number(10,4):=5.4;
total number (10,2);
BEGIN

--number1:=10;
number2 :=null;
total:=number1+number2;
dbms_output.put_line('sum of' ||number1 || 'and' ||number2|| 'is ' ||total );
end 



-------------select operation in PLSQL--------- assgine value inside the varibale with help of select statement

declare
v_id number(10);
v_name varchar2(20);

begin
select id,name into v_id,v_name from employees where employee_id=2;
dbms_output.put_line('the id and name of the employee is'||id||'name');
end;


------------------------------
create table karan (
id int,
name varchar2(20)

)

insert into karan(id,name)
values(2,'Rahul')


declare
v_id number(10);
v_name char(20);
begin
select id,name into v_id,v_name from karan where id=1;
dbms_output.put_line('the id and name  is'||v_id||v_name);
end;

-----------------------with help of this approch if in future if column data type going to change from one data type to other then variable also change them self


declare
v_id number(10);
v_name schema_name.table_name.column_name%type;

-------------------------------------------------------------------------------------------------------------------------
 
---Conditional Statement
 
declare 
a BOOLEAN :=FALSE;
begin
if a then 
dbms_output.put_line('a is true');
ELSE
dbms_output.put_line('a is false');
end if;

end;
-------------------------------------------------------------------------------------
declare 
a number :=10;
begin
if a <10
then  
dbms_output.put_line('a is less then 20');
ELSIF a>10 and a<20
then
dbms_output.put_line('a is in between 10 and 20');
ELSE
dbms_output.put_line('a is greter then 20');
end if;

end;

---------------------if else uses with help of insert and update 

declare 
a number ;
begin

select max(id) into a from karan;

if a<1
then 
delete from karan 
where id=1;

else 
insert into karan (id,name)
values(3,'golu');
end if;
end;









