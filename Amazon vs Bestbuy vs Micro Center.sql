drop table if exists gpu_kaggle CASCADE; -- to drop relationship between tables
drop table if exists microcenter CASCADE;
drop table if exists bestbuy CASCADE;
drop table if exists microcenter_filtered CASCADE;
drop table if exists bestbuy_filtered CASCADE;


create table gpu_kaggle(
	name varchar primary key not null,	
	brand varchar not null,	
	model varchar not null,	
	keywords varchar not null,
	memory varchar not null,
	memory_interface varchar not null,	
	length varchar,	
	interface varchar not null,	
	chipset varchar not null,
	base_clock varchar not null,	
	clock_speed	varchar not null,
	frame_sync varchar,
	amazon varchar);
	

create table microcenter(
	name varchar primary key not null,	
	prices varchar not null);
	
create table bestbuy(
	title varchar primary key not null,	
	prices varchar not null);
	
create table microcenter_filtered(
	gpu_name varchar primary key not null,	
	microcenter_name varchar not null,
	microcenter_price varchar not null);
	
create table bestbuy_filtered(
	gpu_name varchar primary key not null,	
	bestbuy_name varchar not null,
	bestbuy_price varchar not null);
	
select * from gpu_kaggle;
select * from microcenter;
select * from bestbuy;
select * from microcenter_filtered;
select * from bestbuy_filtered;

alter table microcenter_filtered add constraint fk_name_micro
foreign key(gpu_name) references gpu_kaggle(name);
alter table bestbuy_filtered add constraint fk_name_best
foreign key(gpu_name) references gpu_kaggle(name);

select g.name, g.amazon, m.microcenter_price
from gpu_kaggle as g
inner join microcenter_filtered as m
on g.name=m.gpu_name;

select g.name, g.amazon, b.bestbuy_price
from gpu_kaggle as g 
inner join bestbuy_filtered as b
on g.name=b.gpu_name;

