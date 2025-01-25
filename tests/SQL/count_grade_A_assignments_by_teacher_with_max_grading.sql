-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH teacher_grades AS (
    SELECT teacher_id, COUNT(*) AS grade_count
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
),
max_grades AS (
    SELECT teacher_id
    FROM teacher_grades
    WHERE grade_count = (SELECT MAX(grade_count) FROM teacher_grades)
)
SELECT COUNT(*)
FROM assignments
WHERE grade = 'A'
AND teacher_id IN (SELECT teacher_id FROM max_grades);
