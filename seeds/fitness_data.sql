-- First, delete all tables if they exist
DROP TABLE IF EXISTS well_being CASCADE;
DROP TABLE IF EXISTS runners CASCADE;
DROP TABLE IF EXISTS wellbeing_diary CASCADE;
DROP TABLE IF EXISTS runs CASCADE;
DROP TABLE IF EXISTS personal_info CASCADE;

-- Enum for sex, restricting to male and female
DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sex_enum') THEN
        CREATE TYPE sex_enum AS ENUM ('male', 'female');
    END IF;
END $$;

-- Enum for fitness level, restricting to beginner, intermediate, advanced, athlete
DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'fitness_enum') THEN
        CREATE TYPE fitness_enum AS ENUM ('beginner', 'intermediate', 'advanced', 'athlete');
    END IF;
END $$;

-- Enum for activity level, restricting to sedentary, lightly_active, moderately_active, very_active
DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'activity_enum') THEN
        CREATE TYPE activity_enum AS ENUM ('sedentary', 'lightly_active', 'moderately_active', 'very_active');
    END IF;
END $$;

-- Enum for run type, restricting to interval, sprint, long distance, race
DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'run_type_enum') THEN
        CREATE TYPE run_type_enum AS ENUM ('interval', 'sprint', 'long_distance', 'race');
    END IF;
END $$;

-- Create the personal_info table (previously runners)
CREATE TABLE personal_info (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    height INT NOT NULL CHECK (height >= 0), -- in centimeters
    weight DECIMAL(5, 2) NOT NULL CHECK (weight >= 0), -- in kilograms
    bmi DECIMAL(5, 2) GENERATED ALWAYS AS (weight / (height / 100.0) ^ 2) STORED,  -- BMI calculation based on height and weight
    sex sex_enum NOT NULL,  -- Using enum for sex (male/female)
    age INT NOT NULL CHECK (age >= 0),  -- Age of the runner
    fitness_level fitness_enum NOT NULL,  -- Fitness level enum
    activity_level activity_enum NOT NULL  -- Activity level enum
);

-- Create the runs table
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES personal_info(id) ON DELETE CASCADE,
    run_type run_type_enum NOT NULL,  -- Enum for run types
    distance DECIMAL(5, 2) NOT NULL CHECK (distance >= 0),
    duration INTERVAL NOT NULL CHECK (duration >= '00:00:00'::interval),  -- Using INTERVAL for time duration
    date DATE NOT NULL,
    satisfaction INT NOT NULL CHECK (satisfaction >= 1 AND satisfaction <= 10)
);

-- Create the wellbeing_diary table
CREATE TABLE wellbeing_diary (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL REFERENCES personal_info(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    calories_in INT CHECK (calories_in >= 0),  -- User-input calories consumed
    calories_out INT CHECK (calories_out >= 0),  -- User-input calories burned
    mood INT NOT NULL CHECK (mood >= 1 AND mood <= 10),
    stress_level INT NOT NULL CHECK (stress_level >= 1 AND stress_level <= 10),
    hours_of_sleep INTERVAL NOT NULL CHECK (hours_of_sleep >= '00:00'::interval),  -- Using INTERVAL for hours of sleep (hours and minutes)
    worked_out BOOLEAN NOT NULL
);

-- Sample data for personal_info
INSERT INTO personal_info (first_name, last_name, height, weight, sex, age, fitness_level, activity_level) 
VALUES 
('John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active');

-- Sample data for runs
INSERT INTO runs (person_id, date, run_type, distance, duration, satisfaction) 
VALUES 
(1, '2023-09-15', 'interval', 5.00, '00:30:00', 8),
(1, '2023-09-16', 'sprint', 2.50, '00:15:00', 7),
(1, '2023-09-17', 'long_distance', 10.00, '01:00:00', 9),
(1, '2023-09-18', 'race', 7.00, '00:45:00', 9),
(1, '2023-09-19', 'interval', 6.00, '00:35:00', 8);

-- Sample data for wellbeing_diary
INSERT INTO wellbeing_diary (person_id, date, calories_in, calories_out, mood, stress_level, hours_of_sleep, worked_out) 
VALUES 
(1, '2023-09-15', 2500, 2000, 7, 5, '08:00', TRUE),
(1, '2023-09-16', 2200, 1800, 6, 4, '07:30', TRUE),
(1, '2023-09-17', 2700, 2100, 8, 6, '06:45', FALSE),
(1, '2023-09-18', 2600, 1900, 7, 5, '07:00', TRUE),
(1, '2023-09-19', 2400, 2000, 6, 4, '07:15', FALSE);