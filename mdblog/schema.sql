drop table if exists articles;
create table arcticles (
  id INTEGER PRIMARY KEY autoincrement,
  tittle text NOT NULL,
  content text NOT NULL
);
