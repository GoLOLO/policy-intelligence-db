# policy-intelligence-db
This is the database for storing all state and local air district air policies and regulations as well metadata and keywords associated with each doc.

## Unstructured database MVP
a. MongoDB is best for unstructured documents data like classifying policies and regulations

### Requirements (v.1)
a. All States and local air districts policies and regulations as well as policy proposals, rule changes, new rules, etc (could be counties or special air districts)
  1. These are all gonna a be a bit different in how they get classified from entity to entity
b. Multiuser collaboration for document and data upload
  1. Users need to be able to easily upload a new doc or update a doc and add new data ad hoc
c. Search by metadata
  1. This is data that is more than just what's found in the title
  2. User-defined metadata
  3. A user would be able to search for a certain type of policy (e.g. small engines) and the search would tell you all state and districts that have such a policy

### Advanced requirements (v.2)
a. **Historical** changes to documents
b. AI metadata generation assist
  1. User would be able to feed a doc to an the AI and it would offer keywords to store
c. AI summary **assist**
d. Targetted webcrawler for updating database and **alerts**

### Future considerations: policy-intelligence-ai
a. Train an AI on the data in this database to create policy-intelligence-ai
  1. Try not to paint ourselves into a corner in creating the database so that the policy-intelligence-db help us acheive policy-intelligence-ai
  2. AI would be able to offer ai extertise on any policy in the db
  3. AI wold be able to help user author new policies and regulations based on other state's examples


### Personas
1) Policy expert (Garry)
2) Policy librarian (Garry)
3) Policy author/researcher (paying customer)

### Epics
1) As a policy expert i want to index documents (why) so that they are searchable by keyword
2) As a policy librarian I want to easily add docs to a list of docs in a database (why) for future reference.
3) As a policy author I want policy examples when I search by keyword (why) so I can author my own policies quickly/better.

### To do
1) Build DB
2) Build UI for Garry to upload information and access information
