-- First, delete all tables if they exist
DROP TABLE IF EXISTS wellbeing CASCADE;
DROP TABLE IF EXISTS runs CASCADE;
DROP TABLE IF EXISTS runners CASCADE;

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

-- Create the runners table
CREATE TABLE runners (
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
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,
    run_type run_type_enum NOT NULL,  -- Enum for run types
    distance DECIMAL(5, 2) NOT NULL CHECK (distance >= 0),
    duration INTERVAL NOT NULL CHECK (duration >= '00:00:00'::interval),  -- Using INTERVAL for time duration
    date DATE NOT NULL,
    satisfaction INT NOT NULL CHECK (satisfaction >= 1 AND satisfaction <= 10)
);

-- Create the wellbeing table with user-input calories
CREATE TABLE wellbeing (
    id SERIAL PRIMARY KEY,
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    calories_in INT CHECK (calories_in >= 0),  -- User-input calories consumed
    calories_out INT CHECK (calories_out >= 0),  -- User-input calories burned
    mood INT NOT NULL CHECK (mood >= 1 AND mood <= 10),
    stress_level INT NOT NULL CHECK (stress_level >= 1 AND stress_level <= 10),
    hours_of_sleep DECIMAL(3, 1) NOT NULL CHECK (hours_of_sleep >= 0),
    worked_out BOOLEAN NOT NULL
);

-- Sample data inserts
INSERT INTO runners (first_name, last_name, height, weight, sex, age, fitness_level, activity_level) 
VALUES 
('John', 'Doe', 180, 75.0, 'male', 33, 'intermediate', 'moderately_active'),
('Jane', 'Smith', 165, 65.0, 'female', 38, 'beginner', 'lightly_active');

-- Sample data for runs
INSERT INTO runs (runner_id, date, run_type, distance, duration, satisfaction) 
VALUES 
(1, '2023-09-15', 'interval', 5.00, '00:30:00', 8),
(2, '2023-09-16', 'sprint', 2.50, '00:15:00', 7);

-- Sample data for wellbeing
INSERT INTO wellbeing (runner_id, date, calories_in, calories_out, mood, stress_level, hours_of_sleep, worked_out) 
VALUES 
(1, '2023-09-15', 2500, 2000, 7, 5, 8.0, TRUE),
(2, '2023-09-16', 2000, 1800, 6, 4, 7.5, FALSE);