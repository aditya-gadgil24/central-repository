WITH emp_ct AS (
SELECT dep_id, COUNT(*) AS staff_ct
FROM employees
GROUP BY dep_id
)
SELECT e.dep_id, ec.staff_ct
FROM employees e
JOIN emp_ct ec
ON e.dep_id = ec.dep_id
WHERE ec.staff_ct <= 0;	