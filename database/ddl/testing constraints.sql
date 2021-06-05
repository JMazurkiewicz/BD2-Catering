CREATE TABLE item_on_the_menu (
    item_id  NUMERIC(5) IDENTITY(1,1) NOT NULL,
    name     VARCHAR(20),
    cost     NUMERIC(5, 2) NOT NULL
);

INSERT INTO item_on_the_menu
VALUES (null, 0.1);

ALTER TABLE item_on_the_menu DROP CONSTRAINT test_constr;

ALTER TABLE item_on_the_menu ADD CONSTRAINT test_constr CHECK(ASCII(LEFT(name, 1)) BETWEEN ASCII('A') and ASCII('Z') );

select * from item_on_the_menu;

ALTER TABLE item_on_the_menu ADD CONSTRAINT test_constr_num CHECK (cost > 0);

drop table item_on_the_menu