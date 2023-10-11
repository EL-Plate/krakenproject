## Kraken Task 
D10 dataflow processing task 

## Assumptions 
<ol>
    <li>D10 files will never carry duplicate readings</li>
    <li>D10 files will always follow the same format:</li>
    <ul>
    <li>Header</li>
    <li>026</li>
    <li>028</li>
    <li>030</li>
    <li>...</li>
    <li>Footer</li>
    </ul>
</ol>

## Known Issues
<li>custom management command doesn't pick up eco 7 meter readings</li>
<li>Extension validator in models.py would not be sufficient alone for a file upload to be considered secure</li>

## Potential future issues
<li>Single model for all information, duplicating MSNs and MPANs when perhaps not needed, could be split up. See model improvement for info</li>

## Dependencies
<li>Django-4.2 or higher</li>

## Setup

## Unzip the gzipped tarball

## Open the file in your favourite IDE!

## Check django version 
<ol>
<li>Make sure you are in your outer directory</li>
<li>Open a terminal and type: python -m django --version</li>
<li>If django isn't installed, you’ll get an error telling you “No module named django”.</li>
<li>If you get the error above, you'll need to install Django</li>
<li>Type python -m pip install Django into your terminal window</li>
<li>Once pip has finished installing Django, check the installation by completing step 2. again</li>
</ol>

## Make migrations 
<li>In your terminal type: python manage.py makemigrations</li>
<li>your terminal should display the following text:</li>
Migrations for 'readings':<br>
  readings/migrations/0001_initial.py<br>
    - Create model Reading

## Migrate 
<li>In your terminal type: python manage.py migrate</li>
<li>Migrations should now run</li>

## Create superuser
<li>In your terminal type: python manage.py createsuperuser</li>
<li>You will be prompted to input a username followed by an email and password</li>
<li>complete these fields</li>

## Run the server
<li>In your terminal type: python manage.py runserver</li>
<li>Follow this link: http://127.0.0.1:8000/admin to check the admin server is running</li>

## Log in
<li>Use the credentials you set up earlier to log into the admin page</li>

## Using the custom uploadflow command
<li>in a terminal you can type: python manage.py uploadflow "FILEPATH"</li>
<li>FILEPATH is the absolute path of the file you are trying to upload</li>

## Improvements 
<li>Correct custom management command to include eco 7 meters, this will also mean changes to the Reading model to include day/night reads</li>
<li>Inclusion of tests for custom management command</li>
<li>Introduction of a view based file upload system, using a simple form and incorporation of field validation</li>
<li>Reading(s) "reading_date" field could be a DateField instead of a DateTimeField to remove redundant information</li>
