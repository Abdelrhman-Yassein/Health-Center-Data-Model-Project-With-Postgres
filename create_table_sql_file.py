# CREATE DATABASE TABLE

# create Patient table sql query
patient_table = ("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id      INT NOT NULL PRIMARY KEY,
        first_name      VARCHAR(150) NOT NULL ,
        middle_name     VARCHAR(150) NOT NULL,
        last_name       VARCHAR(150) NOT NULL,
        date_of_birth   DATE NOT NULL,
        gender_mfu      VARCHAR(1) NOT NULL,
        address         TEXT NOT NULL,
        other_details   TEXT NULL
    )
""")

# create staff table sql query
staff_table = ("""
            CREATE TABLE IF NOT EXISTS staff (
                staff_id        INT NOT NULL PRIMARY KEY ,
                first_name      VARCHAR(150) NOT NULL ,
                middle_name     VARCHAR(150) NOT NULL ,
                last_name       VARCHAR(150) NOT NULL ,
                date_of_birth   DATE NOT NULL,
                gender_mfu      VARCHAR(1) NOT NULL ,
                qualifications  TEXT NOT NULL ,
                other_details   TEXT NULL 
            )
""")
# create ref_calender table sql query
ref_calender_table = ("""
    CREATE TABLE IF NOT EXISTS ref_calender (
        calender_id   INT NOT NULL PRIMARY KEY ,
        day_number    INT NOT NULL ,
        day_date      DATE NOT NULL,
        week_number   INT NOT NULL ,
        year_number   INT NOT NULL ,
        time_hrs      INT NOT NULL
    )
""")
# create medication table sql query
medication_table = ("""
        CREATE TABLE medication (
            medication_id          INT NOT NULL PRIMARY KEY ,
            medication_type_code   TEXT NOT NULL ,
            medication_unit_cost   VARCHAR(100) NOT NULL ,
            medication_name        VARCHAR(200) NOT NULL,
            medication_description TEXT NOT NULL ,
            other_details          TEXT NULL
        )
""")
# create ref_medication table sql query
ref_medication_types_table = ("""
        CREATE TABLE IF NOT EXISTS ref_medication_types (
            medication_type_code         INT NOT NULL PRIMARY KEY ,
            medication_type_description  TEXT NOT NULL 
        )
""")
# create appointments table sql query
appointments_table = ("""
        CREATE TABLE appointments (
            appointment_id         INT NOT NULL PRIMARY KEY ,
            patient_id             INT NOT NULL REFERENCES patients(patient_id),
            staff_id               INT NOT NULL REFERENCES staff(staff_id),
            appointment_details    TEXT NOT NULL 
        )
""")

# create patients_medication table sql query
patients_medication_table = ("""
        CREATE TABLE IF NOT EXISTS patients_medication (
            patients_medication_id    INT NOT NULL PRIMARY KEY,
            patient_id                INT NOT NULL REFERENCES patients(patient_id),
            medication_id             INT NOT NULL REFERENCES medication(medication_id) ,
            date_time_administered    DATE NOT NULL ,
            dosage                    TEXT NOT NULL ,
            commentss                  TEXT NULL
        )
""")
# create facts table sql query
facts_table = ("""
        CREATE TABLE IF NOT EXISTS facts (
            fact_id                INT NOT NULL PRIMARY KEY ,
            appointment_id         INT NOT NULL REFERENCES appointments(appointment_id) ,
            calender_id            INT NOT NULL REFERENCES ref_calender(calender_id) ,
            medication_id          INT NOT NULL REFERENCES medication(medication_id) ,
            medication_type_code   INT NOT NULL REFERENCES  ref_medication_types(medication_type_code) ,
            patient_id             INT NOT NULL REFERENCES patients(patient_id) ,
            patients_medication    INT NOT NULL REFERENCES patients_medication(patients_medication_id),
            staff_id               INT NOT NULL REFERENCES staff(staff_id) ,
            other_details          TEXT NULL
        )
""")

# create table queries lis
create_table_queries = [patient_table, staff_table, ref_calender_table, medication_table,
                        ref_medication_types_table, appointments_table, patients_medication_table, facts_table]
