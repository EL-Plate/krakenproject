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
<li>Extension validator in models.py would not be sufficient alone for a file upload to be considered secure</li>

## Potential future issues
<li>Single model for all information, duplicating MSNs and MPANs when perhaps not needed, could be split up. See model improvement for info</li>

## Dependencies
<li>Django-4.2 or higher</li>

<h1>Setup</h1>

## Unzip the tarball

## Open the file in your favourite IDE!

## Check django version 
<ol>
<li>Make sure you are in your outer directory</li>
<li>Open a terminal and type:</li>

```commandline
 $ python -m django --version
```

<li>If django isn't installed, you’ll get an error telling you “No module named django”.</li>
<li>If you get the error above, you'll need to install Django</li>
<li>In your terminal type:</li>

```commandline
$ python -m pip install Django 
```

<li>Once pip has finished installing Django, check the installation.</li>

```commandline
$ python -m django --version
```

</ol>

## Make migrations 
<li>In your terminal type:</li>

```commandline
$ python manage.py makemigrations
```

<li>your terminal should display the following text:</li>
Migrations for 'readings':<br>
  readings/migrations/0001_initial.py<br>
    - Create model Reading

## Migrate 
<li>In your terminal type:</li>

```commandline
$ python manage.py migrate
```

<li>Migrations should now run</li>

## Create superuser
<li>In your terminal type:</li>

```commandline
$ python manage.py createsuperuser
```

<li>You will be prompted to input a username followed by an email and password</li>
<li>complete these fields</li>

## Run the server
<li>In your terminal type: python manage.py runserver</li>
<li>Follow this link: http://127.0.0.1:8000/admin to check the admin server is running</li>

## Log in
<li>Use the credentials you set up earlier to log into the admin page</li>

## Using the custom uploadflow command
<li>in a terminal you can type:</li>

```commandline
$ python manage.py uploadflow "FILEPATH"
```

<li>FILEPATH is the absolute path of the file you are trying to upload</li>

## Improvements 
<li>Correct custom management command to include eco 7 meters, this will also mean changes to the Reading model to include day/night reads</li>
<li>Inclusion of tests for custom management command</li>
<li>Introduction of a view based file upload system, using a simple form and incorporation of field validation</li>
<li>Reading(s) "reading_date" field could be a DateField instead of a DateTimeField to remove redundant information</li>
<li>Update the command to take multiple D10 files</li>


## model improvements
```commandline
from django.db import models


class MeterPoint(models.Model):
    meter_point_reference_number = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return f"{self.meter_point_reference_number}"


class Meter(models.Model):
    meter_point = models.ForeignKey(
        MeterPoint,
        on_delete=models.CASCADE,
        verbose_name="Meter Point Reference Number"
    )
    meter_serial_number = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return f"{self.meter_serial_number}"


class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    meter_point = models.ForeignKey(
        MeterPoint,
        on_delete=models.CASCADE,
        verbose_name="Meter Point Reference Number"
    )
    meter = models.ForeignKey(
        Meter,
        on_delete=models.CASCADE,
        verbose_name="Meter Serial Number"
    )
    reading = models.FloatField(max_length=5)
    reading_date = models.DateField()

    def __str__(self):
        return f"{self.reading}"
        
 class DataFlow(models.Model):
    data_flow_id = models.AutoField(primary_key=True)
    d10_file = models.FileField(upload_to="/media/" validators=)
    d10_file_name = models.Charfield(max_length=200)
```

## Further improvements & ideas
Idea for incorporating day/night identifiers into the custom command. 
This would also require adding a new field to the model and changing the object creation stage at the end of the uploadfile command.
```commandline
            '''elif fields[0]=="030" && fields[1] =="DY":
                sections.append({
                    "mpan": current_mpan,
                    "msn": current_msn,
                    "date": fields[2],
                    "reading": fields[3],
                    "day_night": "DY"
                })'''
            '''elif fields[0]=="030" && fields[1] =="NT":
                sections.append({
                    "mpan": current_mpan,
                    "msn": current_msn,
                    "date": fields[2],
                    "reading": fields[3],
                    "day_night": "NT"
                })'''
```
