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


## Setup


## Improvements 
<li>Correct custom management command to include eco 7 meters, this will also mean changes to the Reading model to include day/night reads</li>
<li>Inclusion of tests for custom management command</li>
<li>Introduction of a view based file upload system, using a simple form and incorporation of field validation</li>
<li>Reading(s) "reading_date" field could be a DateField instead of a DateTimeField to remove redundant information</li>
<li>Validation of file contents before upload, some examples below</li>

## Model Improvements

