# job-project

To test or use this project, after you use ./manage.py makemigrations + ./manage.py migrate --run-syncdb, you have to comment the follow lines in forms.py

Lines: 43, 47, 51 and change set parameters in 'choice' as '' on lines 44, 48 and 52.

# The reason

Django will try to find the table mpeople, but was not already created.

After you do this and run the commands to create the database, you can undo the changes to back the original state.
