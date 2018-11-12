-- Tasks are steps that can be taken to complete a project
create table user_rate (
    id           integer primary key autoincrement not null,
    count        integer,
    user        text,
    score       integer,
    channel     text
);

create table restaurant_rate (
    id           integer primary key autoincrement not null,
    count        integer,
    restaurant   text,
    score       integer,
    channel     text
);