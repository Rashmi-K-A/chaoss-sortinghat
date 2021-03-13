Microtask 3:
Based on the elasticsearch documents produced by micro-mordred and source code of chaoss/grimoirelab-elk, try to answer the following questions:

What is the meaning of the JSON attribute author_id? 
   ID of author from SortingHat, will be different for different identities of the same profile.
What is the meaning of the JSON attribute author_org_name?
   The organization that author belongs to. Author can belong to multiple organizations as well.
What is the meaning of the JSON attribute author_uuid?
   ID of the profile of author in SortingHat
What is the meaning of the JSON attribute author_domain?
   Domain associated with the profile of an author
What is the meaning of the JSON attribute uuid? 
  Unique ID for item provided by Perceval
What is the meaning of the JSON attribute utc_commit?
  The data of the commit in UTC.
What is the meaning of the JSON attribute origin?
  The URL where repo was retrieved from


As part of Microtask 10, I created a PR to the chaoss/grimoirelab-elk repo that helped me familiarize myself with identity fields like author_id, author_org_name etc., as well as other metadata fields and data source specific fields.

