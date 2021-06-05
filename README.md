1) To run this task in pycharm terminal, first run the celery server by typing the following command.

            celery -A RouteMLApiTask worker -l info -P eventlet

2) Then parallely run the server of api Using following command 

            python manage.py runserver
             
3) Send JSON format data through post method of created API.

    eg. { "id" : 1, "status":"pending", "item":"book" }
             

3) After applying the POST method we get the message broker id in pycharm.
     

4) Lastly We update the status of that item using patch method of that created API in POSTMAN.

    eg. { "status" : "pending" }
     
