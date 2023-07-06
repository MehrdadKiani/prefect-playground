## prefect --help
```
prefect server start
prefect agent start --pool default-agent-pool --work-queue default

prefect cloud login
prefect cload logout

prefect profile ls
prefect profile inspect default
prefect profile use default
```

Deployment configuration saved to prefect.yaml! You can now deploy using this deployment configuration with:

        $ prefect deploy -n test_flow

You can also make changes to this deployment configuration by making changes to the prefect.yaml file.

To execute flow runs from this deployment, start a worker in a separate terminal that pulls work from the 'first-deploy-worker' work pool:

        $ prefect worker start --pool 'first-deploy-worker'

To schedule a run for this deployment, use the following command:

        $ prefect deployment run 'test-flow/test_flow'