-- SQLite


-- id               --> zodat je weet hoeveel gerechten je hebt
-- Gerecht          --> naam van het gerecht
-- Hoofd_ingredient --> Kip, vis, Vegetarish & anders
-- Sub_ingredient   --> pasta, rijst, aardappel, soep, sla
-- herhaling_score  --> bijvoorbeeld; er mag maar 1 keer een gerecht worden gekozen met score 0 (dus als taco's en swoarma)
                    --> 1 mag maar 1 keer voorkomen, maar (bv soep, maar mag wel in combinatie met taco's)
                    
    -- regels die ik wil
    -- max 1 keer soep
    -- max 1 keer slecht eten (zoals, taco's en swoarma)
    -- max 1 keer vis 
    -- max 1 keer stampot
    -- max 2 keer pasta
    -- max 3 keer rijst
    -- max 3 keer vega
    -- max 3 keer kip
    -- min 1 keer vis
    -- min 1 keer kip
    -- min 1 keer vega
    
INSERT INTO gerechten VALUES (5, 'tacos', 'anders', 'gehakt', 0);