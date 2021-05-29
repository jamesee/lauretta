# Question 5

I followed closely the program structure of "Creating Simple Login API using Go and Mongodb". However, the mongodb driver used are obsolete. I debugged the codes, added the go-validator library, and packaged the codes into a multi-staged docker container.

To test the code, 

```
$ cd Q5
$ docker-compose up -d

$ cd test
$ bash test-all.sh
```

Reference :

- Go Validator v10 \
<https://medium.com/tunaiku-tech/go-validator-v10-c7a4f1be37df>
<https://github.com/go-playground/validator.git>

- Creating Simple Login API using Go and Mongodb\
<https://theshiva5.medium.com/creating-simple-login-api-using-go-and-mongodb-9b3c1c775d2f>

- Multi-stage Docker Builds\
<https://blog.akbuluteren.com/blog/multi-stage-docker-build>

- MongoDB Go driver \
<https://github.com/mongodb/mongo-go-driver.git>