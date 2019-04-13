drop table if exists articles;
create table articles (
  id INTEGER PRIMARY KEY autoincrement,
  title text NOT NULL,
  content text NOT NULL
);
