from demo import pipeline
from prefect.deployments import Deployment
from prefect.filesystems import LocalFileSystem

deployment2 = Deployment.build_from_flow(
    flow=pipeline,
    name="Second Python Deployment Example",
    tags=["extract"],
)

if __name__ == "__main__":
    deployment2.apply()