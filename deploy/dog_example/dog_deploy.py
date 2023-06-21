from dog_flow import dog
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=dog,
    name= "dog-deploy-from-python",
    parameters= {"num_barks": 7},
    work_queue_name="dev",
)

deployment.apply()