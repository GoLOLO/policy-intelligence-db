# policy-intelligence-db
This is an easily searchable and queryable database that stores all state and local air district air policies and regulations as well metadata and keywords associated with each doc.

## Database Choice
1. AWS OpenSearch is best for unstructured documents data like classifying policies and regulations while allowing for full-text search capabilities. It allows for complex search queries including fuzzy matching, proximity queries, and synonym search. 

2. We can start with a simple AWS RDS database to simplify the collection of links and other data that is currently part of the spreadsheet process. With this database we can advance to the OpenSearch database.

## MVP
### v.0 RDS database | data input | data output
1. Relational database (RDS) to capture the data currently being collected in the spreadsheet.

2. Simple UI for data upload - web-based form with similar fields to the spreadsheet.

3. Integrate backend to process form submissions and insert data into the database.

4. Simple search interface for customers with results display in a secure access website.

### v.1 OpenSearch | improved data input | improved customer UI
1. All States and local air districts policies and regulations as well as policy proposals, rule changes, new rules, etc (could be counties or special air districts)
  a. These are all going be a bit different in how they get classified from entity to entity

2. Multiuser collaboration for document and data upload
  a. Users need to be able to easily upload a new doc or update a doc and add new data ad hoc

3. Full-text search capabilities, including fuzzy matching, proximity queries, and synonym search.
  a. This is data that is more than just what's found in the title
  b. User-defined metadata data entry
  c. A user would be able to search for a certain type of policy (e.g. small engines) and the search would tell you all state and districts that have such a policy

### v.2 AI | redlining changes | alerts
1. Train AI
2. **Historical** changes to documents with redlining functionality
3. AI metadata generation assist
  a. User would be able to feed a doc to an the AI and it would offer keywords to store
4. AI summary **assist**
5. Targetted webcrawler for updating database and **alerts**

## User stories
### Personas
1) Policy expert (Garry)
2) Policy librarian (Garry)
3) Policy author/researcher (paying customer)

### Epics
1) As a policy expert i want to index documents (why) so that they are searchable by keyword
2) As a policy librarian I want to easily add docs to a list of docs in a database (why) for future reference.
3) As a policy author I want policy examples when I search by keyword (why) so I can author my own policies quickly/better.

## Rough estimation of costs for v.1
**Startup cost**
- Instance Costs: The cost of m5.large.elasticsearch instances varies by region, but let's say it's around $0.10 per hour     per instance. For two instances over a month (30 days), this would be approximately: 2 instances * $0.10/hour * 24           hours/day * 30 days = $144.
- Storage Costs: Again, this varies, but let's assume it's $0.10 per GB per month. For 45GB, the cost for a month would be:    45 GB * $0.10 = $4.50.
- Data Transfer Costs: These costs can vary widely, but for simplicity, let's allocate a small amount assuming most            operations are internal, say $10.
- Total Estimated Cost for the MVP:
  **The total estimated cost for one month might be around $144 (instances) + $4.50 (storage) + $10 (data transfer) = $158.50.**
  
**Ongoing storage-only costs**
- Storage Costs: If you're using General Purpose SSD (gp2) storage, and assuming the cost is $0.10 per GB-month, the monthly storage cost would be calculated based on the total amount of data stored.
- Instance Costs: Even if the cluster is not actively serving search or indexing requests, the cost of the instances still applies. This cost depends on the instance type and size you've selected.
For instance, if you have a dataset of 50 GB and you are using t2.small.elasticsearch instances (for the sake of an example, let's say they cost around $0.027 per hour), the monthly costs would be:
- Storage Cost: 50 GB * $0.10/GB = $5.00 per month.
- Instance Cost: 2 instances * $0.027/hour * 24 hours/day * 30 days = $38.88 per month.
- Total Holding Cost:
In this scenario, the total cost to just hold the data would be approximately $5.00 (storage) + $38.88 (instances) = **$43.88 per month**.
