USE oblig2024; 

-- Bilde
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic100','Solnedgang','2023-10-25','han100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic101','Blomstereng','2023-09-17','per100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic102','Sandstrand','2023-09-05','jen100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic103','Spesilblankt vann','2023-10-10','ant100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic104','Månen','2023-11-09','ant100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic105','Valper','2023-09-01','ant100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic106','Kattunger','2023-11-18','lin100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic107','Dyreparken','2023-08-02','eir100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic108','Snøstrom','2023-02-10','san100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic109','Hytta','2023-06-18','fra100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic110','Guttetur','2023-07-10','ole100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic111','Girls-trip','2023-07-10','mal100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic112','Konkurranser','2023-04-12','sti100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic113','New york','2023-10-03','tom100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic114','På rød løper','2023-09-17','car100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic115','Skitur','2023-04-14','mat100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic116','Landskap','2023-08-19','ant100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic117','Selfie','2023-02-20','tom100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic118','Barn som leker','2023-08-22','jul100');
insert into Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) values('pic119','Koselig peis','2023-12-12','jul100');

-- Bruker
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('han100','Hans','Hansen','hanshans@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('per100','Per','Petter','perpetter@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('jen100','Jens','Jensen','jensjen@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('ant100','Anton','Anders','antons@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('tom100','Tom','Fredrikson','tomfred@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('gar100','Garn','Nordmann','garnnord@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('sti100','Stiven','Bergensen','stivberg@gmail.no');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('mat100','Matias','Hans','matiasha@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('jul100','Julie','Bo','julieno@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('car100','Caroline','Petter','carolint@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('eir100','Eirik','Fjell','eirikfjell@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('emi100','Emil','Bjell','emilbjell@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('sof100','Sofie','Solberg','annaann@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('sil100','Slije','Stig','siljestig@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('mal100','Malin','Moen','malinmoen@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('san100','Sander','Sand','sandersand@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('knu100','Knut','Knutsen','knutknut@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('mag100','Magnus','Myge','magnusmyge@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('fra100','Frank','Fransen','frankfran@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('ole100','Ole','Olsen','oleolsen@gmail.com');
insert into Bruker(BrukerID, Fornavn, Etternavn, Epost) values('lin100','Linn','Larsen','linnlars@gmail.no');

-- Likes
INSERT INTO Likes(BildeID,BrukerID)
VALUES
-- Likes for pic100
('pic100', 'han100'),
('pic100', 'per100'),
('pic100', 'jen100'),
('pic100', 'ant100'),
('pic100', 'tom100'),
('pic100', 'gar100'),
('pic100', 'sti100'),
('pic100', 'mat100'),

-- Likes for pic101
-- Ingen likes

-- Likes for pic102
('pic102', 'sof100'),
('pic102', 'sil100'),

-- Likes for pic103
('pic103', 'han100'),
('pic103', 'per100'),
('pic103', 'jen100'),
('pic103', 'ant100'),
('pic103', 'tom100'),
('pic103', 'gar100'),
('pic103', 'sti100'),
('pic103', 'mat100'),
('pic103', 'jul100'),
('pic103', 'car100'),
('pic103', 'eir100'),
('pic103', 'emi100'),
('pic103', 'sof100'),
('pic103', 'sil100'),
('pic103', 'mal100'),
('pic103', 'san100'),
('pic103', 'knu100'),
('pic103', 'mag100'),
('pic103', 'fra100'),
('pic103', 'ole100'),
('pic103', 'lin100'),

-- Likes for pic104
('pic104', 'knu100'),
('pic104', 'mag100'),

-- Likes for pic105
-- Ingen likes

-- Likes for pic106
('pic106', 'lin100'),
('pic106', 'han100'),
('pic106', 'per100'),
('pic106', 'jen100'),
('pic106', 'ant100'),

-- Likes for pic107
('pic107', 'tom100'),
('pic107', 'gar100'),
('pic107', 'sti100'),
('pic107', 'mat100'),

-- Likes for pic108
('pic108', 'han100'),
('pic108', 'per100'),
('pic108', 'jen100'),
('pic108', 'ant100'),
('pic108', 'tom100'),
('pic108', 'gar100'),
('pic108', 'sti100'),
('pic108', 'mat100'),
('pic108', 'jul100'),
('pic108', 'car100'),
('pic108', 'eir100'),
('pic108', 'emi100'),
('pic108', 'sof100'),
('pic108', 'sil100'),
('pic108', 'mal100'),
('pic108', 'san100'),

-- Likes for pic109
-- Ingen likes

-- Likes for pic110
('pic110', 'mal100'),
('pic110', 'san100'),
('pic110', 'sof100'),

-- Likes for pic111
('pic111', 'han100'),
('pic111', 'per100'),
('pic111', 'jen100'),
('pic111', 'ant100'),
('pic111', 'tom100'),
('pic111', 'gar100'),
('pic111', 'sti100'),
('pic111', 'mat100'),
('pic111', 'jul100'),
('pic111', 'car100'),
('pic111', 'eir100'),
('pic111', 'emi100'),
('pic111', 'sof100'),
('pic111', 'sil100'),
('pic111', 'mal100'),
('pic111', 'san100'),
('pic111', 'knu100'),
('pic111', 'mag100'),
('pic111', 'fra100'),
('pic111', 'ole100'),
('pic111', 'lin100'),

-- Likes for pic112
('pic112', 'fra100'),
('pic112', 'ole100'),

-- Likes for pic113
('pic113', 'lin100'),
('pic113', 'han100'),
('pic113', 'per100'),
('pic113', 'jen100'),
('pic113', 'ant100'),

-- Likes for pic114
('pic114', 'tom100'),
('pic114', 'gar100'),
('pic114', 'sti100'),
('pic114', 'mat100'),

-- Likes for pic115
('pic115', 'han100'),
('pic115', 'per100'),
('pic115', 'jen100'),
('pic115', 'ant100'),
('pic115', 'tom100'),
('pic115', 'gar100'),
('pic115', 'sti100'),
('pic115', 'mat100'),
('pic115', 'jul100'),
('pic115', 'car100'),
('pic115', 'eir100'),
('pic115', 'emi100'),
('pic115', 'sof100'),
('pic115', 'sil100'),
('pic115', 'mal100'),
('pic115', 'san100'),
('pic115', 'knu100'),
('pic115', 'mag100'),
('pic115', 'fra100'),

-- Likes for pic116
-- Ingen likes

-- Likes for pic117
('pic117', 'mal100'),
('pic117', 'san100'),

-- Likes for pic118
('pic118', 'knu100'),
('pic118', 'mag100'),
('pic118', 'sof100'),


('pic119', 'fra100'),
('pic119', 'ole100');

-- Kommentar
INSERT INTO Kommentar(BildeID,BrukerID,Kommentaren)
VALUES

-- Kommentarer til pic100
('pic100', 'sti100', 'Nydelig solnedgang!'),
('pic100', 'lin100', 'Fantastisk utsikt!'),
('pic100', 'knu100', 'Vakre farger i himmelen.'),
('pic100', 'eir100', 'Dette bildet er magisk.'),
('pic100', 'tom100', 'Solen går ned som en drøm.'),

-- Kommentarer til pic101
('pic101', 'fra100', 'Fantastiske blomster!'),
('pic101', 'sof100', 'Blomsterprakten imponerer.'),
('pic101', 'gar100', 'Naturens underverker.'),

-- Kommentarer til pic102
('pic102', 'ant100', 'Vakker natur!'),
('pic102', 'ole100', 'Dette bildet er nydelig.'),
('pic102', 'jen100', 'Skogens ro.'),
('pic102', 'san100', 'Flott sted å slappe av.'),
('pic102', 'tom100', 'Rolig og harmonisk omgivelse.'),

-- Kommentarer til pic103
-- Ingen kommentarer

-- Kommentarer til pic104
('pic104', 'han100', 'Krystallklart vann!'),
('pic104', 'per100', 'Speilblankt hav.'),
('pic104', 'jen100', 'Ingenting kan sammenlignes.'),
('pic104', 'ant100', 'Havet er som glass.'),
('pic104', 'tom100', 'Forfriskende utsikt.'),

-- Kommentarer til pic105
('pic105', 'han100', 'Første kommentar!'),
('pic105', 'per100', 'Jeg liker de ikke'),
('pic105', 'jen100', 'Katter er bedre'),
('pic105', 'ant100', 'Nattens skjønnhet.'),
('pic105', 'tom100', 'Stjernehimmelen er magisk.'),
('pic105', 'gar100', 'Måneskinnets glød.'),
('pic105', 'sti100', 'Nattens mysterium.'),
('pic105', 'mat100', 'Hundeglede i bilder.'),
('pic105', 'jul100', 'Små lodne venner.'),
('pic105', 'car100', 'Barnas kreative verden.'),
('pic105', 'eir100', 'Smårollinger i aksjon.'),
('pic105', 'emi100', 'Uendelig moro med barna.'),
('pic105', 'sof100', 'Hvor mange er det?'),
('pic105', 'sil100', 'Er de til salgs?'),
('pic105', 'mal100', 'Tipper det bråker mye'),
('pic105', 'san100', 'Ewww. Full av lopper'),
('pic105', 'knu100', 'Herlig! Så lodne'),
('pic105', 'mag100', 'Hva heter den brune og hvite?'),
('pic105', 'fra100', 'Savner hunden min, rip, fido.'),
('pic105', 'ole100', 'Uskyldig liten tass'),
('pic105', 'lin100', 'Ser litt ut som kaniner'),

-- Kommentarer til pic106
-- Ingen kommentarer

-- Kommentarer til pic107
('pic107', 'han100', 'Kattunger som leker!'),
('pic107', 'ant100', 'Herlig kattungekaos.'),
('pic107', 'tom100', 'Sprellende kattunger i aksjon.'),

-- Kommentarer til pic108
-- Ingen kommentarer

-- Kommentarer til pic109
('pic109', 'han100', 'Snøstormen herjer!'),
('pic109', 'per100', 'Kaldt og vakkert.'),
('pic109', 'jen100', 'Magisk vinterstemning.'),
('pic109', 'ant100', 'Snøfnugg i luften.'),
('pic109', 'tom100', 'Naturens styrke i snøstorm.'),

-- Kommentarer til pic110
('pic110', 'mal100', 'Hytta i skogen!'),
('pic110', 'sil100', 'Rolig og avslappende.'),
('pic110', 'mat100', 'Eventyr i hytta i skogen.'),

-- Kommentarer til pic111
('pic111', 'han100', 'Guttetur på sitt beste!'),
('pic111', 'per100', 'Morsomme minner skapes.'),
('pic111', 'jen100', 'Turkamerater i aksjon.'),
('pic111', 'ant100', 'Eventyr i fjellheimen.'),
('pic111', 'tom100', 'Skogens fred og ro.'),
('pic111', 'gar100', 'Hyttekos i skogsmiljø.'),
('pic111', 'sti100', 'Sammen på tur'),
('pic111', 'mat100', 'Fine farger.'),
('pic111', 'jul100', 'Hva er dette?'),
('pic111', 'car100', 'Hvor er dette.'),
('pic111', 'eir100', 'Noen ganger, ja takk.'),
('pic111', 'emi100', 'Uten spesielle tiltak.'),
('pic111', 'sof100', 'Aner ikke hva jeg ser på'),
('pic111', 'sil100', 'Tilfeldig kommentar'),
('pic111', 'mal100', 'Hva driver du med?'),
('pic111', 'san100', 'Hvordan har du gjort dette?'),
('pic111', 'knu100', 'Nei, takk.'),
('pic111', 'mag100', 'Send meg oppskriften?'),
('pic111', 'fra100', 'Savner deg.'),
('pic111', 'ole100', 'Veldig sent på kvelden'),
('pic111', 'lin100', 'Hvorfor gul?'),

-- Kommentarer til pic112
-- Ingen kommentarer

-- Kommentarer til pic113
('pic113', 'sil100', 'Spennende konkurranser!'),
('pic113', 'emi100', 'Adrenalinpumpende aktiviteter.'),
('pic113', 'mal100', 'Tøffe utfordringer.'),
('pic113', 'mat100', 'Vinnerinstinkt i aksjon.'),
('pic113', 'sof100', 'Konkurranseglede i bilder.'),

-- Kommentarer til pic114
('pic114', 'han100', 'New York, den sover aldri!'),
('pic114', 'ole100', 'Storbyeventyr i verdensklasse.'),
('pic114', 'sof100', 'Drømmenes by i virkeligheten.'),
('pic114', 'per100', 'Utforskning av The Big Apple.'),
('pic114', 'emi100', 'Shopping og moro.'),
('pic114', 'gar100', 'Storbyliv og eventyr.'),
('pic114', 'knu100', 'Venner i byens pulserende liv.'),
('pic114', 'lin100', 'Mitt hjerte i New York.'),

-- Kommentarer til pic115
('pic115', 'eir100', 'På den røde løperen!'),
('pic115', 'sof100', 'Glamour og stjerner.'),
('pic115', 'emi100', 'Livet som en filmstjerne.'),
('pic115', 'ole100', 'Rød løper øyeblikk.'),
('pic115', 'han100', 'Stil og eleganse i Hollywood.'),

-- Kommentarer til pic116
-- Ingen kommentarer

-- Kommentarer til pic117
('pic117', 'lin100', 'Fantastisk landskap!'),
('pic117', 'han100', 'Naturperler overalt.'),
('pic117', 'per100', 'Eventyrlige omgivelser.'),
('pic117', 'jul100', 'Naturens vinterprakt.'),
('pic117', 'mal100', 'Skihelt i aksjon.'),
('pic117', 'ole100', 'Høydepunkter på skituren.'),
('pic117', 'jen100', 'Sjelden vakre naturskjønnheter.'),
('pic117', 'ant100', 'Naturglede og utforskning.'),

-- Kommentarer til pic118
('pic118', 'tom100', 'Smil, la oss ta en selfie'),
('pic118', 'gar100', 'Selvportrett i fokus.'),
('pic118', 'sti100', 'Capture the moment.'),
('pic118', 'mat100', 'Selfie-moro med venner.'),
('pic118', 'jul100', 'Skap minner, ta selfier!'),

-- Kommentarer til pic119
('pic119', 'car100', 'Lekende barn er lykkelige!'),
('pic119', 'sof100', 'Barndommens glede.');

-- Emneknagg

INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4515','#VakreMolde');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4514','#Blomster');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4513','#MoldeTur');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4512','#Beach');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4511','#MoldeVann');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4510','#HunderForLife');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4509','#Kjedelig');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4508','#ElskerKatter');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4507','#Vinter');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4506','#Snøstorm');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4505','#Hyttetur');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4504','#GuttaiMolde');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4503','#Sol');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4502','#Konkurranse');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4501','#NewYork');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4500','#Glamorous');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4499','#Ingen');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4498','#Utsikt');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4497','#Selfie');
INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES('4496','#ForeldreLivet');

-- TagForLikes

INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic100','4515');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic101','4514');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic102','4513');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic103','4512');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic104','4511');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic105','4510');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic106','4515');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic107','4508');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic108','4507');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic109','4506');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic110','4505');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic111','4504');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic112','4515');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic113','4502');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic114','4501');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic115','4500');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic116','4499');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic117','4515');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic118','4497');
INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES ('pic119','4496');