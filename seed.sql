-- Populate wrestlers table
INSERT INTO wrestlers (name, finishing_move, height_feet, height_inches, weight_lbs, image_url) VALUES
('Cody Rhodes', 'Cross Rhodes', 6, 2, 220, '/images/cody_rhodes.jpg'),
('Gunther', 'Powerbomb', 6, 6, 284, '/images/gunther.jpg'),
('Nia Jax', 'Leg Drop', 6, 0, 271, '/images/nia_jax.jpg'),
('Liv Morgan', 'Oblivion', 5, 5, 119, '/images/liv_morgan.jpg'),
('Jey Uso', 'Uso Splash', 6, 2, 236, '/images/jey_uso.jpg'),
('LA Knight', 'BFT (Blunt Force Trauma)', 6, 2, 236, '/images/la_knight.jpg'),
('Tama Tonga', 'Gun Stun', 6, 0, 215, '/images/tama_tonga.jpg'),
('Tonga Loa', 'Apeshit', 6, 1, 264, '/images/tonga_loa.jpg'),
('Finn Balor', 'Coup de Grace', 5, 11, 190, '/images/finn_balor.jpg'),
('JD McDonagh', 'Devil Inside', 5, 10, 190, '/images/jd_mcdonagh.jpg'),
('Bianca Belair', 'KOD (Kiss of Death)', 5, 7, 165, '/images/bianca_belair.jpg'),
('Jade Cargill', 'Jaded', 5, 10, 160, '/images/jade_cargill.jpg'),
('Roman Reigns', 'Spear', 6, 3, 265, '/images/roman_reigns.jpg'),
('Rey Mysterio', '619', 5, 6, 174, '/images/rey_mysterio.jpg'),
('Kevin Owens', 'Stunner', 6, 0, 265, '/images/kevin_owens.jpg'),
('Sami Zayn', 'Helluva Kick', 6, 2, 212, '/images/sami_zayn.jpg'),
('Becky Lynch', 'Manhandle Slam', 5, 7, 135, '/images/becky_lynch.jpg'),
('AJ Styles', 'Phenomenal Forearm', 5, 11, 218, '/images/aj_styles.jpg'),
('Randy Orton', 'RKO', 6, 5, 290, '/images/randy_orton.jpg'),
('Charlotte Flair', 'Figure Eight', 5, 10, 143, '/images/charlotte_flair.jpg'),
('Asuka', 'Asuka Lock', 5, 3, 128, '/images/asuka.jpg'),
('Drew McIntyre', 'Claymore Kick', 6, 5, 265, '/images/drew_mcintyre.jpg'),
('Sheamus', 'Brogue Kick', 6, 3, 267, '/images/sheamus.jpg'),
('Damian Priest', 'Reckoning', 6, 5, 249, '/images/damian_priest.jpg'),
('Dominik Mysterio', 'Frog Splash', 6, 1, 190, '/images/dominik_mysterio.jpg'),
('Shinsuke Nakamura', 'Kinshasa', 6, 2, 229, '/images/shinsuke_nakamura.jpg'),
('Iyo Sky', 'Moonsault', 5, 1, 115, '/images/iyo_sky.jpg'),
('Bayley', 'Rose Plant', 5, 6, 119, '/images/bayley.jpg'),
('Dakota Kai', 'Kai-ropractor', 5, 6, 121, '/images/dakota_kai.jpg'),
('Carmella', 'Code of Silence', 5, 5, 110, '/images/carmella.jpg'),
('Alexa Bliss', 'Twisted Bliss', 5, 1, 102, '/images/alexa_bliss.jpg'),
('Omos', 'Chokeslam', 7, 3, 410, '/images/omos.jpg'),
('Braun Strowman', 'Running Powerslam', 6, 8, 385, '/images/braun_strowman.jpg'),
('Karrion Kross', 'Kross Jacket', 6, 4, 265, '/images/karrion_kross.jpg'),
('Bronson Reed', 'Tsunami', 5, 11, 330, '/images/bronson_reed.jpg'),
('Uncle Howdy', 'Sister Abigail', 6, 3, 285, '/images/uncle_howdy.jpg'),
('Jimmy Uso', 'Uso Splash', 6, 3, 251, '/images/jimmy_uso.jpg'),
('Jacob Fatu', 'Moonsault', 6, 2, 262, '/images/jacob_fatu.jpg'),
('Solo Sikoa', 'Samoan Spike', 6, 2, 252, '/images/solo_sikoa.jpg'),
('Tiffany Stratton', 'Prettiest Moonsault Ever', 5, 7, 132, '/images/tiffany_stratton.jpg'),
('Chad Gable', 'Ankle Lock', 5, 8, 202, '/images/chad_gable.jpg'),
('The Rock', 'Rock Bottom', 6, 5, 260, '/images/the_rock.jpg'),
('CM Punk', 'GTS (Go To Sleep)', 6, 2, 218, '/images/cm_punk.jpg'),
('Andrade', 'Hammerlock DDT', 5, 9, 210, '/images/andrade.jpg'),
('Carmelo Hayes', 'Nothing But Net', 5, 10, 200, '/images/carmelo_hayes.jpg'),
('Montez Ford', 'From the Heavens', 6, 1, 227, '/images/montez_ford.jpg'),
('Angelo Dawkins', 'Anointment', 6, 5, 260, '/images/angelo_dawkins.jpg'),
('Austin Theory', 'ATL (A-Town Down)', 6, 1, 220, '/images/austin_theory.jpg'),
('Grayson Waller', 'Rolling Thunder Stunner', 6, 0, 205, '/images/grayson_waller.jpg'),
('Kofi Kingston', 'Trouble in Paradise', 6, 0, 212, '/images/kofi_kingston.jpg'),
('Xavier Woods', 'Limit Break', 5, 11, 205, '/images/xavier_woods.jpg'),
('Bron Breakker', 'Spear', 6, 0, 230, '/images/bron_breakker.jpg'),
('Rhea Ripley', 'Riptide', 5, 8, 137, '/images/rhea_ripley.jpg'),
('R-Truth', 'Lie Detector', 6, 2, 220, '/images/r_truth.jpg'),
('The Miz', 'Skull-Crushing Finale', 6, 2, 221, '/images/the_miz.jpg'),
('Seth Rollins', 'Curb Stomp', 6, 2, 225, '/images/seth_rollins.jpg');



