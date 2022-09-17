Backend Documentation

Environment :-  Python 3.10, 
                Django 4,1,
                Djangorestframework 3.13.1
                Djangorestframework-simplejwt 5.2.0,
                mysql-connector 2.2.9,
                mysql-connector-python 8.0.28,

Authentication Type :- JWT Authentication

Prerequisite :- 1) Python
                2) Django       
                2) Django ORM

The functionalities avialable in this project are,
1) User Registration - Admin, Member
2) Login - Admin, Member
3) Book's Data Operations
    i) Add a book to list
    ii) Delete a book 
    iii) Update book information
    iv) Get the list of all books

The use of above functionaity,

1) User Registration - Admin, Member

    To add a new user, provide the basic data of user to save the information. 

    URL:- http://127.0.0.1:8000/register/ 
    Method = POST

    Example:-
                {
                    "username" : "testuser",           // Username
                    "email" : "testuser@nomail.com",   // Email ID
                    "password" : "testuser",           // password
                    "is_superuser" : true              // True for admin peoples only

                }
    Here "is_superuser" flag is used for differentiating between admin user and member/student user

2) Login - Admin, Member

    To loin as a user, provide the username and password. 
    URL:- http://127.0.0.1:8000/login/ 
    Method = POST
    Example:-
                {
                    "username" : "testuser",           // Username
                    "password" : "testuser",           // password
                }

3) Book's Data Operations

    To perform operations on book to list, you must have to login as admin. 
    URL:- http://127.0.0.1:8000/login/ 
    Method = POST
    Example:-
                {
                    "username" : "testuser",           // Username
                    "password" : "testuser",           // password
                }

    After login you will get Access and Refresh Token, save it for future use.

3.1) Add a book to list
        To add a new book to list, you must have to login as admin.
        use that ACCESS TOKEN for authorization purpose, Add that token in "POSTMAN/Authorization/Bearer Token/"
        and got to following URL,
        URL:- http://127.0.0.1:8000/login/ 
        
        Method = POST
        Example:-
                    {
                        "name" : "",              // Book Name
                        "author" : "",            // Author's Name
                    }
        Send the request. Book is added in the list.

3.2) Delete a book
        To delete a new book to list, you must have to login as admin.
        use that ACCESS TOKEN for authorization purpose, Add that token in "POSTMAN/Authorization/Bearer Token/"
        and got to following URL,
        URL:- http://127.0.0.1:8000/login/ 
        
        Method = DELETE
        Example:-
                    {
                        "is" : 7              // Book id
                    }
        Send the request. Book is deleted from the list.

3.3) Update book information
        To update a book information to list, you must have to login as admin.
        use that ACCESS TOKEN for authorization purpose, Add that token in "POSTMAN/Authorization/Bearer Token/"
        and got to following URL,
        URL:- http://127.0.0.1:8000/login/

        Method = UPDATE
        Example:-
                    {
                        "name" : "",              // Book Name
                        "author" : "",            // Author's Name
                    }
        Send the request. Book's information is updated in the list.

3.4) Get the list of all books
        To Get the list of all books, you must have to login as admin.
        use that ACCESS TOKEN for authorization purpose, Add that token in "POSTMAN/Authorization/Bearer Token/"
        and got to following URL,
        URL:- http://127.0.0.1:8000/register/ 

        Method = GET
        Example:-
                    {
                        "name" : "",              // Book Name
                        "author" : "",            // Author's Name
                    }
        Send the request. 