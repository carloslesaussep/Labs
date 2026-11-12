--1st
select id, song_title, artist, round(((coalesce(duration_ms, 0))/60000), 2) as length_in_minutes from spotification order by COALESCE(duration_ms, 0) desc limit 1;
--2nd
select count(song_title) as song_count from spotification where lower(artist) ILIKE '%drake%';
--3rd
select count(*) as love_count from spotification where lower(song_title) ILIKE '%love%';
--4th
select * from spotification where regexp_like(song_title, '.*[0-9].*');
--5th
select * from spotification order by energy desc limit 5;
--6th
select * from spotification order by danceability desc limit 3;
--7th 
select TRIM(f.value::string) as individual_artist, COUNT(*) as song_count FROM spotification, lateral FLATTEN(input => SPLIT(artist, ',')) f
group by individual_artist order by song_count DESC LIMIT 1;
--8th
select * from spotification order by energy asc limit 5;