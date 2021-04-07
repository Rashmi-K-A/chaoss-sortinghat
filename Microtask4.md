Microtask 4:
Set up the developer environment of SortingHat (muggle branch).

#### Steps to setup using pip:
1. Forked the [Sorting Hat repository.](https://github.com/chaoss/grimoirelab-sortinghat) and set up the repo in my local.
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

#### Steps to setup using poetry:
1. Forked the [Sorting Hat repository.](https://github.com/chaoss/grimoirelab-sortinghat) and set up the repo in my local.
2. Pulled the muggle branch from the upstream repository.
3. Created a virtual environment and install poetry ( I already had it installed.)
4. To install required packages, run `poetry install`.
5. For mysqlclient, I had the following error:

        8 warnings generated.
        gcc -bundle -undefined dynamic_lookup -arch x86_64 -g build/temp.macosx-10.9-x86_64-3.7/_mysql.o -L/usr/local/Cellar/mysql/8.0.22_1/lib -lmysqlclient -lssl -lcrypto -lresolv -o build/lib.macosx-10.9-x86_64-3.7/_mysql.cpython-37m-darwin.so
        ld: library not found for -lssl
        clang: error: linker command failed with exit code 1 (use -v to see invocation)
        error: command 'gcc' failed with exit status 1

    To fix this, I ran `brew info openssl` and set `LDFLAGS` and `CPPFLAGS` using the info that was printed. I was able to install mysqlclient after this

5. To run the development server, I had to run the `migrate` and `runserver` commands.

        ./manage.py migrate --settings=config.settings.devel
        ./manage.py runserver --settings=config.settings.devel
   
6. To run the Sorting Hat UI, I ran `yarn` and `yarn serve` in the sortinghat/ui directory.
7. To login to the UI, I created a user using the following command.

        ./manage.py createsuperuser --settings=config.settings.devel


#### Screenshot of sortinghat muggle branch with development server running:

![Sorting Hat muggle branch](https://github.com/Rashmi-K-A/chaoss-sortinghat/blob/master/assets/sortinghat-muggle.png)
