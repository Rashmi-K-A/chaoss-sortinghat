import datetime
import requests
import logging

GRAPHQL_ENDPOINT = "http://localhost:8000/graphql/"
logger = logging.getLogger(__name__)

def merge_identities(uuid_list):
    to_uuid = uuid_list[0]
    if len(uuid_list)>1:
      for uuid in uuid_list[1:]:
        data = "fromUuids: [\"{}\"], toUuid: \"{}\"".format(uuid, to_uuid)
        query = "mutation { merge(" + data + "){uuid}}"
        res = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
        if res.status_code != 200:
            logger.error(res.text)
    return to_uuid

def add_identities(username, emails):
    uuid_list = []
    for email in emails:
        email = email.strip()
        data = "username: \"{}\", email: \"{}\", source: \"{}\"".format(username, email, "git")
        query = "mutation { addIdentity("+data+"){uuid}}"
        res = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
        if res.status_code == 200:
            res = res.json()
            if 'errors' not in res:
                uuid = res.get('data').get('addIdentity').get('uuid')
                if uuid:
                   uuid_list.append(uuid)
            else:
                logger.error(res.get('errors'))
        else:
            logger.error(res.text)
    if len(uuid_list)>0:
      logger.debug(uuid_list)
      merged_uuid  = merge_identities(uuid_list)
      return merged_uuid
    return None


def add_organizations(orgs):
  for org in orgs:
    org_name = org.split(' ')[0]
    data = "name: \"{}\"".format(org_name)
    query = "mutation { addOrganization(" + data + "){organization{name}}}"
    res = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
    if res.status_code == 200:
      res = res.json()
      if 'errors' in res:
           logger.error(res.get('errors'))
    else:
      logger.error(res.text)


def add_enrollments(uuid, orgs):
    for org in orgs:
        from_date = None
        to_date = None
        if 'from' in org:
            from_date = org.split('from')[-1].split(' ')[1]
            from_date = datetime.datetime.fromisoformat(from_date).isoformat()
        if 'until' in org:
            to_date = org.split('until')[-1].split(' ')[1]
            to_date = datetime.datetime.fromisoformat(to_date).isoformat()
        org_name = org.split(' ')[0]
        data = "organization: \"{}\", ".format(org_name)
        if from_date:
          data += "fromDate: \"{}\", ".format(from_date)
        if to_date:
          data += "toDate: \"{}\", ".format(to_date)
        data += "uuid: \"{}\"".format(uuid)

        query = "mutation { enroll(" + data + "){uuid}}"
        res = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
        if res.status_code != 200:
            logger.error(res.text)



file =  open("dev1.txt", encoding="utf8")
file_data = file.read()
file_data = file_data.replace('\n\t','\t').split('\n')
logger.info('Parsing file:', file.name)
for line in file_data:
  if line and not line.startswith('#'):
    parts = line.split(':')
    username = parts[0]
    user_data = parts[1].split('\t')
    emails = user_data[0].split(',')
    orgs = user_data[1:]
    uuid = add_identities(username,emails)
    add_organizations(orgs)
    add_enrollments(uuid,orgs)
file.close()



