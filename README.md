# CRUDFlaskMongo

A Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. 

## Steps to setup the application:

### 1. Clone the repository and enter into it.

```bash
git clone https://github.com/nitinsomu/CRUDFlaskMongo
cd CRUDFlaskMongo
```

### 2. Download docker desktop.

https://www.docker.com/products/docker-desktop/

### 3. Provide your MongoDB URI and database name.

In the docker-compose.yml replace <MONGODBURI/DBNAME> with the actual MongoDB URI followed by /DBNAME

### 4. Execute the docker-compose command.

```bash
docker-compose up
```

### 5. Test the application using Postman

In postman, test the application for the following REST API end-points

1) Returns a list of all users  
Method - GET  
URL - http://localhost:5000/users  

2) Returns the user with the specified ID.  
Method - GET  
URL - http://localhost:5000/users/{id}
3) Creates a new user with the specified data.  
Method - POST  
URL - http://localhost:5000/users  

In the body, select raw and enter the json in this format:  
```json
{
    "name" : "Nitin",
    "email" : "nitin.somu13@gmail.com",
    "password" : "dummy_password"
}
```
The response will contain the user ID of the created user.  

4) Updates the user with the specified ID with the new data.  
Method - PUT  
URL - http://localhost:5000/users/{id}
In the body, select raw and enter the json in this format:  
```json
{
    "password" : "dummy_password1"
}
```

Atleast one of the key - values pairs must be present.  

5) Deletes the user with the specified ID  

Method - DELETE  
URL - http://localhost:5000/users/{id} 

