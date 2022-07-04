# insert into patients sql query
insert_patients_sql = ("""
   INSERT INTO patients (patient_id,first_name,middle_name,last_name,date_of_birth
					  ,gender_mfu,address,other_details)
    VALUES (1,'AHMED','ADEL','HAASSAS','1996-07-04','m','other_details','other_details')
""")
# insert into staff sql query
insert_staff_sql = ("""
    INSERT INTO staff (staff_id,first_name,middle_name,last_name,date_of_birth
				  ,gender_mfu,qualifications,other_details)
	VALUES  (1,'AHMED','ADEL','HAASSAS','1996-07-04','m','qualifications','other_details')
                                   """)
# insert into ref_calender sql query
insert_ref_calender_sql = ("""
    INSERT INTO ref_calender (calender_id,day_number,day_date,week_number,year_number ,time_hrs)
	VALUES  (1,4,'1996-07-04',5,5,5)
                  """)
# insert into medication sql query
insert_medication_sql = ("""
    INSERT INTO medication (medication_id,medication_type_code,medication_unit_cost
						,medication_name,medication_description ,other_details)
    VALUES  (1,'medication_type_code','medication_unit_cost',
			 'medication_name','medication_description','other_details')
                  """)
# insert into ref_medication_types sql query
insert_ref_medication_types_sql = ("""
    INSERT INTO ref_medication_types (medication_type_code,medication_type_description)
	VALUES  (1,'medication_type_description')
                  """)
# insert into appointments sql query
insert_ref_appointments_sql = ("""
    INSERT INTO appointments (appointment_id,patient_id,staff_id,appointment_details)
	VALUES  (1,1,1,'appointment_details')
                 """)

# insert into patients_medication sql query
insert_patients_medication_sql = ("""
    INSERT INTO patients_medication (patients_medication_id,patient_id,medication_id,
								 date_time_administered,dosage,commentss)
	VALUES  (1,1,1,'1996-07-04','dosage','commentss')
                  """)

# insert into facts sql query
insert_patients_medication_sql = ("""
    INSERT INTO facts (fact_id,appointment_id,calender_id,medication_id,medication_type_code,
								 patient_id,patients_medication,staff_id,other_details)
	VALUES  (1,1,1,1,1,1,1,1,'other_details')
                  """)

insert_queries = [insert_patients_sql, insert_staff_sql, insert_ref_calender_sql, insert_medication_sql,
                  insert_ref_medication_types_sql, insert_ref_appointments_sql, insert_patients_medication_sql, insert_patients_medication_sql]
