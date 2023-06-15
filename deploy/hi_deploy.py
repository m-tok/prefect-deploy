
from hi_flow import hi
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=hi,
    name="log-simple",
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="qa",
)

if __name__ == "__main__":
    deployment.apply()

