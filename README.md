# MindMesh

## How to Run MindMesh

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Akshaycr777/MindMesh.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd MindMesh
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application:**
   ```bash
   python app.py
   ```

## AWS-CICD-Deployment-with-Github-Actions

1. **Login to AWS console**

2. **Create IAM user for deployment**

    - **With specific access**
    1. EC2 Access : It is virtual machine
    2. ECR: Elastic Container registry to save your docker image in aws

    - **Description: About the deployment**
    1. Build Docker image of source code
    2. Push your Docker image to ECR
    3. Launch your EC2
    4. Pull your image from ECR in EC2
    5. Launch your Docker image in EC2

    - **Policy**
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

3. **Create ECR repo to store/save docker image**
   - Save the URI: 431445330726.dkr.ecr.us-east-1.amazonaws.com/mindmesh

4. **Create EC2 machine (Ubuntu)**aa

5. **Open EC2 and Install docker in EC2 Machine**

   ```Optional```
   - sudo apt-get update -y
   - sudo apt-get upgrade

   ```Required```
   - curl -fsSL http://get.docker.com -o get-docker.sh
   - sudo sh get-docker.sh
   - sudo usermod -aG docker ubuntu
   - newgrp docker

6. **Configure EC2 as self-hosted runner:**
   setting>actions>runner>new slef hosted runner>choose os> then run command one by one

7. **Setup github secrets:**  

   - GOOGLE_API_KEY
   - GOOGLE_MODEL
   - TAVILY_API_KEY
   - LANGSMITH_TRACING
   - LANGSMITH_ENDPOINT
   - LANGSMITH_API_KEY
   - LANGSMITH_PROJECT
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
