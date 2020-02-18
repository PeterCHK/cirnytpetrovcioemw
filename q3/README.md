1. The solution is made by Python Flask.
2. All the pip dependencies are extracted (pip3 freeze > requirements.txt)
3. The docker image is set as public and located at docker hub.

To run locally,
pip3 install -r requirements.txt
python3 shorturl.py

#POST method
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https:www.google.com"}' http://localhost:5000/newurl

#GET method
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/<shorturl>

The current solution is stored as a python dictionary. However, if cost and time are allowed, I would implement the database solution on MariaDB RDS and use of write and read replicas.

High availability​ : ​ Please​ make​ it​ highly available and​ no​ single​ point​ ​ of failure.
#use of classic load balancer.
Scalability​ :​ Please​ make​ it​ scalable.
#use of image and scale by auto scaling
Scaling​ target​ : ​ 1000+​ req/s,​ after​ scaling-up/out without​ major​ code​ change
#perform 100 curl req/s on a t2.micro and use 10 machine to perform curl at 1000 req/s, see the effect of auto scaling

● The​ application​ deliverable​ should​ be​ self-contained,​ preferably​ an​ automated
deployment​ package / container image,​ such​ that​ we​ can​ deploy​ it​ easily
#it is delivered as a docker container image
● The​ system/infrastructure​ should​ be​ also​ documented​ OR​ automated​ (via​ e.g.
shell​ script)
#documented
● Please​ briefly​ explain​ your​ system​ and​ say​ why​ you​ are going​ to​ implement
like​ that.
#Python Flask is a light web framework for making simple API endpoints.
#MySQL/MariaDB RDS has the largest page compared to PostgreSQL and non-relational databases without restricting to AWS (Aurora), as a multi-platform solution.
#Docker image is self contained and can scale rapidly.
#Classic load balancer can perform load balancing at network layer as well as application layer.

● Please​ state​ any​ assumption​ and​ limitation​ of​ ​the system​ implemented.
1. Input is in correct format
2. No malicious attacks
3. Required packages are downloadable
4. No expiry date on docker hub hosting public images
5. Port is not in use
