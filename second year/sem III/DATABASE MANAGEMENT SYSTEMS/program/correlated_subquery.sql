drop table orders;
drop table customers;
create table customer
( cust_id number(4) primary key,
  cust_name varchar2(40),
  city varchar2(30)
);
create table orders
( order_id number(4) primary key,
  cust_id number(4) references customer (cust_id),
  order_amount number(8)
);
 insert into customer values (1,'amit sharma','delhi');
 insert into customer values (2,'priya metha','mumbai');
 insert into customer values (3,'ravi kumar','bengaluru');
 insert into customer values (4,'neha singh','kolkata');
 insert into customer values (5,'arjun reddy','hydrabad');
 commit;
 insert into orders values (101,1,4500);
 insert into orders values (102,1,7000);
 insert into orders values (103,2,3200);
 insert into orders values (104,3,8500);
 insert into orders values (105,4,2100);
 commit;
 select * from customer;
 select * from orders;
 select * from customer;
 select * from orders;
 --FIND CUSTOMER WHOSE MAXIMUM ORDER AMOUNT IS GREATER THAN 6000
 select * from customer x where 6000<
( select max (order_amount) from orders y where y.cust_id=x.cust_id);
 -- Non-correlated subquery
 --find customer who made orders greater than 6000
 select cust_id from orders where order_amount > 6000;
 select * from customer where cust_id in
( select cust_id from orders where order_amount > 6000);
