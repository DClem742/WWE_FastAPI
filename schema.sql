CREATE TABLE wrestlers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    finishing_move TEXT,
    height_feet INTEGER,
    height_inches INTEGER,
    weight_lbs INTEGER,
    image_url TEXT,
    theme_song_url TEXT
);

CREATE TABLE championships (
    id SERIAL PRIMARY KEY,
    title_name TEXT,
    current_champion_id1 INTEGER REFERENCES wrestlers(id),
    current_champion_id2 INTEGER REFERENCES wrestlers(id)
);

-- Create merchandise_sales table
CREATE TABLE merchandise_sales (
    id SERIAL PRIMARY KEY,
    wrestler_id INTEGER REFERENCES wrestlers(id),
    sales_amount_usd DECIMAL(10, 2),
    sales_rank INTEGER
);