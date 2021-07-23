### Docker
Recommended setup

1. Install [docker](https://docs.docker.com/get-docker/)
and [docker-compose](https://docs.docker.com/compose/install/)
2. Build the images, in the project root:
    ```shell script
    docker-compose build
    ```
3. Run containers:
    ```shell script
    docker-compose up
    ```
4. Endpoints: 
    To access endpoints run:
    ```shell script
    curl -X POST -H "Content-Type: application/json" -d @test_file.json http://127.0.0.1:5000/zadanie1
       curl -X POST -H "Content-Type: application/json" -d @test_file.json http://127.0.0.1:5000/zadanie1
    ```
