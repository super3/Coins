/*drop table if exists micro_acc;*/
create table micro_acc (
  id integer primary key autoincrement,
  acc_hash text not null,
  balance real not null,
  last_access text not null,
  ip_addr text null,
  withdraw_addr text null,
  withdraw_flag integer not null
);