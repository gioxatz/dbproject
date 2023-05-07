INSERT INTO `schools` (`schoolID`,`name`,`email`,`phone`,`str_name`,`str_number`,`zip_code`,`city`)
VALUES
  (default,"Γενικό Λύκειο Αφάντου","afantou_gel@schools.edu","2241050000","Ρόδου", 11,"26685","Ρόδος");
  
INSERT INTO `schools` (`schoolID`,`name`,`email`,`phone`,`str_name`,`str_number`,`zip_code`,`city`)
VALUES
  (default,"4ο ΓΕΛ ΡΟΔΟΥ","2o_gel_rodou@schools.edu","2241060000","Δωδεκανήσου",57,"61303","Ρόδος"),
  (3,"2o Gel Rodo","arcu.et.pede@protonmail.edu","5273164337","Egestas Street",15,"62412"),
  (4,"3o Gel Rodou","augue.porttitor@aol.edu","5914132223","Lacinia Street",3,"12534","Long Xuyen"),
  (5,"4o Gel Rodou","et.magnis.dis@protonmail.net","7652381024","Accumsan Ave",99,"67675","Carapicuíba");
  
INSERT INTO `schools` (`schoolID`,`name`,`email`,`phone`,`str_name`,`str_number`,`zip_code`,`city`)
VALUES
  (default,"1ο Γενικό Λύκειο Κω","1o_gel_kos@schools.edu","2242055252","Δωδεκανήσου", 2,"14758","Κως");
  
  
  INSERT INTO books values(9780809501632, 1, "Experiments with Alternate Currents of High Potential and High Frequency", "Martino Fine Books", 178, "English", 3, "https://m.media-amazon.com/images/I/51pCVj4lwXL._SX331_BO1,204,203,200_.jpg", "2012 Reprint of 1904 Edition. Exact facsimile of the original edition, not reproduced with Optical Recognition Software. Illustrated. In the War of Currents era in the late 1880s, George Westinghouse and Thomas Edison became adversaries due to Edison's promotion of direct current (DC) for electric power distribution over alternating current (AC) advocated by several European companies and Westinghouse Electric based in Pittsburgh, Pennsylvania. Alternating current had first developed in Europe. Westinghouse was willing to invest in the technology and hired William Stanley, Jr. to work on an AC distribution system using step up and step down transformers of a new design in 1886. After Stanley left Westinghouse, Oliver Shallenberger took control of the AC project. Nikola Tesla joined the team after 1888. Tesla partnered with Westinghouse Electric to commercialize his particular AC system. Westinghouse had previously bought the rights to Tesla's polyphase system patents and other patents for AC transformers. This is one of Tesla's more important lectures on the subject.", default);
  INSERT INTO books values(9780081011249, 1, "Electrical Power Systems", "Butterworth-Heinemann", 815, "English", 2, "https://ars.els-cdn.com/content/image/3-s2.0-C20150061755-cov200h.gif", "Electrical Power Systems provides comprehensive, foundational content for a wide range of topics in power system operation and control. With the growing importance of grid integration of renewables and the interest in smart grid technologies it is more important than ever to understand the fundamentals that underpin electrical power systems. The book includes a large number of worked examples, and questions with answers, and emphasizes design aspects of some key electrical components like cables and breakers. The book is designed to be used as reference, review, or self-study for practitioners and consultants, or for students from related engineering disciplines that need to learn more about electrical power systems.", default);
  INSERT INTO books values(9780078022159, 1, "Database System Concepts", "McGraw Hill", 1376, "English", 4, "https://m.media-amazon.com/images/I/51cq3aAdqNL._SX402_BO1,204,203,200_.jpg", "Database System Concepts by Silberschatz, Korth and Sudarshan is now in its 7th edition and is one of the cornerstone texts of database education. It presents the fundamental concepts of database management in an intuitive manner geared toward allowing students to begin working with databases as quickly as possible. The text is designed for a first course in databases at the junior/senior undergraduate level or the first year graduate level. It also contains additional material that can be used as supplements or as introductory material for an advanced course. Because the authors present concepts as intuitive descriptions, a familiarity with basic data structures, computer organization, and a high-level programming language are the only prerequisites. Important theoretical results are covered, but formal proofs are omitted. In place of proofs, figures and examples are used to suggest why a result is true.", default);
  INSERT INTO books values(9780078022159, 2, "Database System Concepts", "McGraw Hill", 1376, "English", 2, "https://m.media-amazon.com/images/I/51cq3aAdqNL._SX402_BO1,204,203,200_.jpg", "Database System Concepts by Silberschatz, Korth and Sudarshan is now in its 7th edition and is one of the cornerstone texts of database education. It presents the fundamental concepts of database management in an intuitive manner geared toward allowing students to begin working with databases as quickly as possible. The text is designed for a first course in databases at the junior/senior undergraduate level or the first year graduate level. It also contains additional material that can be used as supplements or as introductory material for an advanced course. Because the authors present concepts as intuitive descriptions, a familiarity with basic data structures, computer organization, and a high-level programming language are the only prerequisites. Important theoretical results are covered, but formal proofs are omitted. In place of proofs, figures and examples are used to suggest why a result is true.", default);

  
  INSERT INTO author values(default, "Nikola Tesla");
  INSERT INTO author values(default, "P.S.R. Murty");
  INSERT INTO author values(default, "Avi Silberschatz");
  INSERT INTO author values(default, "Henry F. Korth");
  INSERT INTO author values(default, "S. Sudarshan");
  
  
  INSERT INTO is_author values(9780809501632, 1);
  INSERT INTO is_author values(9780081011249, 2);
  INSERT INTO is_author values(9780078022159, 3);
  INSERT INTO is_author values(9780078022159, 4);
  INSERT INTO is_author values(9780078022159, 5);

  
  
  
  

  
  INSERT INTO subjects values(default, "Electric Energy");
  INSERT INTO subjects values(default, "Ενέργεια");
  INSERT INTO keywords values(default, "Physics of Electricity");
  INSERT INTO subjects values(default, "Literary Fiction");
  INSERT INTO keywords values(default, "Electricity");
  INSERT INTO keywords VALUES(default, "Smart grids");
  INSERT INTO subjects VALUES(default, "Electric Power Engineering");
  INSERT INTO keywords VALUES(default, "Electric Systems");
  INSERT INTO subjects VALUES(default, "Databases");
  INSERT INTO keywords VALUES(default, "Systems");
  
  INSERT INTO has_subject values(9780809501632,  1);
  INSERT INTO has_keywords values( 9780809501632, 1);
  INSERT INTO has_subject values( 9780809501632,  ,3);
  INSERT INTO has_keywords values( 9780809501632,  2);
  INSERT INTO has_subject VALUES( 9780081011249, 1);
  INSERT INTO has_keywords VALUES( 9780081011249, 3);
  INSERT INTO has_subject VALUES( 9780081011249, 4);
  INSERT INTO has_keywords VALUES( 9780081011249, 2);
  INSERT INTO has_keywords VALUES( 9780081011249, 4);
  INSERT INTO has_subject VALUES( 9780078022159, 5);
  INSERT INTO has_keywords VALUES( 9780078022159, 2);
  
  INSERT INTO users VALUES(default, 1, "gioxatz", "Password1", "Giorgos", "Chatzichristodoulou");
  INSERT INTO users VALUES(default, 1, "helenchatz", "Password2", "Eleni", "Chatzichristodoulou");  
  INSERT INTO users VALUES(default, 2, "nick123", "nick123", "Nikolaos", "Albert");
  INSERT INTO users VALUES(default, 2, "chopin", "Password3", "Frederic", "Chopin");
  INSERT INTO users VALUES(default, 3, "ravel", "Password4", "Maurice", "Ravel");
  INSERT INTO users VALUES(default, 1, "gershwin", "Password5", "George", "Gershwin");
  INSERT INTO users VALUES(default, 4, "jsbach", "Password6", "Johahn Sebastian", "Bach");
  
  
  INSERT INTO `users` (`schoolID`, `name`, `surname`, `email`, `username`, `password`)
