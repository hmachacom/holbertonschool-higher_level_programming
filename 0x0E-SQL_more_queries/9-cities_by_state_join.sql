-- Write a script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities INNER JOIN hbtn_0d_usa.states ON hbtn_0d_usa.states.id = hbtn_0d_usa.cities.state_id ORDER BY  cities.id;
