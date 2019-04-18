-- comp9311 19s1 Project 1
-- Author: ZD Liu
-- MyMyUNSW Solutions


-- Q1:
create or replace view Q1(unswid, longname)
as select distinct r.unswid, r.longname from rooms r, semesters s, room_types rt, subjects sb, courses co, classes cl
where sb.code = 'COMP9311' and s.year = 2013 and s.term = 'S1' and rt.description = 'Laboratory' and 
co.subject = sb.id and rt.id = r.rtype and co.semester = s.id and co.id = cl.course 
;

-- Q2:


create or replace view Q2(unswid,name)
as select distinct People.unswid, People.name from People, course_enrolments ce, course_staff
where ce.course = course_staff.course and  course_staff.staff = People.id and ce.student = (select people.id from people where People.name = 'Bich Rae')
;

-- Q3:
create or replace view Q3_h1(student, semester)
as select distinct ce.student , c.semester from courses c, course_enrolments ce, subjects sub, students st
where sub.code = 'COMP9311' and ce.course = c.id and sub.id = c.subject and st.stype = 'intl' and st.id = ce.student
;
create or replace view Q3_h2(student, semester)
as select distinct ce.student , c.semester from courses c, course_enrolments ce, subjects sub, students st
where sub.code = 'COMP9021' and ce.course = c.id and sub.id = c.subject and st.stype = 'intl' and st.id = ce.student
;

create or replace view Q3(unswid, name)
as select distinct p.unswid, p.name from People p, Q3_h1 h1, Q3_h2 h2 where h1.student= p.id and  h1.student = h2.student and h1.semester = h2.semester
;

-- create or replace view Q3(unswid, name)
-- as select p.unswid, p.name from People p, Q3_h1 h1, Q3_h2 h2 where h1.student= p.id and exists(select * from h1, h2 where h1.student = h2.student and h1.semester = h2.semester )
-- ;

-- select count(*) from Q3_h1 h1 inner join Q3_h2 h2 on h1.student = h2.student and h1.semester = h2.semester;


-- Q4:
create or replace view Q4_h1(program,student)
	as select distinct pe.program, pe.student from students st, program_enrolments pe
where pe.student = st.id and st.stype = 'intl' 
;
create or replace view Q4_h11(program,count_intl)
	as select distinct h1.program, count(h1.student) from Q4_h1 h1
group by h1.program
;
create or replace view Q4_h2(program,student)
	as select distinct pe.program, pe.student from program_enrolments pe 
;

create or replace view Q4_h22(program,count_all)
	as select distinct h2.program, count(h2.student) from Q4_h2 h2 
	group by h2.program
;
create or replace view Q4_h3(program,rate)
	as select h2.program,(h1.count_intl * 1.0/h2.count_all) from Q4_h11 h1, Q4_h22 h2 where h1.program = h2.program
;
create or replace view Q4(code,name)
as select pg.code, pg.name from Q4_h3 h3, programs pg
where h3.rate >= 0.3 and h3.rate <= 0.7 and pg.id = h3.program 
;

--Q5:
create or replace view Q5_h1(course,mini_mark, count_mark)
as select ce.course, min(ce.mark) ,count(ce.mark) from course_enrolments ce group by ce.course
;
create or replace view Q5_h2(course,mini_mark, count_mark)
as select course, mini_mark,count_mark from Q5_h1 h1 where h1.mini_mark = (select max(h1.mini_mark) from Q5_h1 h1 where h1.count_mark >= 20) and h1.count_mark >= 20
;
create or replace view Q5(code,name,semester)
as select distinct sub.code, sub.name, s.name from Q5_h2 h2, subjects sub, semesters s,courses c
where sub.id = c.subject and s.id = c.semester and h2.course = c.id
;


-- Q6:
create or replace view Q6_h1(student)
as select distinct st.id from semesters s , streams str, students st,stream_enrolments se, program_enrolments pe
where st.stype = 'local' and str.name = 'Chemistry' and s.year = 2010 and s.term = 'S1' and s.id = pe.semester  and se.partof = pe.id and se.stream = str.id  and st.id = pe.student
;
create or replace view Q6_h2(student)
as select distinct st.id from semesters s ,students st, program_enrolments pe,orgunits org, programs p
where st.stype = 'intl' and org.longname = 'Faculty of Engineering' and s.year = 2010 and s.term = 'S1' and p.offeredby = org.id and s.id = pe.semester and st.id = pe.student and p.id = pe.program
;
create or replace view Q6_h3(student)
as select distinct st.id from semesters s ,students st, stream_enrolments se, program_enrolments pe, programs p
where  p.code = '3978' and s.year = '2010' and s.term = 'S1'and se.partof = pe.id and s.id = pe.semester and st.id = pe.student and p.id = pe.program
;

create or replace view Q6(num1, num2, num3)
as select (select count(h1.student)from Q6_h1 h1),(select count(h2.student)from Q6_h2 h2),(select count(h3.student)from Q6_h3 h3) 
;

-- Q7:


