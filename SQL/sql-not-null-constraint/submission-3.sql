

create table products(
    name text NOT NULL DEFAULT 'Unknown',
    price Integer NOT NULL,
    quantity integer default 0);


-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
