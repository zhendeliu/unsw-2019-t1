-- comp9311 19s1 Project 1
-- Author: ZD Liu
-- MyMyUNSW Solutions


-- Q1:

create or replace view Q1(unswid, longname)
as select distinct r.unswid, r.longname from rooms r, semesters s, room_types rt, subjects sb, courses co,classes cl
where sb.code = 'COMP9311' and s.year = 2013 and s.term = 'S1' and rt.description = 'Laboratory' and 
co.subject = sb.id and rt.id = r.rtype and co.semester = s.id and cl.room = r.id and cl.course = co.id
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
-- Q7:  
create or replace view Q7_h1(staff,sub_id) 
as select DISTINCT cf.staff,sub.id FROM course_staff cf, courses c, subjects sub                                  
where cf.course = c.id and c.subject = sub.id                                                                                         
GROUP BY cf.staff ,sub.id
;

create or replace view Q7_h2(staff,count) 
as select DISTINCT staff,count(sub_id) FROM Q7_h1 
GROUP BY staff
;

create or replace view Q7(name, faculty, email, starting, num_subjects)      
as select DISTINCT p.name, org.longname, p.email ,af.starting, h1.count              
from orgunits org, people p, affiliations af, staff st, orgunit_types ot,staff_roles sr, Q7_h2 h1                                                                         
where ot.name = 'Faculty'and sr.name = 'Dean' and af.isprimary = TRUE and h1.count >= 1 and h1.staff = af.staff and af.staff = st.id                                      
and st.id = p.id and sr.id = af.role  and ot.id = org.utype and af.orgunit = org.id  ;


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

-- Q12:
-- Q12:
create or replace view Q12_h0(course_id, term_count)
as select c.subject, count(s.term) from semesters s, courses c
where (s.term = 'S1' or s.term = 'S2') and (s.year >= 2003 or s.year <= 2012) and s.id = c.semester
GROUP BY c.subject;



create or replace view Q12_h1(code,name,year,term, course_id)
as select sub.code,sub.name,s.year, s.term, c.id from subjects sub,semesters s,courses c, Q12_h0 h0
where h0.term_count >= 20 and sub.code like 'COMP90%' and sub.id = h0.course_id and s.id = c.semester and h0.course_id = c.subject
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
create or replace view Q12_h22(course,name,code,year,term, fail_count)
as select ce.course,h1.name,h1.code,h1.year,h1.term, count(ce.mark) from course_enrolments ce, Q12_h1 h1
where ce.mark < 50 and ce.mark >= 0 and  h1.course_id = ce.course
GROUP BY ce.course,h1.code,h1.name ,h1.term, h1.year
;
create or replace view Q12_h23(course,name,code,year,term, pass_count)
as select h22.course,h22.name,h22.code,h22.year,h22.term, h3.enrol_count-h22.fail_count from Q12_h22 h22, Q12_h3 h3
where h22.course = h3.course
;

create or replace view Q12_h24(course,name,code,year,term, pass_count)
as select * from Q12_h2 UNION select * from Q12_h23
;

create or replace view Q12_h4(course,code,name,year,term,pass_count, enrol_count, pass_rate)
as select h3.course,h2.code,h3.name,h3.year,h3.term,h2.pass_count, h3.enrol_count, CAST(CAST(h2.pass_count as FLOAT)/enrol_count as numeric (4,2)) 
from Q12_h3 h3, Q12_h24 h2
where h3.course = h2.course
;
create or replace view Q12_h5(code,name, year, s1_ps_rate)
as select h4.code,h4.name,substring(cast(h4.year as varchar),3,4),CAST(CAST(sum(pass_count) as FLOAT)/sum(enrol_count) as numeric (4,2)) from Q12_h4 h4
where h4.term = 'S1'
group by h4.code,h4.year,h4.name
;
create or replace view Q12_h6(code,name, year, s2_ps_rate)
as select h4.code,h4.name,substring(cast(h4.year as varchar),3,4),CAST(CAST(sum(pass_count) as FLOAT)/sum(enrol_count) as numeric (4,2)) from Q12_h4 h4
where h4.term = 'S2'
group by h4.code,h4.year,h4.name
;
create or replace view Q12(code, name,year, s1_ps_rate, s2_ps_rate)
as select COALESCE(h6.code,h5.code) as code, COALESCE(h6.name,h5.name) as code,COALESCE(h6.year,h5.year) as year, h5.s1_ps_rate, h6.s2_ps_rate FROM Q12_h5 h5 FULL OUTER JOIN Q12_h6 h6 on h5.code = h6.code and h5.year = h6.year
ORDER BY COALESCE(h6.code,h5.code)
;


