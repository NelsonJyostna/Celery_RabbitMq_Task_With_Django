1) To run this task in pycharm terminal, first run the celery server by typing the following command.

            celery -A RouteMLApiTask worker -l info -P eventlet

2) Then parallely run the server of api Using following command 

            python manage.py runserver
             
3) Send JSON format data through post method of created API.

    eg. { "id" : 1, "status":"pending", "item":"book" }
             

3) After applying the POST method we get the message broker id in pycharm.
     

4) Lastly We update the status of that item using PATCH method of that created API in POSTMAN.

    eg. { "status" : "pending" }

5) Run the RabbitMQ server on localhost:15672/#/ by installing the Rabbitmq 3.8.16 & Erlang 23.3.4.2
     
     
