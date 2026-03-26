# ============================================================
#  PySpark – All Joins Demo with 3 DataFrames
# ============================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("AllJoinsDemo") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ─────────────────────────────────────────
#  1. Create 3 DataFrames (3 values each)
# ─────────────────────────────────────────

# DataFrame 1 – Employees
df_employees = spark.createDataFrame(
    [(1, "Alice",  10),
     (2, "Bob",    20),
     (3, "Charlie",30)],
    ["emp_id", "emp_name", "dept_id"]
)

# DataFrame 2 – Departments
df_departments = spark.createDataFrame(
    [(10, "Engineering"),
     (20, "Marketing"),
     (40, "Finance")],          # dept_id 40 has no matching employee
    ["dept_id", "dept_name"]
)

# DataFrame 3 – Salaries
df_salaries = spark.createDataFrame(
    [(1, 90000),
     (2, 75000),
     (4, 60000)],               # emp_id 4 has no matching employee
    ["emp_id", "salary"]
)

print("\n========== Source DataFrames ==========")
print("── Employees ──"); df_employees.show()
print("── Departments ──"); df_departments.show()
print("── Salaries ──"); df_salaries.show()

# ─────────────────────────────────────────
#  2. INNER JOIN
#     Returns only matching rows in BOTH DataFrames
# ─────────────────────────────────────────
print("\n========== INNER JOIN (Employees ⟕ Departments) ==========")
inner = df_employees.join(df_departments, on="dept_id", how="inner")
inner.show()

# ─────────────────────────────────────────
#  3. LEFT JOIN  (left outer)
#     All rows from left + matching from right; NULL if no match
# ─────────────────────────────────────────
print("\n========== LEFT JOIN (Employees ⟕ Departments) ==========")
left = df_employees.join(df_departments, on="dept_id", how="left")
left.show()

# ─────────────────────────────────────────
#  4. RIGHT JOIN  (right outer)
#     All rows from right + matching from left; NULL if no match
# ─────────────────────────────────────────
print("\n========== RIGHT JOIN (Employees ⟖ Departments) ==========")
right = df_employees.join(df_departments, on="dept_id", how="right")
right.show()

# ─────────────────────────────────────────
#  5. FULL OUTER JOIN
#     All rows from both; NULL where no match
# ─────────────────────────────────────────
print("\n========== FULL OUTER JOIN (Employees ⟗ Departments) ==========")
full_outer = df_employees.join(df_departments, on="dept_id", how="full")
full_outer.show()

# ─────────────────────────────────────────
#  6. CROSS JOIN  (Cartesian product)
#     Every row from left × every row from right
# ─────────────────────────────────────────
print("\n========== CROSS JOIN (Employees × Salaries) ==========")
cross = df_employees.crossJoin(df_salaries)
cross.show()

# ─────────────────────────────────────────
#  7. LEFT SEMI JOIN
#     Rows from left that HAVE a match in right (no right columns)
# ─────────────────────────────────────────
print("\n========== LEFT SEMI JOIN (Employees where dept exists) ==========")
left_semi = df_employees.join(df_departments, on="dept_id", how="left_semi")
left_semi.show()

# ─────────────────────────────────────────
#  8. LEFT ANTI JOIN
#     Rows from left that DO NOT have a match in right
# ─────────────────────────────────────────
print("\n========== LEFT ANTI JOIN (Employees with no dept match) ==========")
left_anti = df_employees.join(df_departments, on="dept_id", how="left_anti")
left_anti.show()

# ─────────────────────────────────────────
#  9. SELF JOIN
#     Joining a DataFrame with itself (find same-dept pairs)
# ─────────────────────────────────────────
print("\n========== SELF JOIN (Same-department employee pairs) ==========")
emp_a = df_employees.alias("a")
emp_b = df_employees.alias("b")
self_join = emp_a.join(emp_b,
                       (col("a.dept_id") == col("b.dept_id")) &
                       (col("a.emp_id")  != col("b.emp_id")),
                       how="inner") \
                  .select(col("a.emp_name").alias("employee_1"),
                          col("b.emp_name").alias("employee_2"),
                          col("a.dept_id"))
self_join.show()

# ─────────────────────────────────────────
# 10. THREE-WAY JOIN
#     Employees ⟕ Departments ⟕ Salaries
# ─────────────────────────────────────────
print("\n========== THREE-WAY JOIN (Employees + Departments + Salaries) ==========")
three_way = df_employees \
    .join(df_departments, on="dept_id", how="left") \
    .join(df_salaries,    on="emp_id",  how="left")
three_way.show()

# ─────────────────────────────────────────
# 11. NON-EQUI JOIN  (inequality condition)
#     Employees whose salary is above 70000
# ─────────────────────────────────────────
print("\n========== NON-EQUI JOIN (salary > 70000) ==========")
non_equi = df_employees \
    .join(df_salaries, on="emp_id", how="inner") \
    .filter(col("salary") > 70000)
non_equi.show()

print("\n✅ All joins completed successfully!")
spark.stop()
