from prefect.filesystems import GitHub

github_block = GitHub.load("my-git-repo")

from prefect.infrastructure.kubernetes import KubernetesJob

kubernetes_job_block = KubernetesJob.load("k8s")

from dog_flow import dog
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=dog,
    name= "dog-deploy-from-python",
    parameters= {"num_barks": 7},
    storage= github_block,
    infrastructure= kubernetes_job_block,
#   path= "/deploy/dog_example/"
#   version=1, 
#   work_queue_name="default",
#   work_pool_name="default-agent-pool"

)

deployment.apply()