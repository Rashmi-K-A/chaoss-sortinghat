#### Microtask 10:
Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc. 

#### Issue
 The data returned from Twitter has deprecated fields that are set to null. We can remove these fields from the enriched twitter object since they are always going to be returned as null and are not going to be of much use. 

PR: https://github.com/chaoss/grimoirelab-elk/pull/964 