-- Write query to get count of assignments in each grade
SELECT grade, COUNT(*)
FROM assignments
WHERE state = 'GRADED'
GROUP BY grade;
