-- 1
SELECT monthname(charged_datetime) AS month, sum(amount) AS revenue
FROM billing
WHERE monthname(charged_datetime) = "March";
-- 2
SELECT sum(amount)
FROM billing
WHERE billing.client_id = 2;
-- 3
SELECT domain_name
FROM sites
WHERE sites.client_id = 10;
-- 4.1
SELECT client_id, count(domain_name) AS number_of_sites, monthname(created_datetime) AS month_created, year(created_datetime) AS year_created
FROM sites
WHERE client_id = 1
GROUP BY month_created, year_created;
-- 4.2
SELECT client_id, count(domain_name) AS number_of_sites, monthname(created_datetime) AS month_created, year(created_datetime) AS year_created
FROM sites
WHERE client_id = 20
GROUP BY month_created, year_created;
-- 5
SELECT sites.domain_name AS website, count(leads.leads_id) AS number_of_leads, date_format(leads.registered_datetime, "%M, %d, %Y") AS date_generated
FROM sites
JOIN leads ON leads.site_id = sites.site_id
WHERE year(leads.registered_datetime) = 2011
	AND (monthname(leads.registered_datetime) = "January" 
    OR (monthname(leads.registered_datetime) = "February" AND dayofmonth(leads.registered_datetime) < 16 ))
GROUP BY website;
-- 6
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, count(leads.leads_id) AS number_of_leads
FROM leads
JOIN sites ON sites.site_id = leads.site_id
	LEFT JOIN clients on clients.client_id = sites.client_id
WHERE year(leads.registered_datetime) = 2011
GROUP BY client_name;
-- 7
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, count(leads.leads_id) AS number_of_leads, monthname(leads.registered_datetime) AS registered_month
FROM leads
JOIN sites ON sites.site_id = leads.site_id
	LEFT JOIN clients on clients.client_id = sites.client_id
WHERE year(leads.registered_datetime) = 2011
	AND month(leads.registered_datetime) < 7
GROUP BY client_name, registered_month;
-- 8.1
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, count(leads.leads_id) AS number_of_leads, sites.domain_name AS website
FROM leads
JOIN sites ON sites.site_id = leads.site_id
	LEFT JOIN clients on clients.client_id = sites.client_id
WHERE year(leads.registered_datetime) = 2011
GROUP BY client_name, website
ORDER BY clients.client_id;
-- 8.2
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, count(leads.leads_id) AS number_of_leads, sites.domain_name AS website
FROM leads
JOIN sites ON sites.site_id = leads.site_id
	LEFT JOIN clients on clients.client_id = sites.client_id
GROUP BY client_name, website
ORDER BY clients.client_id;
-- 9
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, date_format(billing.charged_datetime, "%M, %Y") AS billing_month, sum(billing.amount) AS collected_revenue
FROM billing
LEFT JOIN clients ON clients.client_id = billing.client_id
GROUP BY client_name, billing_month
ORDER BY clients.client_id;
-- 10
SELECT concat(clients.first_name, " ", clients.last_name) AS client_name, group_concat(sites.domain_name separator ' / ') AS sites
FROM clients
JOIN sites ON sites.client_id = clients.client_id
GROUP BY client_name;