VALUES
(1, 'Γιάννης', 'Παπαδόπουλος', 'giannis1@example.com', 'giannis1', 'password1'),
(2, 'Μαρία', 'Πετροπούλου', 'maria1@example.com', 'maria1', 'password2'),
(3, 'Δημήτρης', 'Αθανασιάδης', 'dimitris1@example.com', 'dimitris1', 'password3'),
(1, 'Κωνσταντίνος', 'Παπαδάκης', 'konstantinos1@example.com', 'konstantinos1', 'password4'),
(2, 'Ελένη', 'Αντωνίου', 'eleni1@example.com', 'eleni1', 'password5'),
(3, 'Αλέξανδρος', 'Μαντάς', 'alexandros1@example.com', 'alexandros1', 'password6'),
(1, 'Αγγελική', 'Μαυρομμάτη', 'aggeliki1@example.com', 'aggeliki1', 'password7'),
(2, 'Κυριακή', 'Πανταζή', 'kyriaki1@example.com', 'kyriaki1', 'password8'),
(3, 'Στέλλα', 'Βλάχου', 'stella1@example.com', 'stella1', 'password9'),
(1, 'Γεώργιος', 'Πετρίδης', 'georgios1@example.com', 'georgios1', 'password10'),
(2, 'Αθηνά', 'Καραμάνου', 'athina1@example.com', 'athina1', 'password11'),
(3, 'Σταύρος', 'Γιαννόπουλος', 'stavros1@example.com', 'stavros1', 'password12'),
(1, 'Ιωάννα', 'Παπακωνσταντίνου', 'ioanna1@example.com', 'ioanna1', 'password13'),
(2, 'Ευαγγελία', 'Αγγελοπούλου', 'evangelia1@example.com', 'evangelia1', 'password14'),
(3, 'Νίκος', 'Κωνσταντινίδης', 'nikos1@example.com', 'nikos1', 'password15'),
(1, 'Αιμιλία', 'Κουτσουμπού', 'emilia1@example.com', 'emilia1', 'password16'))
  
  
  INSERT INTO `school_director`
