SET search_path TO project_intelligence;

-- Users
INSERT INTO users (email, full_name, role)
VALUES
('admin@company.com', 'System Admin', 'ADMIN'),
('pm@company.com', 'Project Manager', 'PM'),
('analyst@company.com', 'Data Analyst', 'ANALYST');

-- Project
INSERT INTO projects (
    name,
    description,
    status,
    owner_id
)
SELECT
    'Factory Automation Initiative',
    'Digital transformation and automation deployment.',
    'ACTIVE',
    id
FROM users
WHERE email = 'pm@company.com';

-- Tasks
INSERT INTO tasks (
    project_id,
    title,
    description,
    priority
)
SELECT
    p.id,
    'Define KPIs',
    'Identify operational KPIs for automation success.',
    'HIGH'
FROM projects p
WHERE p.name = 'Factory Automation Initiative';

INSERT INTO project_metrics (
    project_id,
    metric_name,
    metric_value
)
SELECT
    p.id,
    'Cycle Time Reduction',
    15.5
FROM projects p
WHERE p.name = 'Factory Automation Initiative';