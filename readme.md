## Hướng dẫn submit code spark operator với Apache Airflow
### Chuẩn bị:
    - Apache Airflow
    - Source code Spark Java
    - Cụm Kubernetes

    - Java 11
    - Maven
    - Spark 3.5.3
    ... Một số jar file cần thiết khác

    - Jar file code spark: Sau khi build mvn
    - Dockerfile: Phục vụ cho việc build image spark
    - File yaml để deploy spark application: Phục vụ cho việc deploy spark application trên k8s
    - Dag file: Phục vụ cho việc submit code spark operator với Apache Airflow
### Chi tiết từng bước:
    - Bước 1: Build file jar code spark
            - Tôi đã chuẩn bị sẵn 1 file jar trong thư mục images của repository: 
                + Code spark chỉ đơn giản print ra màn hình 1 dòng chữ "Hello World!"
    - Bước 2: Build image spark
            - Tôi sử dụng base image: spark:3.5.3 images này đã có java 11 bên trong.
            - Lệnh:
                + Tại thư mục images:
                    Build images: docker build -t appledog2k/spark-test .
                    Push images to dockerhub: docker push appledog2k/spark-test:latest
    - Bước 4: Viết yaml phục vụ cho việc deployment application spark và phân quyền khi sử dụng
            - Tôi đã chuẩn bị sẵn 1 file yaml trong thư mục dags/kubenetes của repository:
                + File yaml này sẽ deploy 1 spark application với image spark đã build ở trên
    - Bước 3: Tạo dags file
            - Tôi đã chuẩn bị sẵn 1 file dag trong thư mục dags của repository:
                + File dag này sẽ submit code spark với image spark đã build ở trên

### 1 số lệnh test
    - Nếu muốn submit job thủ công thông qua file yaml
        kubectl apply -f spark-pi.yaml
                    
