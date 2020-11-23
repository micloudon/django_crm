This is a Customer Relationship Management portal created using Django.

It takes in Customers, Products, Orders and stores them in a Mysql Database Hosted on Amazon's RDS cloud service.

Users need to login in, in order to view the page, their data is also stored in the aforementioned Database.

If a user forgets their password, a password reset link can be emailed to them.

(Users can sign up with a fake email if they want to view my project more anonymously, but they won't be able to have their passwords reset).

The Product and Customer tables share a relationship with the Orders table; the orders table takes in Product and Customer and fields.

There is also a user Profile page, where users can update information.

The project is styled using Bootstrap and a bit of CSS.

This project will be hosted on an Amazon Ec2 linux server, using NGINX, it will have SSL security and a domain name. 


