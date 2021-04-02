Microtask 4:
Set up the developer environment of SortingHat (muggle branch).

#### Steps to setup:
1. Forked the [Sorting Hat repository.]() and set up the repo in my local.
2. Pulled the muggle branch from the upstream repository.
3. Created a virtual environment and installed all the libraries in requirements.txt.
4. To run the development server, I had to run the `migrate` and `runserver` commands.

        ./manage.py migrate --settings=config.settings.devel
        ./manage.py runserver --settings=config.settings.devel

5. I had an error with mysqlclient so in config/settings/init.py, I added the following code:

        import pymysql
        pymysql.version_info = (1, 4, 0, "final", 0)
        pymysql.install_as_MySQLdb()

   
6. To run the Sorting Hat UI, I ran `yarn` and `yarn serve` in the sortinghat/ui directory.
7. To login to the UI, I created a user using the following command.

        ./manage.py createsuperuser --settings=config.settings.devel




#### Screenshot of sortinghat muggle branch with development server running:

![Sorting Hat muggle branch](https://github.com/Rashmi-K-A/chaoss-sortinghat/blob/master/assets/sortinghat-muggle.png)