VALUES
(default, 1, 'Γιάννης', 'Παπαδόπουλος', 1),
(default, 2, 'Μαρία', 'Πετροπούλου', 2),
(default, 3, 'Δημήτρης', 'Αθανασιάδης', 3)

  INSERT INTO `admin` 
VALUES
(default, 'Αριστοτέλης', 'Γεωργίου', 'admin1@example.com', 'admin1', 'adpassword1'),
(2, 'Ιπποκρατης', 'Πετροπούλου', 'admin2@example.com', 'admin2', 'adpassword2'),
  
  select b.title, sub.subject, sch.name, a.name AS authors from schools sch join books b on sch.schoolID = b.schoolID JOIN is_author ba ON b.ISBN = ba.ISBN join has_subject hs on b.ISBN = hs.ISBN join subjects sub on sub.subID = hs.subID JOIN author a ON ba.authorid = a.authorid;
				
				
SELECT b.title, GROUP_CONCAT(a.name SEPARATOR ', ') AS author
FROM books b
JOIN author ba ON b.ISBN = ba.ISBN
JOIN author a ON ba.authorid = a.authorid
WHERE b.schoolid = 1
GROUP BY b.ISBN;

SELECT b.title, GROUP_CONCAT(a.name SEPARATOR ', ') AS authors
FROM books b
JOIN is_author ba ON b.ISBN = ba.ISBN
JOIN author a ON ba.authorid = a.authorid
GROUP BY b.ISBN

SELECT GROUP_CONCAT(a.name SEPARATOR ', ') AS authors
FROM is_author ia join author a on ia.authorid = a.authorid

