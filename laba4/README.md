# Lab 4
1. Learned about docker in the official documentation
2. Run following commands to test is docker installed successfully:
   ```
   sudo docker -v
   sudo docker -h
   sudo docker run docker/whalesay cowsay Docker is fun
    ```
   Output:
   ```
   $ sudo docker -v
   $ sudo docker -h
   $ sudo docker run docker/whalesay cowsay Docker is fun
   ``` 
   Execution output for these commands located at `test_output.txt` file of this repo.
3. Learned the Dockerfile documentation
4. Create new Dockerfile with Django web app from previous lab
5. Created new DockerHub [repository](https://hub.docker.com/repository/docker/bodia1132/lab4) for this lab 
6. Build and push [image](https://hub.docker.com/layers/127939785/bodia1132/lab4/django/images/sha256-5ed76fc8a46a06215422739b95a9f67bea222be4d5a634bd867ed10850b27307?context=explore) to the repo:
   ```
   sudo docker build --tag bodia1132/lab4:django .
   sudo docker push bodia1132/lab4:django
   ```
7. Run the docker image with 
   ```
   sudo docker run -it --name=django-page --rm --publish 8000:8000 bodia1132/lab4:django
   ```
   Web page works well
8. Create container for minotoring utility:
   1. Create Dockerfile.monitor
   2. Build image with 
      ```
      $ sudo docker build --tag monitor_utility:django --file Dockerfile.monitor . 
      ```
   3. Run both containers.
      ```
      $ sudo docker run -it --name=django-page --rm --publish 8000:8000 bodia1132/lab4:django
      $ sudo docker run --net=host --name=monitor-util --rm -it monitor_utility:django
      ```
	  При запуску дуругого контейнера можна побачити що на терміналі де запускувся сайт приходить інформація.
	  [28/Nov/2020 13:26:40] "GET / HTTP/1.1" 200 166
	  [28/Nov/2020 13:30:06] "GET /health HTTP/1.1" 301 0
	  [28/Nov/2020 13:30:06] "GET /health/ HTTP/1.1" 200 90
	  [28/Nov/2020 13:30:22] "GET / HTTP/1.1" 200 166
	  [28/Nov/2020 13:30:23] "GET / HTTP/1.1" 200 166
	  [28/Nov/2020 13:30:59] "GET /health HTTP/1.1" 301 0
	  [28/Nov/2020 13:30:59] "GET /health/ HTTP/1.1" 200 90
	  [28/Nov/2020 13:32:26] "GET /health HTTP/1.1" 301 0
	  [28/Nov/2020 13:32:26] "GET /health/ HTTP/1.1" 200 90
	  [28/Nov/2020 13:32:46] "GET / HTTP/1.1" 200 166
	  [28/Nov/2020 13:32:53] "GET /health/ HTTP/1.1" 200 90
	  
	  CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
	  fa07bb31d2c9        django-page         5.20%               69.24MiB / 1.941GiB   3.48%               13.7kB / 9.57kB     32.7MB / 0B         3
