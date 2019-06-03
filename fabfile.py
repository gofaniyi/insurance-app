import os, json
from fabric import task
import subprocess

# @task
# def deployAWS(a):
#     """ Build up deployment script here """                 
#     # sample = os.popen('aws configure list').read()
#     # print(sample)
#     call('exit()')



#     # print(env)

@task
def deployAWS(a):
    # call('aws configure list')
    # import pdb; pdb.set_trace()
    aws_region = os.environ.get('AWS_REGION', 'us-east-2')
    aws_account_no = os.environ.get('AWS_ACCOUNT_NO', '826553820820')
    repository_name = 'britecore'
    docker_image_name = repository_name + '_' + repository_name

    response = call('aws ecr describe-repositories --region {}'.format(aws_region))
    response = json.loads(response)
    repositories = response["repositories"]

    if not check_if_project_repository_exist(repositories, repository_name):

        #Create New Repository
        response = call('aws ecr create-repository --repository-name {0} --region {1}'.format(repository_name, aws_region))
        

    #Get Docker Login command
    docker_login_command = call('aws ecr get-login --no-include-email --region {0}'.format(aws_region))
    docker_login_command = docker_login_command.rstrip()

    #Run Docker Login command
    call(docker_login_command)

    #Tag the docker image of britecore project
    call('docker tag {0}:latest {1}.dkr.ecr.{2}.amazonaws.com/{3}:latest'.format(docker_image_name,aws_account_no, aws_region, repository_name))

    import pdb; pdb.set_trace()
    #Push docker image to ECR repository
    call('docker push {0}.dkr.ecr.{1}.amazonaws.com/{2}:latest'.format(aws_account_no, aws_region, repository_name), return_output=False)



def check_if_project_repository_exist(repositories, repository_name):
    status = False
    if repositories:
        repositoryNames = [repository["repositoryName"] for repository in repositories]
        if repository_name in repositoryNames:
            status = True
    return status




def call(command,return_output=True):
    command = command.split(' ')
    if return_output:
        MyOut = subprocess.Popen(command, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
        response, error = MyOut.communicate()

        if error:
            pass
            #This failed.
            #subprocess.call(["exit"])
        
        return response
    subprocess.call(command)



