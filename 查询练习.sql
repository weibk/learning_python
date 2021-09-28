-- 1. 查询出部门编号为30的所有员工

select *
from t_employees
where deptno = 30;

-- 2. 所有经理的姓名、编号和部门编号。

select ename, empno, deptno
from t_employees
where job = '经理';

-- 3. 找出奖金高于工资的员工。

select *
from t_employees
where comm > sal;

-- 4. 找出奖金高于工资60%的员工。

select *
from t_employees
where comm > sal * 0.6;

-- 5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。

select *
from t_employees
where (deptno = 10 and job = '经理')
   or (deptno = 20 and job = '分析员');

-- 6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。

select *
from t_employees
where (deptno = 10 and job = '经理')
   or (deptno = 20 and job = '分析员')
   or (job <> '经理' and job <> '武装上将' and sal >= 3000);

-- 7. 无奖金或奖金低于1000的员工。

select *
from t_employees
where ISNULL(comm) = 1
   or comm < 1000;

-- 8. 查询名字由三个字组成的员工。

select *
from t_employees
where CHAR_LENGTH(ename) = 3;

-- 9. 查询2000年以及以后入职的员工。

select *
from t_employees
where (hiredate > '2000-00-00') = 1;

-- 10. 查询所有员工详细信息，用编号升序排序

select *
from t_employees
order by empno;

-- 11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序

select *
from t_employees
order by sal desc, hiredate;

-- 12. 查询每个部门的平均工资

select a.dname as 部门, avg(sal) as 平均工资
from t_dept a
         inner join t_employees b
where a.deptno = b.deptno
group by a.dname;

-- 13. 查询每个部门的雇员数量。

select a.dname as 部门, count(a.deptno) as 人数
from t_dept a
         inner join t_employees b
where a.deptno = b.deptno
group by a.dname;

-- 14. 查询每种工作的最高工资、最低工资、人数

select job as 部门, max(sal) as 最高工资, min(sal) as 最低工资, count(job) as 人数
from t_employees
group by job;