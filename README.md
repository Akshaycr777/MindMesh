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

2.  **Create IAM user for deployment**

    - **With specific access**: 
    1. EC2 Access : It is virtual machine
    2. ECR: Elastic Container registry to save your docker image in aws

    - **Description: About the deployment**
    1. Build Docker image of source code
    2. Push your Docker image to ECR
    