INSERT INTO championships (title_name, current_champion_id1, current_champion_id2) VALUES
('WWE Championship', 1, NULL),
('World Heavyweight Championship', 2, NULL),
('WWE Women''s Championship', 3, NULL),
('Women''s World Championship', 4, NULL),
('Intercontinental Championship', 5, NULL),
('United States Championship', 6, NULL),
('WWE Tag Team Championship', 7, 8),
('World Tag Team Championship', 9, 10),
('Women''s Tag Team Championship', 11, 12);

INSERT INTO merchandise_sales (wrestler_id, sales_amount_usd, sales_rank) VALUES
(13, 1000000.00, 1),  -- Roman Reigns
(1, 950000.00, 2),    -- Cody Rhodes
(56, 920000.00, 3),   -- Seth Rollins
(17, 900000.00, 4),   -- Becky Lynch
(11, 850000.00, 5),   -- Bianca Belair
(20, 830000.00, 6),   -- Charlotte Flair
(42, 800000.00, 7),   -- The Rock
(14, 780000.00, 8),   -- Rey Mysterio
(2, 750000.00, 9),    -- Gunther
(19, 740000.00, 10),  -- Randy Orton
(43, 730000.00, 11),  -- CM Punk
(18, 720000.00, 12),  -- AJ Styles
(21, 710000.00, 13),  -- Asuka
(5, 700000.00, 14),   -- Jey Uso
(22, 690000.00, 15),  -- Drew McIntyre
(6, 680000.00, 16),   -- LA Knight
(37, 680000.00, 17),  -- Jimmy Uso
(15, 670000.00, 18),  -- Kevin Owens
(50, 670000.00, 19),  -- Kofi Kingston
(16, 660000.00, 20),  -- Sami Zayn
(23, 650000.00, 21),  -- Sheamus
(33, 640000.00, 22),  -- Braun Strowman
(24, 630000.00, 23),  -- Damian Priest
(55, 630000.00, 24),  -- The Miz
(9, 620000.00, 25),   -- Finn Balor
(48, 620000.00, 26),  -- Austin Theory
(26, 610000.00, 27),  -- Shinsuke Nakamura
(3, 600000.00, 28),   -- Nia Jax
(44, 600000.00, 29),  -- Andrade
(28, 590000.00, 30),  -- Bayley
(51, 590000.00, 31),  -- Xavier Woods
(12, 580000.00, 32),  -- Jade Cargill
(46, 580000.00, 33),  -- Montez Ford
(31, 570000.00, 34),  -- Alexa Bliss
(39, 560000.00, 35),  -- Solo Sikoa
(4, 550000.00, 36),   -- Liv Morgan
(45, 550000.00, 37),  -- Carmelo Hayes
(27, 540000.00, 38),  -- Iyo Sky
(47, 540000.00, 39),  -- Angelo Dawkins
(34, 530000.00, 40),  -- Karrion Kross
(52, 530000.00, 41),  -- Bron Breakker
(25, 520000.00, 42),  -- Dominik Mysterio
(29, 510000.00, 43),  -- Dakota Kai
(54, 510000.00, 44),  -- R-Truth
(30, 500000.00, 45),  -- Carmella
(49, 500000.00, 46),  -- Grayson Waller
(35, 490000.00, 47),  -- Bronson Reed
(32, 480000.00, 48),  -- Omos
(40, 470000.00, 49),  -- Tiffany Stratton
(38, 460000.00, 50),  -- Jacob Fatu
(7, 450000.00, 51),   -- Tama Tonga
(41, 440000.00, 52),  -- Chad Gable
(36, 420000.00, 53),  -- Uncle Howdy
(8, 400000.00, 54),   -- Tonga Loa
(10, 350000.00, 55),  -- JD McDonagh
(53, 760000.00, 56);  -- Rhea Ripley