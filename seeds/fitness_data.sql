-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS wellbeing CASCADE;  
DROP TABLE IF EXISTS runs CASCADE;  
DROP TABLE IF EXISTS runners CASCADE;  

-- Create sequences for each table
CREATE SEQUENCE IF NOT EXISTS runners_id_seq;
CREATE SEQUENCE IF NOT EXISTS runs_id_seq;
CREATE SEQUENCE IF NOT EXISTS wellbeing_id_seq;

-- Create the runners table
CREATE TABLE runners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    height INT NOT NULL, -- in centimetres
    weight INT NOT NULL, -- in kilograms, turn innto decimals
    gender VARCHAR(10) NOT NULL, -- fix options to male/female/other
    dob DATE NOT NULL,
    age INT NOT NULL,
    fitness_level INT NOT NULL,  -- 1=Beginner, 2=Intermediate, 3=Advanced, 4=Athlete - revisit type
    activity_level INT NOT NULL  -- 1=Sedentary, 2=Lightly active, 3=Moderately active, 4=Very active - revisit type
);

-- Create the runs table
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,  -- Foreign key to runners table with cascade
    run_type INT NOT NULL CHECK (run_type >= 1 AND run_type <= 4),  -- 1='Interval', 2='Sprint', 3='Long distance', 4='Race'
    distance DECIMAL(5, 2) NOT NULL,  -- Distance in kilometers
    duration INT NOT NULL,  -- Duration in minutes - change to interval
    date DATE NOT NULL,  -- Date of the run
    satisfaction INT NOT NULL CHECK (satisfaction >= 1 AND satisfaction <= 10)  -- Added satisfaction field
);

-- Create the wellbeing table
CREATE TABLE wellbeing (
    id SERIAL PRIMARY KEY,
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,  -- Foreign key to runners table with cascade
    date DATE NOT NULL,
    calories INT NOT NULL CHECK (calories >= 0 AND calories <= 10000),  -- Calories consumed
    water INT NOT NULL CHECK (water >= 0 AND water <= 5),  -- Water intake in liters - change to decimal
    mood INT NOT NULL CHECK (mood >= 1 AND mood <= 10),  -- Mood on a scale of 1-10
    stress_level INT NOT NULL CHECK (stress_level >= 1 AND stress_level <= 10),  -- Stress level on a scale of 1-10
    hours_of_sleep DECIMAL(3, 1) NOT NULL,  -- Hours of sleep (e.g., 7.5) change to time/interval
    worked_out BOOLEAN NOT NULL  -- Whether they worked out that day (true/false)
);

INSERT INTO runners (id, first_name, last_name, gender, dob, height, weight, fitness_level, activity_level, age) 
VALUES 
(1, 'John', 'Doe', 'Male', '1990-01-15', 180, 75, 2, 3, EXTRACT(YEAR FROM AGE('1990-01-15'::date))),  -- John Doe
(2, 'Jane', 'Smith', 'Female', '1985-08-25', 165, 65, 1, 2, EXTRACT(YEAR FROM AGE('1985-08-25'::date)));

-- Insert  data into runs table
INSERT INTO runs (runner_id, date, run_type, distance, duration, satisfaction) 
VALUES (1, '2023-09-15', 1, 5.00, 30, 8);  -- Using runner_id 1, run_type 'Interval'

INSERT INTO runs (runner_id, date, run_type, distance, duration, satisfaction) 
VALUES (2, '2023-09-16', 2, 2.50, 15, 7);  -- Using runner_id 2, run_type 'Sprint'

-- Insert data into wellbeing table
INSERT INTO wellbeing (runner_id, date, calories, water, mood, stress_level, hours_of_sleep, worked_out) 
VALUES (1, '2023-09-15', 2500, 2, 7, 5, 8.0, TRUE);  -- Data for runner_id 1

INSERT INTO wellbeing (runner_id, date, calories, water, mood, stress_level, hours_of_sleep, worked_out) 
VALUES (2, '2023-09-16', 2000, 3, 6, 4, 7.5, FALSE); 