-- Define an SQL view Q7(name,faculty,email,starting,num_subjects) which gives the details about some Dean of Faculty at UNSW. 
-- The view should return the following details about each Dean:
-- ⚫ their name (use the name field from the People table)
-- ⚫ the faculty (use the longname field from the OrgUnits table)
-- ⚫ their email address (use the email field from People table)
-- ⚫ the date that they were appointed (use the starting date from the Affiliations table) 
-- ⚫ the number of different subjects they have participated as a staff
-- Since there is some dirty-looking data in the Affiliations table, you will need to ensure that you return only legitimate Head of School. 
-- Apply the following filters together:
-- ⚫ only choose people whose role is exactly ‘Dean’
-- ⚫ only choose people for whom this is their primary role
-- ⚫ only choose people who have taught at least one subject.
-- ⚫ only choose organisational units whose type is actually ‘Faculty’
-- Note:
-- ⚫ Two subjects are different if they have different subject codes



create or replace view Q7_h1(offeredby, count)
as select DISTINCT offeredby,count(code) FROM subjects GROUP BY offeredby;

create or replace view Q7(name, faculty, email, starting, num_subjects)
as select p.name, org.longname, p.email ,af.starting, p.id from orgunits org, people p, affiliations af, staff st, orgunit_types ot,staff_roles sr, Q7_h1 h1
where ot.name = 'Faculty'and sr.name = 'Dean' and af.isprimary = TRUE and af.staff = st.id and st.id = p.id and sr.id = af.role and org.id = h1.offeredby 
;



-- UNSW wants to know the most popular subjects. Define a SQL view Q8(subject) that lists the most popular subjects. A subject is one of the most popular subjects if there are at least 20 distinct students enrolled (via the Course_enrolments table) in at least 20 distinct courses offerings of the subject. Each tuple in the view should contain the following:
-- ⚫ the subject code (Subjects.code field) and name (Subjects.name field), in the format e.g. COMP9311 Database Systems (Note that there is a space between subject code and name)
-- Note:
-- ⚫ Some course offerings have no students enrolled in. It appears in Courses, but not in
-- Course_enrolments.
-- Q8: 
create or replace view Q8_h0(course,counts)
as SELECT course, count(student) from course_enrolments GROUP BY course
;
create or replace view Q8_h1(subject, counts)
as SELECT subject, count(id) from courses c, Q8_h0 h0 where  h0.counts >= 20 and c.id = h0.course GROUP BY subject
;
create or replace view Q8(subject)
as SELECT concat(sub.code,' ',sub.name) as ssub from subjects sub, Q8_h1 h1
where sub.id = h1.subject and h1.counts >= 20
;



-- Define SQL view Q9(year, num, unit), which gives, for each unit, the year with the greatest number of distinct international students enrolled, and the number of distinct international students enrolled for this year. The view should return the following details about each unit:
-- • year should be taken from Semesters.year field.
-- • num counts the total number of international students enrolled.
-- • unit should be taken from OrgUnits.longname field.
-- Note:
-- • you should ignore the units with no international student.
-- • In the case of ties, the same unit with different years should all be included in the result.
-- Q9:
create or replace view Q9_h0(student, offeredby,year)
as SELECT DISTINCT st.id, p.offeredby,s.year from semesters s,programs p, program_enrolments pe, students st
where st.stype = 'intl' and pe.program = p.id and pe.student = st.id and s.id = pe.semester 
;
create or replace view Q9_h01(units,counts,year)
as SELECT org.longname, count(h0.student), h0.year from Q9_h0 h0 , orgunits org
where org.id = h0.offeredby
GROUP BY org.longname,h0.year
;
create or replace view Q9_h03(unit,num)
as SELECT h01.units, max(h01.counts) from Q9_h01 h01
GROUP BY h01.units
;
create or replace view Q9(year,num,unit)
as SELECT DISTINCT h2.year,h3.num, h2.units from Q9_h03 h3, Q9_h01 h2
where h3.unit = h2.units and h3.num = h2.counts
;

-- Q10
create or replace view Q10_h1(student,course,mark)
as select ce.student, ce.course, ce.mark from course_enrolments ce, courses c, semesters s
where ce.mark >= 0 and s.year = '2011' and s.term = 'S1' and s.id = c.semester and c.id = ce.course
;
create or replace view Q10_h2(student,counts,avg_mark)
as SELECT student,count(course),avg(mark) from Q10_h1 GROUP BY student
;
create or replace view Q10_h3(rank_num,student,counts,avg_mark)
as select rank() OVER(order by avg_mark desc) as row_num,* from Q10_h2 where counts >=3
;
create or replace view Q10(unswid,name,avg_mark)
as SELECT p.unswid, p.name, cast(h3.avg_mark as numeric (4,2)) from Q10_h3 h3, people p 
WHERE  h3.rank_num <= 10  and h3.student = p.id 
;


