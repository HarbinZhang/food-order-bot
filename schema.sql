-- Tasks are steps that can be taken to complete a project
create table rate (
    id           integer primary key autoincrement not null,
    count        integer,
    user        text,
    score       integer
);