1. Create a new app called `store`
2. Define a model called `Product` with the following fields:
    - `name`: CharField with a maximum length of 100 characters
    - `description`: TextField
    - `price`: DecimalField with a maximum of 10 digits and 2 decimal places
    - `stock`: IntegerField with a default value of 0
    - `created_at`: DateTimeField that auto-populates with the current date and time when a product is created
    add anything else you think is necessary for the model
3. Add product to admin panel
4. Create a Product Object
5. Add view / url / template to display all products