-- Below are the rules for students’ academic standings:
-- i. If a student takes more than one course in a semester, his/her academic standing would be
-- ‘Probation’ if none of them passed, ‘Referral’ if 50% or less of the taken courses are passed,
-- and ‘Good’ otherwise.
-- ii. If a student takes only one course in a semester, he/she will receive ‘Good’ if he/she passes it,
-- and ‘Referral’ if he/she fails it.
-- Define SQL view Q11(unswid,name,academic_standing), which gives the unswid, name and academic standing of students with the unswid beginning with ‘313’ in 2011 S1. The view should return the following details about each student:
-- • unswid should be taken from People.unswid field.
-- • name should be taken from People.name field.
-- • academic standing should be defined as the rules given above. You will need to
-- display ‘Good’, ‘Probation’, ‘Referral’ for each student you found. Note:
-- • for each student, we only consider the courses in which he/she receives a not null mark. You may use Course_enrolments.mark >= 0 to retrieve a list of valid students.
-- • to pass a course, a student needs to get 50 or more in that course. (Course_enrolments.mark >= 50)
-- • don’t consider the students who never get any mark from any course in that semester.
-- Q11:
create or replace view Q11_h1(student,course,mark )
as select ce.student ,ce.course,ce.mark from  courses c,semesters s,course_enrolments ce
where s.year = '2011' and  s.term = 'S1' and ce.mark >= 0 and s.id = c.semester and c.id = ce.course
;

create or replace view Q11_h2(unswid,name,student,cou_count)
as select p.unswid,p.name,h1.student,count(h1.course)
from  Q11_h1 h1,people p
where cast(p.unswid as varchar) like '313%' and p.id = h1.student 
GROUP BY h1.student,p.unswid,p.name
;

create or replace view Q11_h10(student,counts_m)
as select h1.student,count(h1.mark)
from  Q11_h1 h1
where h1.mark>= 50
GROUP BY h1.student
;

create or replace view Q11_h3(unswid,name,student,cou_count,counts_m,rate_pass)
as select h2.unswid,h2.name,h2.student,h2.cou_count,COALESCE(h10.counts_m,0), CAST(CAST(COALESCE(h10.counts_m,0) as FLOAT)/h2.cou_count as numeric (4,2)) 
from Q11_h2 h2 LEFT JOIN Q11_h10 h10 on h10.student = h2.student
;

create or replace view Q11(unswid,name,academic_standing)
as select unswid,name,
(CASE 
	WHEN cou_count =1 and rate_pass=1 THEN
		'Good'
	WHEN cou_count=1 and rate_pass<1 THEN
		'Referral'
	WHEN cou_count <> 1 and rate_pass=0 THEN
		'Probation'
	WHEN cou_count>1 and rate_pass>0 and rate_pass<=0.5 THEN
		'Referral'
	WHEN cou_count>1 and rate_pass>0.5 THEN
		'Good'
END) as standing
from  Q11_h3
;



-- Q12:

create or replace view Q12_h1(code,name,year,term, course_id)
as select sub.code,sub.name,s.year, s.term, c.id from subjects sub, courses c, semesters s
where (s.term = 'S1' or s.term = 'S2') and sub.code like 'COMP90%' and sub.id = c.subject and s.id = c.semester
;

create or replace view Q12_h2(course,name,code,year,term, pass_count)
as select ce.course,h1.name,h1.code,h1.year,h1.term, count(ce.mark) from course_enrolments ce, Q12_h1 h1
where ce.mark >= 50 and  h1.course_id = ce.course
GROUP BY ce.course,h1.code,h1.name ,h1.term, h1.year
;
create or replace view Q12_h3(course,name,code,year,term, enrol_count)
as select ce.course,h1.name,h1.code,h1.year,h1.term, count(ce.mark) from course_enrolments ce, Q12_h1 h1
where ce.mark >= 0 and  h1.course_id = ce.course
GROUP BY ce.course,h1.code,h1.name ,h1.term, h1.year
;
create or replace view Q12_h4(course,code,name,year,term,pass_count, enrol_count, pass_rate)
as select h3.course,h2.code,h3.name,h3.year,h3.term,h2.pass_count, h3.enrol_count, CAST(CAST(h2.pass_count as FLOAT)/enrol_count as numeric (4,2)) 
from Q12_h3 h3, Q12_h2 h2
where h3.course = h2.course
;
create or replace view Q12_h5(code,name, year, s1_ps_rate)
as select h4.code,h4.name,h4.year,CAST(CAST(sum(pass_count) as FLOAT)/sum(enrol_count) as numeric (4,2)) from Q12_h4 h4
where h4.term = 'S1'
group by h4.code,h4.year,h4.name
;
create or replace view Q12_h6(code,name, year, s2_ps_rate)
as select h4.code,h4.name,h4.year,CAST(CAST(sum(pass_count) as FLOAT)/sum(enrol_count) as numeric (4,2)) from Q12_h4 h4
where h4.term = 'S2'
group by h4.code,h4.year,h4.name
;
create or replace view Q12(code, name,year, s1_ps_rate, s2_ps_rate)
as select COALESCE(h6.code,h5.code) as code, COALESCE(h6.name,h5.name) as code,COALESCE(h6.year,h5.year) as year, h5.s1_ps_rate, h6.s2_ps_rate FROM Q12_h5 h5 FULL OUTER JOIN Q12_h6 h6 on h5.code = h6.code and h5.year = h6.year
ORDER BY COALESCE(h6.code,h5.code)
;




