# Django_GPT_Summarize
```
The project is located at `/home/ec2-user/apps/gptdjango`.

Within the project:

- `init.py` is used to store configuration files, databases, and GPT configuration parameters.
- `gptapi/views.py` is the file for handling requests.
- `gptdjango`: This directory contains the project's configuration files.
- `pythonev`: This directory contains the virtual environment.

```

## Set Up

### Activating the Virtual Environment

Enter the project directory in SSH and activate the environment:

```
cd /home/ec2-user/apps/gptdjango/pythonev/
source pythonenv_37/bin/activate
```

### Starting gunicorn in supervisor

Enter the supervisor management console:

```
supervisorctl -c ~/etc/supervisord.conf
```

Update and restart `myDJ` to launch the application through gunicorn's Django project:

```
update
restart myDJ
```

Start nginx:

```
# Start the Nginx service:
sudo systemctl start nginx
```

### Details

1. Create a Django project.

2. Define route URL addresses in `gptdjango/gptdjango/urls.py`.

3. Write CBV (Class-Based Views) in `gptdjango/gptapi/views.py`.

4. Configure the database and GPT parameters.

5. Create ORM (Object-Relational Mapping) models.

6. Migrate the database.

7. Deploy the Django project to an AWS EC2 instance and configure Nginx, Gunicorn, and supervisor.

8. Initiate a test request:

   - Method: POST
   - Data type: json
   - Data: `{"text":"test_post"}`
   - URL: `54.224.192.53/summarize/`

### Note
The request data must have a key named "text", and the data cannot be empty. The request method can only be POST. 
The request data size must not exceed the limit set by the admin (5000).
The Greenwich Mean Time (GMT) / Coordinated Universal Time (UTC) +4 is used in the timestamp.
